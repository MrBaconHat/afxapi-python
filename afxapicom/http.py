import aiohttp
from .errors import *


class HTTPClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    async def request(self, endpoint, params: dict | None = None):
        params = params or {}
        params['apikey'] = self.api_key

        headers = {'User-Agent': 'afxapi/1.0'}

        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30)
        ) as session:
            async with session.get(
                self.base_url + endpoint,
                params=params,
                headers=headers
            ) as resp:
                if resp.status == 200:
                    return await resp.json()

                await self.__interpret_status(resp.status, await resp.text())


    async def __interpret_status(self, status, err_msg):
        exc_dict = {
            401: AuthenticationFailed,
            403: Forbidden,
            404: NotFound,
            422: ValidationError,
            429: RateLimited,
            500: InternalServerError
        }

        if status in exc_dict:
            raise exc_dict[status](err_msg)
        else:
            raise Exception(f"HTTP ERROR: {status}: {err_msg}")