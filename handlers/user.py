from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram_i18n import I18nContext, LazyFilter
#
from loader import router_user
from keyboard.main import main_keyboard

class User(StatesGroup):
    name = State()
    surname = State()


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
async def language_selector(message: Message, i18n: I18nContext, state: FSMContext) -> None:
    lang_map = {
        "🇺🇿 Uzbek": "uz",
        "🇷🇺 Русский": "ru",
        "🇬🇧 English": "en"
    }
    selected_locale = lang_map.get(message.text, "en") # type: ignore
    await i18n.set_locale(selected_locale)

    await message.answer(
        i18n.get("name"))# type: ignore
    await state.set_state(User.name)

@router_user.message(User.name)
async def get_user_name(msg: Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer(i18n.get("surname"))
    await state.set_state(User.surname)

@router_user.message(User.surname)
async def get_user_surname(msg: Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(surname=msg.text)
    data = await state.get_data()
    await msg.answer(text=i18n.get("user_detail", name=data["name"], surname=data["surname"]).replace("\\n", "\n"))
    await state.clear()