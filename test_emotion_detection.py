from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        test1 = emotion_detector("I am glad this happened")
        self.assertEqual(test1['dominant_emotion'], 'joy')

    def test_anger(self):
        test2 = emotion_detector("I am really mad about this")
        self.assertEqual(test2['dominant_emotion'], 'anger')

    def test_disgust(self):
        test3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test3['dominant_emotion'], 'disgust')

    def test_sadness(self):
        test4 = emotion_detector("I am so sad about this")
        self.assertEqual(test4['dominant_emotion'], 'sadness')

    def test_fear(self):
        test5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()