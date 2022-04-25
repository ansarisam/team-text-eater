from transformers import pipeline

summarizer = pipeline('summarization')

def summarize(para,max_len,min_len):
  temp = summarizer(para, max_length=max_len, min_length=min_len)
  return(temp[0]['summary_text'])