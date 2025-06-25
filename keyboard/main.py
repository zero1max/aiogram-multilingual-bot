from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import LazyProxy

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=LazyProxy("help"))], # type: ignore
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇷🇺 Русский"),
            KeyboardButton(text="🇬🇧 English")
        ]
    ],
    resize_keyboard=True
)