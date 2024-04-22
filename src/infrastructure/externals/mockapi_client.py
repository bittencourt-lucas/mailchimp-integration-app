import os
import logging
from dotenv import load_dotenv
from typing import List
from src.application.models.mockapi_contact import MockAPIContact
from src.application.models.contact import Contact
from src.infrastructure.clients.http_client import HttpClient


class MockAPIClient:
    def __init__(self):
        load_dotenv()

        self.base_url = os.getenv('MOCKAPI_BASE_URL')
        if not self.base_url:
            raise ValueError('MOCKAPI_BASE_URL is not set')

        self.client = HttpClient()
        self.client.set_url(self.base_url)
        self.client.set_headers({'Content-Type': 'application/json'})

    async def get_contacts(self) -> List[Contact]:
        """
        Add members to a specific list in Mailchimp API.

        Returns the response if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            response: List[MockAPIContact] = await self.client.get('/contacts')
            return self.format_contacts(response)
        except Exception as e:
            logging.error(f'Error: {e}')
            raise ConnectionError('Error getting data')

    def format_contacts(self, contacts: List[MockAPIContact]) -> List[Contact]:
        """
        Add members to a specific list in Mailchimp API.

        Returns the response if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        return [
            {
                'firstName': contact['firstName'],
                'lastName': contact['lastName'],
                'email': contact['email']
            }
            for contact in contacts
        ]

    async def close(self):
        """
        Close the HTTP client.
        """
        await self.client.close()
