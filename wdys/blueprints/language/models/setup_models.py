from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    AutoModelForSequenceClassification
)

# Declare default model for Entity Recognigtion
ner_model = "dbmdz/bert-large-cased-finetuned-conll03-english"
# Load Model and associtated tokenizer
tokenizer = AutoTokenizer.from_pretrained(ner_model)
model = AutoModelForTokenClassification.from_pretrained(ner_model)
# save models
model.save_pretrained('./entity')
tokenizer.save_pretrained('./entity')

# Declare default model for Sentiment Analysis
sent_model = 'distilbert-base-uncased-finetuned-sst-2-english'
# Load model for sentiment analysis
tokenizer = AutoTokenizer.from_pretrained(sent_model)
model = AutoModelForSequenceClassification.from_pretrained(sent_model)
# save models
model.save_pretrained('./sentiment')
tokenizer.save_pretrained('./sentiment')
