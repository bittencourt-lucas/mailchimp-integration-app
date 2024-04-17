from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class GetListsService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self):
        try:
            response = await self.client.get_lists()
            await self.client.close()
            return response
        except Exception as e:
            print(f'Error: {e}')
            await self.client.close()
            return None
