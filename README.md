# Team-Text-Eater

This repository represents Team Text Eater's to the summarization problem: to summarize the returned list of paragraphs from the module getParagraphs developed by Team Paralegal. This repository consists of functions that will each be used the transformation of the paragraph to summary, these include finding an optimal maximum and minimum token length of the summary based on the original paragraph.   

The flow of the final integrated function getSummarization, begins with calling the getParagraphs function in module Paragraph developed by team Paralegal, this function returns a list of paragraphs in structure of nested JSON dictionaries. Then these paragraphs are looped through multiple functions, initially it pre-processed to check for any illegal characters, then is tokenized for finding the optimal limits for the based on the original length of the paragraph that will be eventually used in the BERT summarizer pipeline from Hugging Face Library, which is a pre-trained encode-decoder tranformer model that will summarizze the paragraph.Then passed through the fuction getNER from getNER module developeed by team Gryfinndor, which return a two list of dictionaries that consists of entities and relations within the paragraph.At the end, this fuction returns a nested list of JSON Dictionaries that contains Paragraph Id, Document Id, Paragraph, Topic, Summary, Entities, Relations and the time taken for each paragraph for complete the loop.

Sample test Script for implementation:

from team-text-eater import getSummarization

getSummarization('Path-to-Text_Document')
