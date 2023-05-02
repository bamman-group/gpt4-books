import openai

API_ORG = ""
API_KEY = ""

openai.organization = API_ORG
openai.api_key = API_KEY

def predict(passage):
  text="""What was the year in which the following passage was written?  You must make a prediction of a year, even if you are uncertain.

  Example:

  Input: "He felt his face. 'I miss sneering at something I love. How we used to love to gather in the checker-tiled kitchen in front of the old boxy cathode-ray Sony whose reception was sensitive to airplanes and sneer at the commercial vapidity of broadcast stuff.’"
  Output: <year>1996</year>

  Input: "The multiplicity of its appeals—the perpetual surprise of its contrasts and resemblances! All these tricks and turns of the show were upon him with a spring as he descended the Casino steps and paused on the pavement at its doors. He had not been abroad for seven years—and what changes the renewed contact produced! If the central depths were untouched, hardly a pin-point of surface remained the same. And this was the very place to bring out the completeness of the renewal. The sublimities, the perpetuities, might have left him as he was: but this tent pitched for a day’s revelry spread a roof of oblivion between himself and his fixed sky."
  Output: <year>1905</year>

  Input: %s
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


passage="She ran a damp cloth over the keyboard. He was close enough to smell: limes and cloves and the lingering afterburn of sex, washed away but still there if you knew about it, like a removed stain. “Everyone was coming, you shudda seen it,” he told Nazneen, as though she had not. “Then—smack”—he clicked his fingers—“all gone again.” His beard had grown in. Even a beard could not hide how handsome he was. She remembered the meeting in the community hall at the edge of the estate, sitting below the stage, flaming inside her red sari, watching him pull the audience to his side, running home and waiting for him, knowing yet scarcely believing he would come. That was how she wanted him, like that, not with his feet on her coffee table and holes in his socks. “When we were going to organize that march ... different story.” He bent down and unraveled some wires. “Make another one.” “Lion Hearts were going to march against us. We were going to march against them. But they bottled it. They knew they were going to be outnumbered. We were going to hammer ’em.” He banged his head on the table coming up again, and rubbed it with his fist."
content, full=predict(passage)
print(content)
print(full)


