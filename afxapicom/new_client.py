from .http import HTTPClient


class Client(HTTPClient):
    def __init__(self, api_key, base='https://api.fxapi.com/v1'):
        super().__init__(base, api_key)

    async def status(self):
        return await self.request('/status')

    async def currencies(self, currencies: list[str] | None = None):
        return await self.request(
            '/currencies',
            params={
                'currencies': ','.join(currencies) if currencies else None
            }
        )

    async def latest(self, base_currency: str | None = None, currencies: list[str] | None = None):
        return await self.request(
            '/latest',
            params={
                'base_currency': base_currency,
                'currencies': ','.join(currencies) if currencies else None
            }
        )

    async def historical(self, date: str, base_currency: str | None = None, currencies: list[str] | None = None):
        return await self.request(
            '/historical',
            params={
                'date': date,
                'base_currency': base_currency,
                'currencies': ','.join(currencies) if currencies else None
            }
        )

    async def range(self, datetime_start: str, datetime_end: str, accuracy: str | None = None, base_currency: str | None = None, currencies: list[str] | None = None):
        return await self.request(
            '/range',
            params={
                'datetime_start': datetime_start,
                'datetime_end': datetime_end,
                'accuracy': accuracy,
                'base_currency': base_currency,
                'currencies': ','.join(currencies) if currencies else None
            }
        )

    async def convert(self, value: float, date: str | None = None, base_currency: str | None = None, currencies: list[str] | None = None):
        return await self.request(
            '/convert',
            params={
                'value': value,
                'date': date,
                'base_currency': base_currency,
                'currencies': ','.join(currencies) if currencies else None
            }
        )