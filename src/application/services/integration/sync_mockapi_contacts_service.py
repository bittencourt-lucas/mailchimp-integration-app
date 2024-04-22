import random
import logging
from typing import List
from src.application.models.contact import Contact
from src.application.models.mockapi_contact import MockAPIContact
from src.application.models.mailchimp_contact import MailchimpContact
from src.application.models.mailchimp_list import MailchimpList
from src.application.models.sync_output import SyncOutput
from src.application.services.mailchimp.add_members_to_list_service \
    import AddMembersToListService
from src.application.services.mailchimp.get_lists_service \
    import GetListsService
from src.application.services.mockapi.get_contacts_service \
    import GetContactsService


class SyncMockApiMailchimpService:
    def __init__(self):
        self.get_contacts_service = GetContactsService()
        self.get_lists_service = GetListsService()
        self.add_members_to_list_service = AddMembersToListService()

    async def execute(self) -> SyncOutput:
        """
        Sync contacts from MockAPI to a Mailchimp list.

        Returns the number of synced contacts and their details if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            contacts: List[MockAPIContact] = await \
                self.get_contacts_service.execute()
            contacts.append(self.generate_new_contact())

            get_lists: List[MailchimpList] = await \
                self.get_lists_service.execute()
            list_id: str = get_lists['lists'][0]['id']

            synced_contacts: List[MailchimpContact] = await \
                self.add_members_to_list_service.execute(
                    list_id,
                    self.format_contacts(contacts),
                )

            output: SyncOutput = {
                'synced_contacts': len(synced_contacts),
                'contacts': synced_contacts,
            }

            return output
        except Exception as e:
            logging.error(f'Error: {e}')
            raise ConnectionError(f'Error syncing contacts: {e}')

    def generate_new_contact(self) -> Contact:
        """
        Generate a new contact with a unique email.

        Returns a dictionary representing the new contact.
        """
        random_number: int = random.randint(0, 1000)
        return {
            'firstName': 'Lucas',
            'lastName': 'Bittencourt',
            'email': f'Lucas.Bittencourt{random_number}@trio.email'
        }

    def format_contacts(self,
                        contacts: List[MockAPIContact]
                        ) -> List[MailchimpContact]:
        """
        Format contacts to match Mailchimp's required structure.

        Returns a list of formatted contacts.
        """
        return [
            {
                'email_address': contact['email'],
                'status': 'subscribed',
                'merge_fields': {
                    'FNAME': contact['firstName'],
                    'LNAME': contact['lastName'],
                },
            }
            for contact in contacts
        ]
