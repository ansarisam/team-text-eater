from capstone_team_text_eater.pre_process import pre_process
from capstone_team_text_eater.tokenize_para import tokenize_para
from capstone_team_text_eater.summarize import summarize
from gryffindorner.getNER import getNER
from team_paralegal_main.ParagraphAssociatedLabel import Paragraph
import json
para_obj = Paragraph()


def getSummarization(path): 
    
      para_list = para_obj.getParagraphs(path)
      fout = open("C:/Masters/SPRING 2022/DEAN 690/output.txt", 'w', encoding='utf-8')
      for i in range(0,len(para_list)):
          para = para_list[i]['paragraphs'][0]['text']
          para = pre_process(para)
          max_len,min_len = tokenize_para(para)
          summary = summarize(para,max_len,min_len)
          ents, rels = getNER(para, 0.45)
          fdict = {'DocId':para_list[i]['docId'],'Pid':para_list[i]['paragraphs'][0]['pid'],'Topic':para_list[i]['paragraphs'][0]['topic'],'paragraph': para,'Summary':summary,'Entities':ents,'Relations':rels}
          json.dump(fdict, fout)
          fout.write("\n\n")

