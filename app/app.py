import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization")
qa_model = pipeline("question-answering")

st.title("AI Research Assistant")

text = st.text_area("Enter text")

if st.button("Summarize"):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    st.write(summary[0]['summary_text'])

question = st.text_input("Ask question")

if st.button("Get Answer"):
    answer = qa_model(question=question, context=text)
    st.write(answer['answer'])
