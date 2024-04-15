
import pytest
from src.application.services.mockapi_service import MockAPIService


@pytest.mark.asyncio
async def test_mockapi_service_get_contacts(mocker):
    mock_response = {
        'status_code': 200,
        'data': [{
            'name': 'John Doe',
            'email': 'johndoe@email.com'
            }]
        }
    mock_get = mocker.patch('httpx.AsyncClient.get')
    mock_get.return_value = mocker.Mock(status_code=200)
    mock_get.return_value.json.return_value = mock_response

    service = MockAPIService()
    contacts = await service.get_contacts()

    mock_get.assert_called_once_with(
        'https://challenge.trio.dev/api/v1/contacts'
        )
    assert contacts == mock_response
