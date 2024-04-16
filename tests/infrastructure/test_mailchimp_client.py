import os
from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


def test_mailchimp_api_init(mocker):
    url = 'https://us1.api.mailchimp.com/3.0'
    api_key = 'test_key'

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_BASE_URL': url,
        'MAILCHIMP_API_KEY': api_key
        })

    client = MailchimpAPIClient()

    assert client.client.base_url == url
    assert client.client.client.headers == {
        'Authorization': f'Bearer {os.getenv('MAILCHIMP_API_KEY')}',
        }
    assert client.client.client.url == url
