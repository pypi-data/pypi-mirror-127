# EnjoyDevApi

#### Библиотека для работы с EnjoyMickey API.

---
Использование:
```python
import asyncio
from EnjoyDevApi.api import Api, KeyLevel


async def main():
    api = Api(
        'token',        # Your token
        KeyLevel.guest  # Your token level
    )

    res = await api.banCheck(627925818429145119)

    print(res.is_banned)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

