from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_i18n import I18nContext, LazyFilter
#
from loader import router_user
from keyboard.main import main_keyboard

@router_user.message(CommandStart())
async def start(message: Message, i18n: I18nContext) -> None:
    name = message.from_user.mention_html() # type: ignore
    await message.answer(
        text=i18n.get("hello", user=name),
        reply_markup=main_keyboard
    )


@router_user.message(LazyFilter("help"))
async def help_handler(message: Message, i18n: I18nContext) -> None:
    await message.answer(i18n.help())


@router_user.message(F.text.in_(["🇺🇿 Uzbek", "🇷🇺 Русский", "🇬🇧 English"]))
async def language_selector(message: Message, i18n: I18nContext) -> None:
    lang_map = {
        "🇺🇿 Uzbek": "uz",
        "🇷🇺 Русский": "ru",
        "🇬🇧 English": "en"
    }
    selected_locale = lang_map.get(message.text, "en") # type: ignore
    await i18n.set_locale(selected_locale)

    await message.answer(
        i18n.get("hello", user=message.from_user.full_name), # type: ignore
        reply_markup=main_keyboard
    )