import asyncio
from logging import basicConfig, INFO

from contextlib import suppress
from loader import dp, bot, i18n
import handlers

async def main():
    basicConfig(level=INFO)
    i18n.setup(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())