import os
import pytest
from src.application.services.mailchimp.add_members_to_list_service \
    import AddMembersToListService
from src.application.services.mailchimp.create_list_service \
    import CreateListService
from src.application.services.mailchimp.get_list_members_info_service \
    import GetListMembersInfoService


@pytest.mark.asyncio
async def test_create_list_service(mocker):
    mock_request = {
        'name': 'Test List',
    }
    mock_response = [{
        'id': 'test_list_id',
    }]

    mock_post = mocker.patch('httpx.AsyncClient.post')
    mock_post.return_value = mocker.Mock(status_code=200)
    mock_post.return_value.json.return_value = mock_response

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_KEY': 'test_api',
        'MAILCHIMP_BASE_URL': 'https://us1.api.mailchimp.com/3.0'
        })

    service = CreateListService()
    response = await service.execute(mock_request)

    mock_post.assert_called_once_with(
        f'{os.environ.get('MAILCHIMP_BASE_URL')}/lists',
        headers={'Authorization': f'Bearer {os.getenv('MAILCHIMP_API_KEY')}'},
        json=mock_request,
    )
    assert response == mock_response


@pytest.mark.asyncio
async def test_get_list_members_info_service(mocker):
    list_id = 'test_list_id'
    mock_response = [{
        'email_address': 'test@email.com',
        'status': 'subscribed',
        'merge_fields': {
            'FNAME': 'Test',
            'LNAME': 'User'
        }
    }]

    mock_get = mocker.patch('httpx.AsyncClient.get')
    mock_get.return_value = mocker.Mock(status_code=200)
    mock_get.return_value.json.return_value = mock_response

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_KEY': 'test_api',
        'MAILCHIMP_BASE_URL': 'https://us1.api.mailchimp.com/3.0'
        })

    service = GetListMembersInfoService()
    response = await service.execute(list_id)

    mock_get.assert_called_once_with(
        f'{os.environ.get('MAILCHIMP_BASE_URL')}/lists/{list_id}/members',
        headers={'Authorization': f'Bearer {os.getenv('MAILCHIMP_API_KEY')}'},
    )
    assert response == mock_response


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
        'id': 'test_list_id',
    }

    mock_post = mocker.patch('httpx.AsyncClient.post')
    mock_post.return_value = mocker.Mock(status_code=200)
    mock_post.return_value.json.return_value = mock_response

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_KEY': 'test_api',
        'MAILCHIMP_BASE_URL': 'https://us1.api.mailchimp.com/3.0'
        })

    service = AddMembersToListService()
    response = await service.execute(list_id, mock_request)

    mock_post.assert_called_once_with(
        f'{os.environ.get('MAILCHIMP_BASE_URL')}/lists/{list_id}/members',
        headers={'Authorization': f'Bearer {os.getenv('MAILCHIMP_API_KEY')}'},
        json=mock_request,
    )
    assert response == mock_response
