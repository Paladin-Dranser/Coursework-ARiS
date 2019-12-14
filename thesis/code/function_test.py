import pytest
import requests
import re

BASE_URL = 'http://flask-coursework-1560154162.eu-central-1.elb.amazonaws.com/'
# Check response code
@pytest.mark.parametrize("url, response_code", [
        (BASE_URL, 200),
        ('{}contact'.format(BASE_URL), 200),
        ('{}registration'.format(BASE_URL), 200),
        ('{}readers'.format(BASE_URL), 200),
        ('{}search'.format(BASE_URL), 400) # it is used only with parameters (so we get error 400)
    ])
def test_available(url, response_code):
    real_code = requests.get(url=url).status_code
    assert real_code == response_code , \
        'You website does not work (response code for {url} == {code})! \
        Real response code = {real_code}'.format(url=url, code=response_code, real_code=real_code)

# Test search by author
@pytest.mark.parametrize("search_words, radio_button", [
        ('Nabokov', 'author'),
        ('Ring', 'book')
    ])
def test_search(search_words, radio_button):
    params = {'search_words': search_words, 'radio_button': radio_button}
    response = requests.get(url='{}search'.format(BASE_URL), params=params)

    assert re.search(search_words, response.text, re.IGNORECASE), \
        'Search does not work ({type} {words} is not found)!'.format(type=radio_button,
                                                                     words=search_words)

# Test we shouldn't sign up if username is exist
def test_registration():
    data = {'username': 'Iwant10', 'password': '123', 'registration': ''}
    response = requests.post(url='{}registration'.format(BASE_URL),
        data=data)

    assert re.search('Try again', response.text, re.IGNORECASE), \
        'You register a new user, but the username is existed!'
