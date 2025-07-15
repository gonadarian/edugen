import os
import json

import requests
import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_KEY")
token = os.getenv("GOOGLE_TOKEN")
project = "gonadarian"
url = "https://texttospeech.googleapis.com/v1/text:synthesize"
mock = False


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


def get_speech_mock():
    return {
        "audioContent": "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"
    }


def audio_generate(text):
    file = text
    if mock:
        speech = get_speech_mock()
    else:
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

    prompt = f"A {term}. Simple drawing, few pastel colors. In kawaii style."

    # prompt = f"A {term} in kawaii style using pastel colors."

    # prompt = f"A {term}. Simple drawing, few pastel colors. In duolingo style."

    # prompt = f"Create an image of a {term}, illustrated in a simple and cute manner, using few pastel colors. " \
    #          f"Incorporate a common style often seen in cute and endearing styles of animation, characterized " \
    #          f"by large, expressive eyes and rounded shapes. The colors used should be calming, soft, and muted, " \
    #          f"reminiscent of the hues commonly found in pastel art pieces."

    # prompt = f"Create an image of a {term}, in Kawaii style. Don't draw anything around the image. " \
    #          f"Don't draw too big eyes. Use pastel colors."

    # prompt = f"Create an image of a {term}, in Kawaii style, but without the eyes. " \
    #          f"Don't draw anything around the image.  Use pastel colors"

    # za rebuse
    # prompt = f"Create a simple image, as a drawing with few pastel colors. Draw a {term} with white background."

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


do_words = True
do_images = not do_words

if __name__ == '__main__':
    words = [
        "bow|baʊ",
        "bow|boʊ",
        "bow",
    ]

    if do_words:
        for word in words:
            audio_generate(word)

    if do_images:
        for word in words:
            image_generate(word)
