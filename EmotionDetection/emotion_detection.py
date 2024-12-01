import requests  # Import requests to handle HTTP requests
import json  # Import json to parse JSON data

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload  = { "raw_document": { "text": text_to_analyse } }

    try:
        # Send POST request to Watson API
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP response codes 4xx or 5xx

        response_data = response.json()
        
        # Extract emotions and their scores
        emotions = response_data['emotionPredictions'][0]['emotion']
       # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Format the output
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return result
    except requests.exceptions.RequestException as e:
        # Handle network errors or HTTP response issues
        return {"error": str(e)}