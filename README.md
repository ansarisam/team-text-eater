# Team-Text-Eater

This repository represents Team Text Eater's summarization problem: To summarize the returned list of paragraphs from the module ,getParagraphs function is  developed by Team Paralegal. This repository consists of functions that will be used for the transformation  of the paragraph to summary, these include finding an optimal maximum and minimum token length of the summary based on the original paragraph.   


The flow of the final integrated function getSummarization(), begins with calling the getParagraphs() function in module Paragraph which is developed by team Paralegal, this function returns a list of paragraphs in structure of nested JSON dictionaries. Then these paragraphs are looped through multiple functions:first, the paragraphs are pre-processed to check for any illegal characters, then tokenized to find the optimal limits based on the paragraph's original length, which will be eventually used in the Hugging Face Library's BERT summarizer pipeline, which is a pre-trained encode-decoder transformer model that will summarize the paragraphs.Then passed to the getNER method from the Gryffindor team's getNER module, which returns a list of two dictionaries containing entities and relations within the paragraph. Finally, this function provides a nested list of JSON Dictionaries containing the paragraph Id, Document Id, paragraph, Topic, Summary, Entities, Relations, and the time taken to finish the loop for each paragraph.

Sample test Script for implementation:

from team-text-eater import getSummarization

getSummarization('Path-to-Text_Document')
