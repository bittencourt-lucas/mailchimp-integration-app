from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class CreateListService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self, data):
        response = await self.client.create_list(data)
        return response
