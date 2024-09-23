''' Executing this code activates the sentiment_analyer code
    and imports the JSON library and the third-party library 
    requests.
'''

import json      # Import the JSON library
import requests  # Import the requests library to handle HTTP requests

# Define the function 'sentiment_analyzer' to take the string input (text_to_analyse)
def sentiment_analyzer(text_to_analyse):
    '''
    Analyzes the text input and return the dictionary
    with the status code 200. If an error is encountered
    then the response status code return is 500.

    Parameters:
     'label' (key-value): The type of sentiment detected.
     'score' (key-value): The score rating for the sentiment.

    Returns:
     dictionary: The type of sentiment in the text and its score.
    '''
    # Define URL for the sentiment analysis service
    url ='https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Send a POST request to the API with the text and headers
    try:
        response = requests.post(url, json = myobj, headers=header, timeout=5)
    except requests.exceptions.Timeout:
        # End  connection and retry
        print("Request timed out!")
    # Parse the JSON response
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # Return turn a dictionary with label and score
    return {'label': label, 'score': score}
