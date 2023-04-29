filename=$1
output_id=$2

# run BookNLP to tokenize the text and extract entities
python run_booknlp.py $filename $output_id

# create name cloze examples from those BookNLP files
python create_name_cloze_from_booknlp.py booknlp_output/$output_id/$output_id.entities booknlp_output/$output_id/$output_id.tokens > booknlp_output/$output_id/$output_id.name_cloze.txt