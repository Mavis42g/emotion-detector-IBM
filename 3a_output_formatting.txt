import json
import sys
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Sending the POST request
    response = requests.post(url, json=input_json, headers=headers)

    response_dict = json.loads(response.text)
    emotion_scores = response_dict["emotionPredictions"][0]["emotion"]
    result = {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
    }

    result["dominant_emotion"] = max(result, key=result.get)

    return (
        "{\n"
        f"'anger': {result['anger']},\n"
        f"'disgust': {result['disgust']},\n"
        f"'fear': {result['fear']},\n"
        f"'joy': {result['joy']},\n"
        f"'sadness': {result['sadness']},\n"
        f"'dominant_emotion': '{result['dominant_emotion']}'\n"
        "}"
    )

if __name__ == "__main__":
    text = sys.argv[1]
    result = emotion_detector(text)
    print(result)