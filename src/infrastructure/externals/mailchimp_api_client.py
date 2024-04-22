import os
import logging
from typing import List
from src.application.models.mailchimp_contact import MailchimpContact
from src.application.models.mailchimp_list import MailchimpList
from src.infrastructure.clients.http_client import HttpClient


class MailchimpAPIClient:
    def __init__(self):
        self.client = HttpClient()

        self.base_url = os.getenv('MAILCHIMP_API_BASE_URL')
        if not self.base_url:
            raise ValueError('MAILCHIMP_API_BASE_URL is not set')

        self.api_key = os.getenv('MAILCHIMP_API_KEY')
        if not self.api_key:
            raise ValueError('MAILCHIMP_API_KEY is not set')

        self.client.set_url(self.base_url)
        self.client.set_headers({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
            })

    async def get_lists(self) -> List[MailchimpList]:
        """
        Retrieve all lists from Mailchimp API.

        Returns the response if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            response: List[MailchimpList] = await self.client.get(
                endpoint='/lists'
            )
            return response
        except Exception as e:
            logging.error(f'Error: {e}')
            raise ConnectionError('Error getting lists from MailChimp')

    async def add_members_to_list(self, list_id: str,
                                  data: List[MailchimpContact]
                                  ) -> List[MailchimpContact]:
        """
        Add members to a specific list in Mailchimp API.

        Returns the response if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            response: List[MailchimpContact] = await self.client.post(
                endpoint=f'/lists/{list_id}/members',
                json=data
            )
            return response
        except Exception as e:
            logging.error(f'Error: {e}')
            raise ConnectionError('Error posting data to MailChimp')

    async def close(self):
        """
        Close the HTTP client.
        """
        await self.client.close()
