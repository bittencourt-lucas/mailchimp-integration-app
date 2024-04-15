from src.infrastructure.clients.mailchimp_client import MailchimpClient


class MailchimpService:
    def __init__(self):
        self.client = MailchimpClient()

    async def create_list(self, data):
        try:
            response = await self.client.post(
                endpoint='/lists',
                json=data
            )
            return response
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def get_list_members_info(self, list_id):
        try:
            response = await self.client.get(
                endpoint=f'/lists/{list_id}/members'
            )
            return response
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def add_member_to_list(self, list_id, data):
        try:
            response = await self.client.post(
                endpoint=f'/lists/{list_id}/members',
                json=data
            )
            return response
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def close(self):
        await self.client.close()
