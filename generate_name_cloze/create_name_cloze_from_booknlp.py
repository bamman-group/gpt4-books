# Extract passages from a BookNLP-processed book where there is exactly one PROP entity (a PER), one token long.

import sys, re

sids={}
sids_start={}
sids_end={}
tokens=[]
ent_tokens={}

target_context=50
min_context=40
max_context=60

invalid_names=set(["god", "dad", "mother", "father", "mama", "daddy", "ma", "papa", "mum", "jesus", "christ", "pa", "mom", "kid"])

def get_closest_ner(i):

	nextEnt=None
	prevEnt=None

	for j in range(i+1, len(tokens)):
		if j in ent_tokens:
			nextEnt=j
			break

	for j in range(i-1, -1, -1):
		if j in ent_tokens:
			prevEnt=j
			break

	return prevEnt, nextEnt

def get_passage(i):

	prevEnt, nextEnt=get_closest_ner(i)

	if prevEnt is not None:
		excludePrevSid=sids[prevEnt]
		startSid=excludePrevSid+1
	else:
		startSid=0

	if nextEnt is not None:
		excludeNextSid=sids[nextEnt]
		endSid=excludeNextSid-1
	else:
		endSid=sids[len(tokens)-1]

	
	must_include=sids[i]

	cands={}
	for start_cand in range(startSid,must_include+1):
		for end_cand in range(must_include,endSid+1):
			length=sids_end[end_cand] - sids_start[start_cand]
			if length > min_context and length < max_context:
				cands[start_cand, end_cand]=abs(length-target_context)

	if len(cands) > 0:
		(start_sid, end_sid),v=sorted(cands.items(), key=lambda item: item[1])[0]
		start_tok=sids_start[start_sid]
		end_tok=sids_end[end_sid]

		assert start_tok <= i and end_tok >= i

		return start_tok, end_tok


	else:
		return None, None

	return None, None


def read_toks(filename):
	lastSid=None
	lastOffset=0

	with open(filename) as file:
		file.readline()
		for line in file:
			cols=line.rstrip().split("\t")
			
			sid=int(cols[1])
			token=cols[4]
			tid=int(cols[3])

			sids[tid]=sid

			if sid not in sids_start:
				sids_start[sid]=tid

			if sid != lastSid and lastSid is not None:
				lasttid=int(tid)-1
				sids_end[lastSid]=lasttid

			lastSid=sid

			onset=int(cols[6])
			offset=int(cols[7])

			if onset > lastOffset:
				token=' ' + token

			tokens.append(token)

			lastOffset=offset

		sids_end[lastSid]=tid

def read_ents(filename):

	idd=filename.split("/")[-1]
	idd=re.sub("\.entities$", "", idd)

	ents={}

	single_per_ents={}

	with open(filename) as file:
		file.readline()
		for line in file:
			cols=line.rstrip().split("\t")
			prop=cols[3]
			cat=cols[4]
			start=int(cols[1])
			end=int(cols[2])

			if prop == "PROP":
				ents[start,end]=1

			text=cols[5]

			length=end-start

			if prop == "PROP" and cat == "PER" and length == 0:
				single_per_ents[start]=1


	for start,end in ents:
		for i in range(start, end+1):
			ent_tokens[i]=1


	for i in single_per_ents:

		start, end=get_passage(i)

		if start == None:
			continue

		invalid=False
		for j in range(start,end):
			if j in ent_tokens and j != i:
				invalid=True

		assert invalid is False
		if invalid is False:
			# print(i, end-start)
			orig=tokens[i]

			if orig.lower().lstrip().rstrip() in invalid_names:
				continue

			# one additional check to make sure the same word as the original does not show up in the passage
			dupFlag=False
			for t in range(start, end+1):
				tok=tokens[t]
				if t != i and tok.lower().lstrip().rstrip() == orig.lower().lstrip().rstrip():
					dupFlag=True


			if dupFlag is True:
				continue

			if tokens[i].startswith(" "):
				tokens[i]=" [MASK]"
			else:
				tokens[i]="[MASK]"
			if end-start > min_context and end-start < max_context:
				print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (idd, end-start, i, start, end, orig.lstrip().rstrip(), ''.join(tokens[start:end+1]).lstrip().rstrip()))


read_toks(sys.argv[2])
read_ents(sys.argv[1])				