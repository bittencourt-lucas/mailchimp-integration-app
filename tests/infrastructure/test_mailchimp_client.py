import os
import pytest
from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


def test_mailchimp_api_init(mocker):
    url = 'https://us1.api.mailchimp.com/3.0'
    api_key = 'test_key'

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_BASE_URL': url,
        'MAILCHIMP_API_KEY': api_key
        })

    client = MailchimpAPIClient()

    assert client.base_url == url
    assert client.client.headers == {
        'Authorization': f'Bearer {os.getenv('MAILCHIMP_API_KEY')}',
        'Content-Type': 'application/json',
        }
    assert client.client.url == url


def test_mailchimp_api_missing_base_url(mocker):
    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_BASE_URL': '',
        'MAILCHIMP_API_KEY': 'test_key'
        })

    with pytest.raises(ValueError):
        MailchimpAPIClient()


def test_mailchimp_api_missing_api_key(mocker):
    mocker.patch.dict(os.environ, {
        'MAILCHIMP_BASE_URL': 'https://us1.api.mailchimp.com/3.0',
        'MAILCHIMP_API_KEY': ''
        })

    with pytest.raises(ValueError):
        MailchimpAPIClient()
