import json 
import requests 
def emotion_detector(text_to_analyse):    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    json_obj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = json_obj, headers = header)
    status_code = response.status_code
    json_formatted_response = json.loads(response.text)
    
    if text_to_analyse:
        anger = json_formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = json_formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = json_formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = json_formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = json_formatted_response['emotionPredictions'][0]['emotion']['sadness']

        json_build = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness}

        sorted_emotion_value = dict(sorted(json_build.items(), key=lambda obj: obj[1], reverse=True))
        json_build['dominant_emotion']= list(sorted_emotion_value.keys())[0]
        return json_build

    elif status_code == 400:
        json_build = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
        return json_build
    