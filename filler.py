from openai import OpenAI
import re
import speech_recognition as sr

client = OpenAI(api_key="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")


def generate_response(user_input):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": """
                for the below text return integer total count of all filler words
                return only the total count 
          """ 
          +user_input
      },

    ],
    temperature=0,
    max_tokens=256,
    top_p=1
  )

  return response.choices[0].message.content


def compute_filler(audio_file):

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        transcript = recognizer.recognize_google(audio_data)

    nWords = len(transcript.split())
    fillers = generate_response(transcript)

    pattern = r'\d+'
    
    matches = re.findall(pattern, fillers)
    
    nFillers =  int(matches[0])

    return nWords,nFillers
