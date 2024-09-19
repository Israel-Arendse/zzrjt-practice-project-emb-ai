import requests # Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyse): # Define the function 'sentiment_analyzer' to take the string input (text_to_analyse)
    url ='https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL for the sentiment analysis service
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create the dictionary 'myobj' with the text to be analyzed under the variable 'text'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers
    return response.text # Return the response text from the API