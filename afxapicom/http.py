import aiohttp
from .errors import *


class HTTPClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        
        self.session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        await self._get_session()
        return self

    async def __aexit__(self, *args):
        if self.session is not None and not self.session.closed:
            await self.session.close()
            

    async def _get_session(self) -> aiohttp.ClientSession:
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=30)
            )
        return self.session

    async def request(self, endpoint, params: dict | None = None):
        
        params = params or {}
        params['apikey'] = self.api_key

        headers = {}
        headers['User-Agent'] = 'afxapi/1.0'
        
        session = await self._get_session()
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