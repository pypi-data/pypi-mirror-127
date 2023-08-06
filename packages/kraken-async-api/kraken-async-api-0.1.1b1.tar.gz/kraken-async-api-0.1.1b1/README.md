# Kraken-async-api
[![codecov](https://codecov.io/gh/nickjfenton/kraken-async-api/branch/master/graph/badge.svg?token=ZRHK1XGKDA)](https://codecov.io/gh/nickjfenton/kraken-async-api)

A library for asynchronous communications with the Kraken cryptocurrency exchange.

## Quickstart

```python
import asyncio

from kraken_async_api import Kraken, Config, Depth


async def print_(data):
    print(data)


async def main():
    # Only necessary if you wish to communicate with private endpoints
    config = Config(api_key="your api-key", api_sec="your api-sec")

    kraken_exchange = await Kraken.connect(async_callback=print_, config=config)

    # ... your usage of the API here, for example:
    kraken_exchange.public.subscribe_to_book(["XXBTZGBP"], Depth.D25)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

```
