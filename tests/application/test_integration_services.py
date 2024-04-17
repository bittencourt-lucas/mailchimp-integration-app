import os
import pytest
from src.application.services.integration.sync_mockapi_contacts_service \
    import SyncMockApiMailchimpService


@pytest.mark.asyncio
async def test_sync_mockapi_contacts_service(mocker):
    mock_response = {
        'synced_contacts': 1,
        'contacts': [{
            'email_address': 'test@email.com',
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': 'Test',
                'LNAME': 'User'
            },
        }]
    }

    mock_get_contacts = mocker.patch(
        'src.application.services.mockapi.get_contacts_service.'
        'GetContactsService.execute'
    )
    mock_get_contacts.return_value = [{
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'test@email.com',
    }]

    mock_get_lists = mocker.patch(
        'src.application.services.mailchimp.get_lists_service.'
        'GetListsService.execute'
    )
    mock_get_lists.return_value = {
        'lists': [{
            'id': 'test_list_id',
            'name': 'Test List',
        }]
    }

    mock_add_members = mocker.patch(
        'src.application.services.mailchimp.add_members_to_list_service.'
        'AddMembersToListService.execute'
    )
    mock_add_members.return_value = [{
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
        'MAILCHIMP_API_BASE_URL': 'https://us1.api.mailchimp.com/3.0',
        'MOCKAPI_BASE_URL': 'https://challenge.trio.dev/api/v1'
        })

    service = SyncMockApiMailchimpService()
    response = await service.execute()

    assert response == mock_response

    mock_get_contacts.assert_called_once()
    mock_get_lists.assert_called_once()
    mock_add_members.assert_called_once()
