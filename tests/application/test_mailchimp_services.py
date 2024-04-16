import os
import pytest
from src.application.services.mailchimp.add_members_to_list_service \
    import AddMembersToListService


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
