import logging
from typing import List
from src.application.models.mailchimp_list import MailchimpList
from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class GetListsService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self) -> List[MailchimpList]:
        """
        Retrieve lists from Mailchimp.

        Returns the response if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            response: List[MailchimpList] = await self.client.get_lists()
            await self.client.close()
            return response
        except Exception as e:
            logging.error(f'Error: {e}')
            await self.client.close()
            raise ConnectionError('Error getting lists')
