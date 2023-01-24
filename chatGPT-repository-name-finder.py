# Trying to find repository name in a text

import spacy
import pandas as pd
import os
import glob
from spacy import displacy
import fitz
from pathlib import Path

nlp = spacy.load('en_core_web_sm')
doc = nlp('I like to save my data in Odum Institute Archive Dataverse')

# Using pattern match for finding repositories in text

pattern = [{'ORTH': 'Odum Institute Archive Dataverse'}]

from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
matcher.add("Odum", None, pattern)
matcher(doc)

# using PDF2 and NLP model
df_PA4 = pd.DataFrame(columns = ['Grant No.','Entities', 'Labels'])
files_path = 'your path'
read_files = glob.glob(os.path.join(files_path,"*.pdf")) 

for files in read_files:
    doc = fitz.open(files).pages
    #if the filename is clear and distinct
    base = os.path.basename(files)
    filename = Path(base).stem
    #if the filename is not the official name  of the application
    #filename="DMP_"+str(i)
    text = ""
    for page in doc:
        text = text + str(page.getText())
    tx = "  ".join(text.split('\n'))
    #Load SpaCy Model
    docs = nlp(tx)
    entities = []
    labels = []
    for ent in docs.ents:
        entities.append(ent)
        labels.append(ent.label_)
    df = pd.DataFrame({'Grant No.':filename,'Entities':entities,'Labels':labels})
    #df=df.drop_duplicates(subset=['Entities'])
    df = df.astype('str')
    df.drop_duplicates(subset=['Entities','Labels'], keep="first", inplace=True)
    df_PA4 = df_PA4.append(df, ignore_index=True)

df_PA4.head()

# Making pivot table of the dataframe
table = df_PA4.pivot_table(index=['Grant No.'],
                             columns=['Labels'],
                             values=['Entities'],
                             aggfunc=lambda x: ', '.join(str(v) for v in x))
table.head()
#Exporting the table as an excel file
table.to_excel('DMP_info.xlsx')
