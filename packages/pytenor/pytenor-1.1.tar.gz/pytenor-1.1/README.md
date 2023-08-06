<p align="center">
    <img src="logo.png"></img>
</p>

# PyTenor
A simple API wrapper for tenor's gif api that is built with asyncio.

PyTenor's code is small and fairly documented as well using docstrings. There are plans to add an actual documentation in this README in the future..

## Installation
```
python -m pip install pytenor
```

## Examples
```py
import asyncio
from pytenor import Tenor

api = Tenor(key="api key here")


async def main():
    # Search for gifs. This returns a GIF object.
    gifs = await api.search("linux users opening a new tab")

    print("Here are the gifs I found")
    for gif in gifs:
        print(f"URL: {gif.url} | Available Formats: {gif.available_formats}")


if __name__ == "__main__":
    asyncio.run(main())

```

## Covered API Endpoints
- /search
- /trending
- /categories
- /search_suggestions
- /autocomplete
- /trending_terms
- /registershare
- /gifs

For more help on what parameters you can pass onto each method. Please red [Tenor's API documentation](https://tenor.com/gifapi/documentation).
