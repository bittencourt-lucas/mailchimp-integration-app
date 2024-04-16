import os
import pytest
from src.application.services.mockapi.get_contacts_service \
    import GetContactsService


@pytest.mark.asyncio
async def test_get_contacts_service(mocker):
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

    service = GetContactsService()
    contacts = await service.execute()

    mock_get.assert_called_once_with(
        f'{os.environ.get('MOCKAPI_BASE_URL')}/contacts',
        headers={'Content-Type': 'application/json'}
        )
    assert contacts == mock_response
