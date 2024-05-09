import openai
import Text_to_Speech
import cv2
import pytesseract
def summ():
    openai.api_key = ""

    Text_to_Speech.spk("Capturing")
    cam = cv2.VideoCapture(0)
    _, frame = cam.read()
    #img = cv2.imread(frame)
    img = frame
    # Adding custom options
    '''custom_config = r'--oem 3 --psm 6'
    x = pytesseract.image_to_string(img, config=custom_config)'''

    #custom_config = r'--oem 3 --psm 6'
    x = pytesseract.image_to_string(img)

    #text = "This tutorial uses distinct functions for each task we want GPT-4 to perform. This is not the most efficient way to do this task - you can put these instructions into one function, however, splitting them up can lead to higher quality summarization."
    response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=(f"Summarize the following text:\n{x}\n\nSummary:"),
                temperature=0.5,
                max_tokens=1024,
                n = 1,
                stop=None
            )
    summary = response.choices[0].text.strip()
    Text_to_Speech.spk(summary)
    print(summary)









'''
from openai import OpenAI

def abstract_summary_extraction(transcription, client):
    response = client.chat.completions.create(
        model="gpt-3",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    print(response.choices[0].message.content)
def summ():
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="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",
    )
    abstract_summary_extraction(r"This tutorial uses distinct functions for each task we want GPT-4 to perform. This is not the most efficient way to do this task - you can put these instructions into one function, however, splitting them up can lead to higher quality summarization.", client)
summ()

'''
'''





import requests
def summ():
    url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer-text"

    payload = {
        "text": "Automatic summarization is the process of reducing a text document with a computer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is another.",
        "sentnum": "5"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2a4338b497msha5f35b0d24e324fp18917bjsned120d806d14",
        "X-RapidAPI-Host": "textanalysis-text-summarization.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())

















'''







'''import requests

url = "https://api.edenai.run/v2/text/summarize"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "output_sentences": 1
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA4Y2YzMTktMjliZC00MmY2LTk5MmItZDcxODNiMTM5MWU4IiwidHlwZSI6ImFwaV90b2tlbiJ9.m7Eqpf39_1J_rC7zPAoZcnSlwX8Sv027yA_APTEJVwA"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)'''
