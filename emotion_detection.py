import sys

from final_project.EmotionDetection.emotion_detection import emotion_detector, format_emotion_output


if __name__ == "__main__":
    text = sys.argv[1]
    result = emotion_detector(text)
    print(format_emotion_output(result))
