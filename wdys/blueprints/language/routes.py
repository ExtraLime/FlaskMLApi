from flask import Blueprint, request, jsonify
from wdys.blueprints.language.models.ner import NER
from wdys.blueprints.language.models.sentiment import SA
from langdetect import detect

language = Blueprint('language', __name__, template_folder='templates')


@language.route('/')
def home():
    return 'API is Working'


@language.route('/ner', methods=['GET', 'POST'])
def get_ents():
    text = request.args.get('sentence')

    if detect(text) != 'en':
        return jsonify({'error': "This doesn't appear to be english"})
    elif not text or len(text) > 500:
        message = 'This sentence is either too short or too long'
        return jsonify({'error': message})

    model = NER()
    entities = model.get_ents(text)

    return jsonify(entities)


@language.route('/sentiment', methods=['GET', 'POST'])
def get_sentiment():
    text = request.args.get('sentence')

    if detect(text) != 'en':
        return jsonify({'error': "This doesn't appear to be english"})
    elif not text or len(text) > 500:
        message = 'This sentence is either too short or too long'
        return jsonify({'error': message})

    model = SA()
    sentiment = model.get_sentiment(text)

    return jsonify(sentiment)
