import os
import requests
import PyPDF2

api_key = os.environ['voice_api_key']

with open('read_me_please.pdf', 'rb') as file:
    fileReader = PyPDF2.PdfFileReader(file)
    page = fileReader.getPage(0)
    page_content = page.extractText()



params = {
    "key": api_key,
    "src": page_content,
    "c": "mp3",
    "v": 'Linda',
    "hl": "en-us",
    "b64": True
}

#response = requests.get(url="http://api.voicerss.org/", params=params)

response = requests.get(url=f"http://api.voicerss.org/?key={api_key}&hl=en-us&v=Amy&src={page_content}")

with open("audio2.mp3","ab") as audiofile:
    audiofile.write(response.content)