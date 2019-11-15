This is my attempt to dive into NLP which I have been trying to get my feet wet. The notebooks can be found in *nbs* directory.

[1] NLP Introduction to Python using spacy and textacy - The notebook is heavily inspired from the book by NLP in Python: Quick Start Guide by [Nirant Kasliwal](https://nirantk.com/)

[2] Entity Extraction from [OpenShift Product Documentation](https://access.redhat.com/documentation/en-us/openshift_container_platform) - openshift-entities.py - This python scripts reads the file `openshift_docs_compact_sample100.jsonl` and uses spacy and textacy to extract the entities and writes them to `openshift_docs_compact_sample100.out`

[3] Product Named Entity Recognition(NER) - This notebook uses Spacy's Phrase Matcher Component to bootstrap custom domain specific product entity recognition and also shows how to add custom extension attributes to the entity.

[4] Advanced NLP with Spacy contains notebooks created based on Ines Montani [Spacy Course](https://course.spacy.io/).  

[5] Keyword Phrase Extraction illustrated using OpenShift 4 titles. This notebook uses graph based single rank method(unsupervised) to extract the keyphrases found in OpenShift knowledge base titles. 

[6] IMDB Reviews - Sentiment Classification using [fastai](https://docs.fast.ai/). This notebook uses pretrained language model wikitext103 in order to perform sentiment classification on IMDB Reviews data set. 
