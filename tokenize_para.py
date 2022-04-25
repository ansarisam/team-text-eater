import nltk

def tokenize_para(para):
   token_len,max_len,min_len = 0,0,0
   token_len = len(nltk.word_tokenize(para))
   if token_len>=60:
    max_len = int(33/100*(token_len))
    min_len = int(2/10*(token_len))
   elif token_len<60 and token_len>25:
    max_len = int(1/2*(token_len))
    min_len = int(4/10*(token_len))
   elif token_len<=25:
    max_len = token_len
    min_len = token_len
   return(max_len,min_len)