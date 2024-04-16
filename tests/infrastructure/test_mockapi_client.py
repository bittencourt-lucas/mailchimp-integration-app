import os
import pytest
from src.infrastructure.externals.mockapi_client import MockAPIClient


def test_mockapi_client_init(mocker):
    url = 'https://challenge.trio.dev/api/v1'
    mocker.patch.dict(os.environ, {
        'MOCKAPI_BASE_URL': url
        })

    service = MockAPIClient()

    assert service.base_url == url
    assert service.client.url == url
    assert service.client.headers == {'Content-Type': 'application/json'}


def test_mockapi_client_missing_base_url(mocker):
    mocker.patch.dict(os.environ, {
        'MOCKAPI_BASE_URL': ''
    })

    with pytest.raises(ValueError):
        MockAPIClient()


def test_format_contacts(mocker):
    url = 'https://challenge.trio.dev/api/v1'
    contacts = [{
        'createdAt': '2022-02-18T16:32:23.057Z',
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'johndoe@outlook.com',
        'avatar': 'https://cdn.fakercloud.com/avatars/dshster_128.jpg',
        'id': '115'
    }]
    expected_output = [{
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'johndoe@outlook.com'
    }]

    mocker.patch.dict(os.environ, {
        'MOCKAPI_BASE_URL': url
        })

    service = MockAPIClient()
    output = service.format_contacts(contacts)

    assert output == expected_output
