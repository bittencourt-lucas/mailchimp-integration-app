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

    mocker.patch.dict(os.environ, {
        'MAILCHIMP_API_KEY': 'test_api',
        'MAILCHIMP_API_BASE_URL': 'https://us1.api.mailchimp.com/3.0',
        'MOCKAPI_BASE_URL': 'https://challenge.trio.dev/api/v1'
        })

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
        },
    }]

    response = client.get("/contacts/sync")

    assert response.status_code == 200
    assert response.json() == mock_response
