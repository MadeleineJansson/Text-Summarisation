import requests
import json
import base64

print("Select Summarization Test Type:")
print("        Type 1 for text summarization: 1")
print("        Type 2 for file summarization: 2")
print("        Type 3 for url summarization: 3")
var = input("Please enter selected type: ")

############ Check for text ############
if  var == "1":
    url = 'http://127.0.0.1:5000/summarize'
    ### Adding new
    #print("Please enter in percentage the ratio wanted for the summary (0-100): ")
    print()
    max_ratio = input("Please enter in percentage the max ratio wanted for the summary (0-100): ")
    
    params = {'data': 'Text summarization is a way to condense the large amount of information into a concise form by the process of selection of important information and discarding unimportant and redundant information. With the amount of textual information present in the world wide web the area of text summarization is becoming very important. The extractive summarization is the one where the exact sentences present in the document are used as summaries. The extractive summarization is simpler and is the general practice among the automatic text summarization researchers at the present time. Extractive summarization process involves giving scores to sentences using some method and then using the sentences that achieve highest scores as summaries. As the exact sentence present in the document is used the semantic factor can be ignored which results in generation of less calculation intensive summarization procedure. This kind of summary is generally completely unsupervised and language independent too. Although this kind of summary does its job in conveying the essential information it may not be necessarily smooth or fluent. Sometimes there can be almost no connection between adjacent sentences in the summary resulting in the text lacking in readability.', 'ratio': max_ratio}
    print("-------------------------------------------------------------------------------------------------")
    print('Summarizing')
    r = requests.post(url, params=params)

    print("-------------------------------------------------------------------------------------------------")
    print(r)
    print("Summary: ", r.text)

############ Check for file ############
elif var == "2":
    url = 'http://127.0.0.1:5000/summarize_file'
    print()
    max_ratio = input("Please enter in percentage the max ratio wanted for the summary (0-100): ")
    files = {'file': open('corona.txt', 'rb')}
    params = {'ratio': max_ratio}
    print("-------------------------------------------------------------------------------------------------")
    print('Summarizing File...')
    r = requests.post(url, files=files, params=params)
    print("-------------------------------------------------------------------------------------------------")
    print(r)
    print("Summary: ", r.text)

############ Check for url ############
elif var == "3":
    url = 'http://127.0.0.1:5000/summarize_url'
    
    print()
    max_ratio = input("Please enter in percentage the max ratio wanted for the summary (0-100): ")
    
    params = {'data': 'https://www.nytimes.com/2020/12/02/opinion/facebook-twitter-misinformation.html?action=click&module=Opinion&pgtype=Homepage', 'ratio': max_ratio}
    print("-------------------------------------------------------------------------------------------------")
    print('Summarizing File...')
    r = requests.post(url, params=params)
    print("-------------------------------------------------------------------------------------------------")
    print(r)
    print("Summary: ", r.text)

else:
    print()
    print('Please enter a valid choice.')

    
    