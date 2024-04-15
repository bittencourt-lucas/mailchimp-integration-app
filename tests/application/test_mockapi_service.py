import os
import pytest
from src.application.services.mockapi_service import MockAPIService


def test_format_contacts():
    service = MockAPIService()
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

    output = service.format_contacts(contacts)
    assert output == expected_output


@pytest.mark.asyncio
async def test_mockapi_service_get_contacts(mocker):
    mock_response = [{
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'johndoe@outlook.com'
        }]

    mock_get = mocker.patch('httpx.AsyncClient.get')
    mock_get.return_value = mocker.Mock(status_code=200)
    mock_get.return_value.json.return_value = mock_response

    mocker.patch.dict(os.environ, {
        'MOCKAPI_BASE_URL': 'https://challenge.trio.dev/api/v1'
        })

    service = MockAPIService()
    contacts = await service.get_contacts()

    mock_get.assert_called_once_with(
        f"{os.environ.get('MOCKAPI_BASE_URL')}/contacts"
        )
    assert contacts == mock_response
