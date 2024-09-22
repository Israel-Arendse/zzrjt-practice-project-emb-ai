import requests # Import the requests library to handle HTTP requests
import json     # Import the json library

def sentiment_analyzer(text_to_analyse): # Define the function 'sentiment_analyzer' to take the string input (text_to_analyse)
    url ='https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL for the sentiment analysis service
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create the dictionary 'myobj' with the text to be analyzed under the variable 'text'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} # Set the headers required for the API request

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

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
