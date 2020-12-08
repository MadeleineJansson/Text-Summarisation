# Text-Summarisation
BERTsum applied for extractive text summarisation. Endpoint created with Flask.

# text_summarisers

Bidirectional Encoder Representations from Transformers, is designed as a deeply 
bidirectional model. The network effectively captures information from both the 
right and left context of a token from the first layer itself and all the way 
through to the last layer. BERT is based on the Transformer architecture and is 
pre-trained on a large corpus of unlabelled text including the entire Wikipedia 
(that is 2,500 million words) and Book Corpus (800 million words). 

BERTsum, which is used in this repo, is a fine-tuned version where transfer 
learning has been adopted in order to tweek the model to perform extractive text 
summarisation on documents. 

# Installations required:
- pip install pytorch
- pip install bert-extractive-summarizer
- pip install newspaper3k
- pip install Flask
- pip install ipywidgets
- pip install rouge-metric
- pip install summa

# Files
- final_summarizer.ipynb and summary.PNG for visualising the model using iPyWidgets
- text_api.py and text_summarizer.py are files for creating an endpoint with Flask
