import os
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram_i18n import I18nMiddleware
from aiogram.client.default import DefaultBotProperties
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()
router_user = Router()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # type: ignore
dp.include_router(router=router_user)
i18n = I18nMiddleware(core=FluentRuntimeCore(path="locales/{locale}/LC_MESSAGES"), default_locale="en")