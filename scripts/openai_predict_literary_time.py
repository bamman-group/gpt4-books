import openai

API_ORG = ""
API_KEY = ""

openai.organization = API_ORG
openai.api_key = API_KEY

def predict(passage):
  text="""Read the following passage of fiction. Then do five things. 

1: Briefly summarize the passage.
 
2: Reason step by step to decide how much time is described in the passage. If the passage doesn't include any explicit reference to time, you can guess how much time the events described would have taken. Even description can imply the passage of time by mentioning the earlier history of people or buildings. But characters' references to the past or future in spoken dialogue should not count as time that passed in the scene. Report the time using units of years, weeks, days, hours, or minutes. Do not say zero or N/A. 

3: If you described a range of possible times in step 2 take the midpoint of the range. Then multiply to convert the units into minutes. 

4: Report only the number of minutes elapsed, which should match the number in step 3. Do not reply N/A. 

5: Given the amount of speculation required in step 2, describe your certainty about the estimate--either high, moderate, or low.
 

Input:

TWENTY-FIVE It was raining again the next morning, a slanting gray rain like a swung curtain of crystal beads. I got up feeling sluggish and tired and stood looking out of the windows, with a dark harsh taste of Sternwoods still in my mouth. I was as empty of life as a scarecrow's pockets. I went out to the kitchenette and drank two cups of black coffee. You can have a hangover from other things than alcohol. I had one from women. Women made me sick. I shaved and showered and dressed and got my raincoat out and went downstairs and looked out of the front door. Across the street, a hundred feet up, a gray Plymouth sedan was parked. It was the same one that had tried to trail me around the day before, the same one that I had asked Eddie Mars about. There might be a cop in it, if a cop had that much time on his hands and wanted to waste it following me around. Or it might be a smoothie in the detective business trying to get a noseful of somebody else's case in order to chisel a way into it. Or it might be the Bishop of Bermuda disapproving of my night life.

Output:

1: A detective wakes up 'the next morning,' looks out a window for an undefined time, drinks (and presumably needs to make) two cups of coffee, then shaves and showers and gets dressed before stepping out his front door and seeing a car. 

2: Making coffee, showering, and getting dressed take at least an hour. There's some ambiguity about whether to count the implicit reference to yesterday (since this is 'the next morning') as time elapsed in the passage, but let's say no, since yesterday is not actually described. So, an hour to 90 minutes. 

3: 1.25 hours have elapsed. Multiplying by 60 minutes an hour that's 75 minutes.
 
4: 75 minutes.
 
5: Low confidence, because of ambiguity about a reference to the previous day.

Input:

CHAPTER I  "TOM!" No answer.  "TOM!"  No answer.  "What's gone with that boy, I wonder? You TOM!" No answer.  The old lady pulled her spectacles down and looked over them about the room; then she put them up and looked out under them. She seldom or never looked _through_ them for so small a thing as a boy; they were her state pair, the pride of her heart, and were built for "style," not service--she could have seen through a pair of stove-lids just as well. She looked perplexed for a moment, and then said, not fiercely, but still loud enough for the furniture to hear:  "Well, I lay if I get hold of you I'll--"  She did not finish, for by this time she was bending down and punching under the bed with the broom, and so she needed breath to punctuate the punches with. She resurrected nothing but the cat.  "I never did see the beat of that boy!" She went to the open door and stood in it and looked out among the tomato vines and "jimpson" weeds that constituted the garden. No Tom. So she lifted up her voice at an angle calculated for distance and shouted: "Y-o-u-u TOM!" There was a slight noise behind her and she turned just in time to seize a small boy by the slack of his roundabout and arrest his flight.

Output:

1: An old lady calls for a boy named Tom, checks for him under the bed, goes to the open door and calls for him — then finally catches him.

2: The lady's actions are described minutely and seem rapid; they probably took two to four minutes. The lady also alludes to Tom's past bad behavior, but references to the past in dialogue should not count as time passing in the scene. 

3: Three minutes have elapsed.

4: 3 minutes.

5: High confidence.

Input: 

%s

Output:

""" % passage

  completion = openai.ChatCompletion.create(

    # ChatGPT
    model="gpt-3.5-turbo",

    # GPT-4
    # model="gpt-4",

    messages=[
      {"role": "user", "content": text}
    ],
    temperature=0.0
  )

  return completion["choices"][0]["message"]["content"], completion


passage="The cop looks worshipful. An elderly woman, easing heavy shopping bags to the floor, inquires reverently into the stock of religious materials. But this is only a ploy. Once answers are forthcoming, she confesses her fear that the earth has become peopled by the alien occupants of flying saucers. She looks at the shopgirl imploringly. A student comes looking for esoteric titles. He stands at attention by the counter and rattles them off. Then he lingers there, volunteering, for some reason, unabashed insights into the sources of his frustrations. The girl listens carefully. She listens to all of them. But she smiles in such a secret way that they cannot be sure she has heard. Most people buy books to pay her for her time. I buy books so 226 ELBOW ROOM I can stand at the counter and get a closer inspection of her mystery. This time I am sure her face is the source of all this interest. It is a free face, a fresh face. In it I can see no servitude to the expressions of faces I have seen before. Hers is a smile completely unaware of any predecessor. It derives entirely from within itself. Her mystery, I think, is an awareness of this liberation from the familiar. But not even her smile seems conscious of this."
content, full=predict(passage)
print(content)
print(full)


