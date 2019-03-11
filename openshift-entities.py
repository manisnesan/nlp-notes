import jsonlines
import spacy, textacy
from typing import List
import re
import csv


def load_spacy_module():
    nlp = spacy.load('en_core_web_lg')
    return nlp

'''
Given a list of entities, this removes empty and duplicate entities 
and return a list with unique entities
'''
def remove_empty_duplicate_entities(entities):
    unique_list = []
    entity_text_list = set()
    for entity in entities: 
        if entity.text.strip() not in entity_text_list and len(entity.text.strip()) > 0:
            entity_text_list.add(entity.text.strip())
            unique_list.append(entity)
        
    return entity_text_list  

def load_data():
    data = []
    with jsonlines.open('openshift_docs_compact_sample100.jsonl') as reader:
        for item in reader:
            data.append(item)
    return data

def preprocess(sections) :
    '''
    Strips the numbers appearings before each section
    Example
    ['32.1. Overview', '32.2. Before You Begin'] => ['Overview', 'Before You Begin']
    '''
    return  [ ' '.join(x.split()[1:]) for x in sections]

def extract_entities(nlp, text: str) -> List[str]:    
    texts = nlp(text)
    text_entities = [ent for ent in textacy.extract.named_entities(
                            texts, 
                            exclude_types={'CARDINAL', 'TIME', 'GPE', 'MONEY', 'DATE', 'QUANTITY', 'PERCENT'})]

    unique_text_entities = remove_empty_duplicate_entities(text_entities)
    #print('Entities found :{}'.format(str(unique_text_entities)))
    return unique_text_entities

def run():
    
    # Load spacy model
    print('Loading spacy module ...')
    nlp = load_spacy_module()

    #Load data
    print('Loading the data')
    docs = load_data()

            
    #Extract entities from each doc's sections
    for data in docs:
        entities = []
        page_title = data['page_type_title'].split('.')[1].strip()
        doc_title = data['page_type_docTitle']
        sections = preprocess(data['section_titles'])
        #title_content = '{} {} {}'.format(doc_title, page_title, ' '.join(sections))
        for each in sections:
                entities.extend(extract_entities(nlp, each))

        entities = list(set(entities))
        print(f"uri : {data['uri']}")
        print(f"product : {data['product_type_name']}")
        print()      
        print(f"doc title : {data['page_type_docTitle']}")
        print(f"page title : {page_title}")

        print(f"intent/topic : {data['page_type_urlFragment'].replace('-', '_')}")
        if (len(entities) > 0):                
                print(f"entities: {entities}")              
        else:
                print(f"entities : NONE")
        
        print()
        print('===============================================')
        print()

run()

