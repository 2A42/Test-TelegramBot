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

def get_dad_joke():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        for p in data:
            return p['joke']
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error

def get_fact():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        for p in data:
            return p['fact']
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error

def get_quote():
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        for p in data:
            return '"' + p['quote'] + '"\n- ' + p['author']
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error

def get_mood(text):
    api_url = 'https://api.api-ninjas.com/v1/sentiment?text={}'.format(text)
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data['sentiment'] == 'NEGATIVE':
            return '\N{crying face}'
        elif data['sentiment'] == 'WEAK_NEGATIVE':
            return '\N{worried face}'
        elif data['sentiment'] == 'NEUTRAL':
            return '\N{thinking face}'
        elif data['sentiment'] == 'WEAK_POSITIVE':
            return '\N{slightly smiling face}'
        elif data['sentiment'] == 'POSITIVE':
            return '\N{grinning face with smiling eyes}'
        else:
            return '\N{turtle}'
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error

def get_rword():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        return data['word']
    else:
        error = "Error:" + str(response.status_code) + str(response.text)
        return error

def get_definition(word):
    api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': AI_API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data['valid'] == True:
            return word + ' - ' + data['definition']
        else:
            return None
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