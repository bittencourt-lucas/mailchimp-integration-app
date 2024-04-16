import httpx


class HttpxClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    def set_headers(self, headers):
        self.headers = headers

    def set_url(self, url):
        self.url = url

    async def get(self, endpoint):
        try:
            response = await self.client.get(
                f'{self.url}{endpoint}',
                headers=self.headers
                )
            return response.json()
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def post(self, endpoint, json):
        try:
            response = await self.client.post(
                f'{self.url}{endpoint}',
                headers=self.headers,
                json=json
                )
            return response.json()
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def close(self):
        await self.client.aclose()
