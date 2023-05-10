import requests
import shutil
import json

from config import AI_API_KEY #custom info

def get_joke():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        for p in data:
            return p['joke']
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error

def get_image():
    api_url = 'https://api.api-ninjas.com/v1/randomimage'
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY, 'Accept': 'image/jpg'}, stream=True)
    if response.status_code == requests.codes.ok:
        with open('img.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error

def get_image_info(image):
    api_url = 'https://api.api-ninjas.com/v1/objectdetection'
    files = {'image': image}
    response = requests.post(api_url, headers={'X-Api-Key': AI_API_KEY}, files=files)
    if response.status_code == requests.codes.ok:
        data = response.json()
        result = ""
        for p in data:
            result = result + "It's " + p['label'] + " with " + str(int(float(p['confidence']) * 100)) + "% of confidence\n"
        return result
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error