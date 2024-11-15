import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, headers=headers, json=input_json)
        data = response.json()  
        
        if response.status_code == 200 and 'emotionPredictions' in data:
            emotions = data['emotionPredictions'][0]['emotion']
            return emotions
        else:
            return f"Unexpected response structure: {data}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
