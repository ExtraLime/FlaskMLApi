import requests
from flask import url_for


class TestRoute(object):
    def test_root_route(self, client):
        """ Home page should respond with 200"""
        response = client.get(url_for('language.home'))
        assert response.status_code == 200

    def test_langauge_id(self, client):
        """Non English Sentences should return a json with an error key"""
        # Non English Sentence
        not_english = 'Cela est un phrase en francais'
        # build body for post
        body = [('sentence', not_english)]

        # get response from endpoints
        entity_response = requests.post(
            url_for('language.get_ents'), params=body)
        sentiment_response = requests.post(
            url_for('language.get_sentiment'), params=body)

        # get json
        ent_res = entity_response.json()
        sent_res = sentiment_response.json()

        # get status codes
        ent_code = entity_response.status_code == 200
        sent_code = sentiment_response.status_code == 200
        # ensure responses are 200
        assert all([ent_code, sent_code])

        # confirm proper error
        assert ent_res['error'] == "This doesn't appear to be english"
        assert sent_res['error'] == "This doesn't appear to be english"

    def test_length(self, client):
        test_string = 'C'*501
        body = [('sentence', test_string)]
        response = requests.post(url_for('language.get_ents'), params=body)
        res = response.json()

        assert response.status_code == 200
        assert res['error'] == 'This sentence is either too short or too long'
