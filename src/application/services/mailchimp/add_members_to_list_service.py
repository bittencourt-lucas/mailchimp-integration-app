from src.infrastructure.externals.mailchimp_api_client \
    import MailchimpAPIClient


class AddMembersToListService:
    def __init__(self):
        self.client = MailchimpAPIClient()

    async def execute(self, list_id, members):
        response = await self.client.add_members_to_list(list_id, members)
        return response
