# loading model from file system 
import json
import numpy as np
from flask import Flask, request, redirect, url_for, flash, jsonify

# BERTSUM
from summarizer import Summarizer

# Extract full text from URL
from newspaper import fulltext
import requests

# Validate URL
import validators


# Creates the server that takes requests and returns output 
app = Flask(__name__)


def summarizer(original_text, max_ratio):
    """
    Summarizes the original text by using BERT extractive summarizer.
    IN: original text (string)
    OUT: summary (string)
    """
    print('Original text: ', original_text)
    print("------------------------------------------------------------------------------------------------------")
    model = Summarizer()
    if max_ratio == 0:
        result = model(original_text)
    else:
        max_ratio = max_ratio/100
        result = model(original_text, ratio=max_ratio)
    
    #result = model(original_text)
    summary = "".join(result)
    print("------------------------------------------------------------------------------------------------------")
    print("BERTsum summary: ", summary)
    print("-------------------------------------------------------------------------------------------------------")
    
    return summary

def read_file(uploaded_file):
    """
    Reads the file from its format and produces the text in string format.
    IN: file (<_io.BufferedReader name='file_name.txt'>)
    OUT: full text (string)
    """
    file_read = uploaded_file.read()
    input_text = file_read.decode('utf-8') # replace("\n", "")
    
    return input_text

# Different methods:
# GET: Retrieves a resource
# POST: Creates a resource
# PUT: Updates or creates within an existing resource
# PATCH: Partially modifies an existing resource
# DELETE: Removes the resource

# "/summarize/text" will be used after the IP for api calls (ex: http://128.0.0.1/summarize).
@app.route('/summarize', methods=['POST'])
def summarize_text():
    """
    Summarizes text which is entered in the text field.
    IN: -
    OUT: summary (json)
    """
    # does the same check as the if statement. If ‘data’ is present in the query parameters, its value is stored in data. 
    # is True if ‘data’ was present in the query parameters, and False if not.   
    
    input_text = request.args.get("data")

    max_ratio = request.args.get("ratio")    
    if max_ratio == '':
        max_ratio = int(0)
    else:
        max_ratio = int(max_ratio)
        
    summary = summarizer(input_text, max_ratio)

    return jsonify(summary) 

@app.route("/summarize_file", methods=["POST"]) 
def summarize_file():
    """
    Summarizes text which is entered as a file.
    IN: -
    OUT: summary (json)
    """    
    uploaded_file = request.files['file'] # 'file': <_io.BufferedReader name='file_name.txt'>
    input_text = read_file(uploaded_file)

    max_ratio = request.args.get('ratio')
    if max_ratio == '':
        max_ratio = int(0)
    else:
        max_ratio = int(max_ratio)
    
    summary = summarizer(input_text, max_ratio)
    
    return jsonify(summary)

@app.route('/summarize_url', methods=['POST'])
def summarize_url():
    """
    Summarizes text which is entered from a URL.
    IN: -
    OUT: summary (json)
    """    
    input_url = request.args.get("data")
    input_text = fulltext(requests.get(input_url).text)
    
    max_ratio = request.args.get("ratio")
    
    if max_ratio == '':
        max_ratio = int(0)
    else:
        max_ratio = int(max_ratio)
        
    summary = summarizer(input_text, max_ratio)
    
    return jsonify(summary)
    
if __name__ == '__main__':
    # debug=True — restarts the application automatically when it encounters any change in the code
    # host=’0.0.0.0' — makes the web service public
    # port=5000 — the port that we use to access the application
    app.run(port=5000, debug=True)