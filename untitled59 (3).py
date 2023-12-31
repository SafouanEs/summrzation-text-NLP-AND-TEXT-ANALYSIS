# -*- coding: utf-8 -*-
"""Untitled59.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVuOI0IYblQgcrcYaIgG_wItG7chn84g
"""

pip install sentencepiece
import sentencepiece as spm
s = spm.SentencePieceProcessor(model_file='spm.model')

!pip install ibm-watson

!pip install streamlit ngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile streamlit_app.py
# 
# import streamlit as st
# from ibm_watson import NaturalLanguageUnderstandingV1 as NLU
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, SentimentOptions, EntitiesOptions, RelationsOptions
# from transformers import T5Tokenizer, T5ForConditionalGeneration
# 
# def initialize_watson_nlu(api_key, service_url):
#     authenticator = IAMAuthenticator(api_key)
#     nlu = NLU(version='2022-04-07', authenticator=authenticator)
#     nlu.set_service_url(service_url)
#     return nlu
# 
# def analyze_text(text, nlu_instance):
#     response = nlu_instance.analyze(
#         text=text,
#         features=Features(
#             keywords=KeywordsOptions(emotion=True, sentiment=True, limit=5),
#             sentiment=SentimentOptions(),
#             entities=EntitiesOptions(sentiment=True, limit=5),
#             relations=RelationsOptions()
#         )
#     ).get_result()
#     return response
# 
# def load_t5_model():
#     model = T5ForConditionalGeneration.from_pretrained('t5-base')
#     tokenizer = T5Tokenizer.from_pretrained('t5-base')
#     return model, tokenizer
# 
# def summarize_text(text, model, tokenizer, genre):
#     input_text = f"summarize: {text}"
#     input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
#     summary_ids = model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary
# 
# def main():
#     st.title('MSS_SUMMARIZATION TEXTS AND ANALYSIS')
# 
#     api_key = st.sidebar.text_input("Enter your IBM Watson NLU API Key", type="password")
#     service_url = st.sidebar.text_input("Enter your IBM Watson NLU Service URL")
# 
#     text = st.text_area("Enter the text you'd like to analyze:", height=200)
#     genre = st.selectbox("Choose the genre for summarization:", ["business", "entertainment", "politics", "sport", "technology"])
# 
#     if st.button('Analyze and Summarize Text'):
#         if api_key and service_url and text:
#             try:
#                 nlu_instance = initialize_watson_nlu(api_key, service_url)
#                 t5_model, t5_tokenizer = load_t5_model()
# 
#                 result = analyze_text(text, nlu_instance)
#                 summary = summarize_text(text, t5_model, t5_tokenizer, genre)
# 
#                 st.subheader('Summary')
#                 st.write(summary)
# 
#                 st.subheader('Analysis Results')
#                 sentiment = result.get('sentiment', {}).get('document', {})
#                 st.write(f"**Overall Sentiment**: {sentiment.get('label')} (score: {sentiment.get('score')})")
# 
#                 st.subheader('Keywords and their sentiment:')
#                 for keyword in result.get('keywords', []):
#                     st.write(f"- {keyword.get('text')}: Relevance {keyword.get('relevance')}, Sentiment {keyword.get('sentiment').get('label')} (score: {keyword.get('sentiment').get('score')})")
# 
#                 st.subheader('Entities and their sentiment:')
#                 for entity in result.get('entities', []):
#                     st.write(f"- {entity.get('type')} {entity.get('text')}: Relevance {entity.get('relevance')}, Sentiment {entity.get('sentiment').get('label')} (score: {entity.get('sentiment').get('score')})")
# 
# 
# 
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")
#         else:
#             st.error("Please provide all required inputs.")
# 
# if __name__ == "__main__":
#     main()
# 
#

!streamlit run streamlit_app.py &>/dev/null&

!pip install pyngrok

from pyngrok import ngrok

# Terminate open tunnels if exist
ngrok.kill()

# Setting the authtoken (replace 'your_auth_token' with the actual token you copied)
ngrok.set_auth_token("2a22fEw7uCdzM57A8hGi5WJkFp7_2xpuXPLCT83wVCrryaRf")

# Open a HTTP tunnel on the port 8501 (default port)
public_url = ngrok.connect(8501)  # Use an integer for the port number
public_url

ngrok.disconnect(public_url)