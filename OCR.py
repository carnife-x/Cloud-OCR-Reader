import os
import json
import requests

API_KEY = '7932418f651547e7bd2caa731c339290'
ENDPOINT = 'https://iit-ocr.cognitiveservices.azure.com/vision/v3.1/ocr'
DIR = os.getcwd()

#used to extract text from results
def parse_text(results):
    text = ''
    for region in results['regions']:
        for line in region['lines']:
            for word in line['words']:
                text += word['text'] + ' '
            text += '\n'
    return text
#this function calls the Azure Api to process the image and extract information from it
def get_text(pathToImage):
    pathToImage=pathToImage[9:]  
    print('Processing: ' + pathToImage)
    headers  = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params   = {
        'language': 'en',
        'detectOrientation ': 'true'
    }
    payload = open(pathToImage, 'rb').read()
    response = requests.post(ENDPOINT, headers=headers, params=params, data=payload)
    results = json.loads(response.content)
    return results

#merges the parse_text and get_text to extract the relavant details
def handler(filename):
    text = ''
    if filename.endswith((".jpg",".png",".jpeg","jfif")): 
        pathToImage = '{0}/{1}'.format(DIR, filename)
        results = get_text(pathToImage)
        text += parse_text(results)
        data=text.splitlines()
        name=data[1]
        DOB=data[3]
        pan=data[5]
        if len(data)>8:
            name=data[5]
            DOB=data[8]
            pan=data[3]

    return name,DOB,pan



if __name__ == '__main__':
    None
    

