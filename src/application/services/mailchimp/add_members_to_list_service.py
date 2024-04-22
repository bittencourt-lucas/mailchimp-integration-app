import logging
from typing import List
from src.application.models.mailchimp_contact import MailchimpContact
from src.application.models.contact import Contact
from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class AddMembersToListService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self, list_id: str,
                      members: List[MailchimpContact]
                      ) -> List[MailchimpContact]:
        """
        Add members to a Mailchimp list.

        Returns a list of added members if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        added_members: List[Contact] = []

        try:
            for member in members:
                response: List[MailchimpContact] = await \
                    self.client.add_members_to_list(
                        list_id,
                        member
                        )
                if response['email']:
                    added_members.append({
                        'firstName': member['merge_fields']['FNAME'],
                        'lastName': member['merge_fields']['LNAME'],
                        'email': member['email_address'],
                    })
            await self.client.close()
            return added_members
        except Exception as e:
            logging.error(f'Error: {e}')
            await self.client.close()
            raise ConnectionError('Error adding members to list')
