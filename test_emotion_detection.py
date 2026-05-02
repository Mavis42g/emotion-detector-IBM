import ast
import os
import sys
import unittest


ROOT_DIR = os.path.dirname(__file__)
PACKAGE_ROOT = os.path.join(ROOT_DIR, "final_project")
sys.path.insert(0, PACKAGE_ROOT)

from EmotionDetection.emotion_detection import emotion_detector


def parse_result(result):
	if isinstance(result, str):
		return ast.literal_eval(result)
	return result


class TestEmotionDetection(unittest.TestCase):
	def assert_dominant_emotion(self, text, expected):
		result = parse_result(emotion_detector(text))
		self.assertIn("dominant_emotion", result)
		self.assertEqual(result["dominant_emotion"], expected)

	def test_joy(self):
		self.assert_dominant_emotion("I am glad this happened", "joy")

	def test_anger(self):
		self.assert_dominant_emotion("I am really mad about this", "anger")

	def test_disgust(self):
		self.assert_dominant_emotion("I feel disgusted just hearing about this", "disgust")

	def test_sadness(self):
		self.assert_dominant_emotion("I am so sad about this", "sadness")

	def test_fear(self):
		self.assert_dominant_emotion("I am really afraid that this will happen", "fear")


if __name__ == "__main__":
	unittest.main()
