import os
import pytest
from fastapi import APIRouter
from fastapi.testclient import TestClient
from src.routers.router import root_router
from main import app


client = TestClient(app)


def test_root_router_exists():
    assert root_router.__class__ is APIRouter


@pytest.mark.asyncio
async def test_sync_contacts(mocker):
    mock_data = [{
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'johndoe@email.com',
        }]

    mock_response = {
        'success': True,
        'data': mock_data
    }

    mocker.patch.dict(os.environ, {
        'MOCKAPI_BASE_URL': 'https://challenge.trio.dev/api/v1',
        'MAILCHIMP_API_KEY': 'test_api',
        'MAILCHIMP_API_BASE_URL': 'https://us1.api.mailchimp.com/3.0',
        })

    mock_get_contacts = mocker.patch(
        'src.application.services.mockapi.get_contacts_service.'
        'GetContactsService.execute'
    )
    mock_get_contacts.return_value = mock_data

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
    mock_add_members.return_value = mock_data

    mock_get = mocker.patch('httpx.AsyncClient.get')
    mock_get.return_value = mocker.Mock(status_code=200)
    mock_get.return_value.json.return_value = mock_response

    response = client.get("/contacts/sync")

    assert response.status_code == 200
    found = False
    for key, value in mock_response.items():
        if key in response.json() and value == response.json()[key]:
            found = True
            break

    assert found
