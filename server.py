''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the flask app
app = Flask("Sentiment Analyzer")

# Defines a function with two purposes
# 1: Sends a GET request to the HTML interface to receive the input text
# 2: Calls the 'sentiment_analyzer' application with 'text_to_analyze' as an argument
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The code uses an 'if' and 'elif' function to check
        if the input is valid. The output returned shows the label and 
        its confidence score for the provided text. If the input is invalid 
        then the output returns the message 'Invalid input! Try again.'
    '''
    # Retrieve the text to analyze from the requests arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_anaylzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

     # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    
    else:
         # Return a formmatted string with the sentiment label and score
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")
def render_index_page():  # Runs the 'render_template' function in the 'index.html' HTML template
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html") 

# Runs the Flask app
if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000) # Hosts the app on the port:5000