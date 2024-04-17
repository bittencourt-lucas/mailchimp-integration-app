import os
import pytest
from src.application.services.mailchimp.add_members_to_list_service \
    import AddMembersToListService
from src.application.services.mailchimp.get_lists_service \
    import GetListsService


@pytest.mark.asyncio
async def test_add_members_to_list_service(mocker):
    list_id = 'test_list_id'
    mock_request = [{
            'email_address': 'test@email.com',
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': 'Test',
                'LNAME': 'User'
            }
        }]
    mock_response = {
        'id': 'test_id',
        'email': 'test@email.com',
        'fistName': 'Test',
        'lastName': 'User'
    }

    mock_post = mocker.patch('httpx.AsyncClient.post')
    mock_post.return_value = mocker.Mock(status_code=200)
    mock_post.return_value.json.return_value = mock_response

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_KEY': 'test_api',
        'MAILCHIMP_API_BASE_URL': 'https://us1.api.mailchimp.com/3.0'
        })

    service = AddMembersToListService()
    await service.execute(list_id, mock_request)

    mock_post.assert_called_once()


@pytest.mark.asyncio
async def test_add_members_to_list_exception(mocker):
    list_id = 'test_list_id'
    mock_request = [{
            'email_address': 'test@email.com',
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': 'Test',
                'LNAME': 'User'
            }
        }]
    url = 'https://us1.api.mailchimp.com/3.0'
    api_key = 'test_key'

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_BASE_URL': url,
        'MAILCHIMP_API_KEY': api_key
        })

    mock_post = mocker.patch('httpx.AsyncClient.post')
    mock_post.side_effect = Exception('Test')

    service = AddMembersToListService()
    response = await service.execute(list_id, mock_request)

    assert response is None


@pytest.mark.asyncio
async def test_get_lists_service(mocker):
    mock_response = {
        'lists': [
            {
                'id': 'test_id',
                'name': 'Test List'
            }
        ]
    }

    mock_get = mocker.patch('httpx.AsyncClient.get')
    mock_get.return_value = mocker.Mock(status_code=200)
    mock_get.return_value.json.return_value = mock_response

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_KEY': 'test_api',
        'MAILCHIMP_API_BASE_URL': 'https://us1.api.mailchimp.com/3.0'
        })

    service = GetListsService()
    response = await service.execute()

    assert response == mock_response


@pytest.mark.asyncio
async def test_mailchimp_api_get_lists_exception(mocker):
    url = 'https://us1.api.mailchimp.com/3.0'
    api_key = 'test_key'

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_BASE_URL': url,
        'MAILCHIMP_API_KEY': api_key
        })

    mock_get = mocker.patch('httpx.AsyncClient.get')
    mock_get.side_effect = Exception('Test')

    service = GetListsService()
    response = await service.execute()

    assert response is None
