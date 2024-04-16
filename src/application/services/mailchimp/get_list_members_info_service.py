from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class GetListMembersInfoService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self, list_id):
        response = await self.client.get_list_members_info(list_id)
        return response
