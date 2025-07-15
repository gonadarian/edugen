import os
import json

import requests
import base64
from openai import OpenAI
from dotenv import load_dotenv

from words import all_words
from prompts import all_prompts


load_dotenv()

key = os.getenv("OPENAI_KEY")
token = os.getenv("GOOGLE_TOKEN")
project = "gonadarian"
url = "https://texttospeech.googleapis.com/v1/text:synthesize"


def get_text_speech(text):
    speech_input = {"text": text}
    return get_speech(speech_input)


def get_ssml_speech(text, phoneme):
    ssml = f"""<speak><phoneme alphabet="ipa" ph="{phoneme}">{text}</phoneme></speak>"""
    speech_input = {"ssml": ssml}
    return get_speech(speech_input)


def get_speech(speech_input):
    headers = {
        "Authorization": f"Bearer {token}",
        'x-goog-user-project': project,
        'Content-Type': 'application/json',
    }

    payload = json.dumps({
        "input": speech_input,
        "voice": {
            "languageCode": "en-gb",
            "name": "en-GB-Neural2-C",
            "ssmlGender": "FEMALE"
        },
        "audioConfig": {
            "audioEncoding": "MP3"
        }
    })

    response = requests.post(url, headers=headers, data=payload)
    print("response status_code:", response.status_code)
    print("response text:", response.text)

    return json.loads(response.text)


def audio_generate(text):
    file = text
    if "|" in text:
        parts = text.split("|")
        speech = get_ssml_speech(parts[0], parts[1])
        file = f"{parts[0]} ({parts[1]})"
    else:
        speech = get_text_speech(text)

    audio_content = speech['audioContent']
    print(audio_content)

    decoded_audio = base64.b64decode(audio_content)
    with open(f"output/{file}.mp3", "wb") as f:
        f.write(decoded_audio)


def image_generate(term):
    client = OpenAI(
        api_key=key,
    )

    prompt = all_prompts[use_prompt].format(term=term)
    print(f"term: '{term}', prompt type: '{use_prompt}', prompt: '{prompt}'")

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    print(f"response: {response}")
    print(f"image: {image_url}")


do_audio = False
do_image = not do_audio
use_book = "flupe"
use_chapter = 8
use_word = 1
use_prompt = "kawaii_lines"


def do():
    words = all_words[use_book][use_chapter]
    print(f"book: {use_book}, chapter: {use_chapter}, words: {words}")

    if do_audio:
        for word in words:
            audio_generate(word)

    if do_image:
        word = words[use_word]
        print(f"image for word no: {use_word}, word: {word}")
        image_generate(word)


if __name__ == '__main__':
    do()
