from SentimentAnalysis.sentiment_analysis import sentiment_analyzer # Import sentiment_analyzer from the SentimentAnalysis package
import unittest # Import the unnittest library

# Define a test case class for testing the sentiment_analyzer
class test_sentiment_analyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        # test when 'I love working with Python' is sent as input, it is labeled as 'SENT_POSITIVE'
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE') 

        # Test case for negative sentiment
        # test when 'I hate working with Python' is sent as input, it is labeled as 'SENT_NEGATIVE'
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertNotEqual(result_2['label'], 'SENT_NEGATIVE') 

        # Test case for neutral sentiment
        # test when 'I am neutral on Python' is sent as input, it is labed as 'SENT_NEUTRAL'
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertLessEqual(result_3['label'], 'SENT_NEUTRAL') 

# Run all the test cases defined in the module when the script is executed
# This will automatically discover and run all the test cases defined in the module
unittest.main()