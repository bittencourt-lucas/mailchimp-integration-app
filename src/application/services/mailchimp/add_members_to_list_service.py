import logging
from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class AddMembersToListService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self, list_id, members):
        added_members = []

        try:
            for member in members:
                response = await self.client.add_members_to_list(
                    list_id,
                    member
                    )
                if response['id']:
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
