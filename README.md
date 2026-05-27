# afxapicom

An unofficial async Python client for currency exchange rates.

## Installation

Install from pip:
```sh
pip install afxapicom
```

Install from source:
```sh
pip install git+https://github.com/MrBaconHat/afxapi-python.git
```

## Usage

All requests are made using the `Client` class, initialized with your API key.

```python
import afxapicom
import asyncio

async def main():
    client = afxapicom.Client('YOUR_API_KEY')
    # make calls here

asyncio.run(main())
```

### Check API Status

```python
result = await client.status()
print(result)
```

### Retrieve Currencies

```python
result = await client.currencies(currencies=['EUR', 'USD'])
print(result)
```

### Latest Exchange Rates

```python
result = await client.latest(base_currency='USD', currencies=['EUR', 'GBP'])
print(result)
```

### Historical Exchange Rates

```python
result = await client.historical('2024-01-01', base_currency='USD')
print(result)
```

### Exchange Rates Over a Range

```python
result = await client.range('2024-01-01', '2024-01-07', base_currency='USD')
print(result)
```

### Convert Currencies

```python
result = await client.convert(1000, base_currency='USD', currencies=['EUR', 'GBP'])
print(result)
```

## Error Handling

```python
from afxapicom import Client
from afxapicom.errors import AuthenticationFailed, RateLimited, QuotaExceeded

async def main():
    client = Client('YOUR_API_KEY')
    try:
        result = await client.latest()
        print(result)
    except AuthenticationFailed:
        print("Invalid API key")
    except RateLimited:
        print("Rate limit hit, slow down")
    except QuotaExceeded:
        print("Monthly quota exceeded")

asyncio.run(main())
```
