from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class GetListsService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self):
        response = await self.client.get_lists()
        await self.client.close()
        return response
