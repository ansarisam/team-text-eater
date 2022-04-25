
import string

def pre_process(para):
  result = para.translate(string.punctuation)
  return(result)