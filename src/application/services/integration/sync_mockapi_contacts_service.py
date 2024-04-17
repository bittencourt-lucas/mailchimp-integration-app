import random
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

    async def execute(self):
        contacts = await self.get_contacts_service.execute()
        contacts.append(self.generate_new_contact())

        get_lists = await self.get_lists_service.execute()
        list_id = get_lists['lists'][0]['id']

        synced_contacts = await self.add_members_to_list_service.execute(
            list_id,
            self.format_contacts(contacts),
        )

        output = {
            'synced_contacts': len(synced_contacts),
            'contacts': synced_contacts,
        }

        return output

    def generate_new_contact(self):
        random_number = random.randint(0, 1000)
        return {
            'firstName': 'Lucas',
            'lastName': 'Bittencourt',
            'email': f'Lucas.Bittencourt{random_number}@trio.email'
        }

    def format_contacts(self, contacts):
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
