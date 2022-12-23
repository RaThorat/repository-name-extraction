# Trying to find repository name in a text

import spacy
import pandas as pd
from spacy import displacy

nlp =spacy.load('your_NLP_model')

def has_SURFsara_token(doc):
    for t in doc:
        if t.lower_ in ['SURFsara', 'DRYAD']:
            if t.pos_ != 'VERB':
                return True
    return False

 doc=nlp('I like to save my data in Odum Institute Archive Dataverse')

# Using pattern match for finding repositories in text
has_SURFsara_token(doc)
pattern = [{'ORTH': 'Odum Institute Archive Dataverse'}]
#pattern = [{'ORTH': 'SURF', 'LOWER': 'sara'}]

from spacy.matcher import Matcher
matcher=Matcher(nlp.vocab)
matcher.add("Odum", None, pattern)
matcher(doc)

# using PDF2 and NLP model
df_PA4= pd.DataFrame(columns = ['Grant No.','Entities', 'Labels'])
files_path= 'your path'
read_files=glob.glob(os.path.join(files_path,"*.pdf")) 
#i=1
for files in read_files:
    doc=fitz.open(files)
    #if the filename is clear and distinct
    from pathlib import Path
    base = os.path.basename(files)
    filename=Path(base).stem
    #if the filename is not the official name  of the application
    #filename="DMP_"+str(i)
    text=""
    for page in doc:
        text=text +str(page.getText())
    tx="  ".join(text.split('\n'))
    #Load SpaCy Model
    docs=repo_model(tx)
    entities = []
    labels = []
    for ent in docs.ents:
        entities.append(ent)
        labels.append(ent.label_)
    df = pd.DataFrame({'Grant No.':filename,'Entities':entities,'Labels':labels})
    #df=df.drop_duplicates(subset=['Entities'])
    df = df.astype('str')
    df.drop_duplicates(subset=['Entities','Labels'], keep="first", inplace=True)
    #for filname in df['Grant No.']:
        #new_row={'Grant No.':filename, 'Entities':entities,'Labels':labels}
        #df_PA4 = df_PA4.append(new_row, ignore_index=True)
    df_PA4 = df_PA4.append(df, ignore_index=True)
    
    #i=i+1
df_PA4.head()

table = df_PA4.pivot_table(index=['Grant No.'],
                             columns=['Labels'],
                             values=['Entities'],
                             aggfunc=lambda x: ', '.join(str(v) for v in x))
table.head()
table.to_excel('DMP_info.xlsx')
