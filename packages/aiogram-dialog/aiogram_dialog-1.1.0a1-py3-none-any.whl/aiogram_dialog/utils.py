from dataclasses import dataclass
from typing import Optional, Tuple

from aiogram import Bot
from aiogram.types import Message, CallbackQuery, Chat, InlineKeyboardMarkup, \
    ChatMemberUpdated
from aiogram.exceptions import TelegramBadRequest

from .context.events import (
    DialogUpdateEvent, ChatEvent
)

CB_SEP = "\x1D"


def get_chat(event: ChatEvent) -> Chat:
    if isinstance(event, (Message, DialogUpdateEvent, ChatMemberUpdated)):
        return event.chat
    elif isinstance(event, CallbackQuery):
        if not event.message:
            return Chat(id=event.from_user.id)
        return event.message.chat


@dataclass
class NewMessage:
    chat: Chat
    text: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    parse_mode: Optional[str] = None
    force_new: bool = False
    disable_web_page_preview: Optional[bool] = None


def intent_callback_data(intent_id: str, callback_data: Optional[str]) -> Optional[str]:
    if callback_data is None:
        return None
    return intent_id + CB_SEP + callback_data


def add_indent_id(message: NewMessage, intent_id: str):
    if not message.reply_markup:
        return
    for row in message.reply_markup.inline_keyboard:
        for button in row:
            button.callback_data = intent_callback_data(
                intent_id, button.callback_data
            )


def remove_indent_id(callback_data: str) -> Tuple[str, str]:
    if CB_SEP in callback_data:
        intent_id, new_data = callback_data.split(CB_SEP, maxsplit=1)
        return intent_id, new_data
    return "", callback_data


async def show_message(bot: Bot, new_message: NewMessage, old_message: Message):
    if not old_message or new_message.force_new:
        await remove_kbd(bot, old_message)
        return await send_message(bot, new_message)
    if new_message.text == old_message.text and new_message.reply_markup == old_message.reply_markup:
        return old_message
    try:
        return await bot.edit_message_text(
            message_id=old_message.message_id,
            chat_id=old_message.chat.id,
            text=new_message.text,
            reply_markup=new_message.reply_markup,
            parse_mode=new_message.parse_mode,
            disable_web_page_preview=new_message.disable_web_page_preview,
        )
    except TelegramBadRequest as err:
        if 'message is not modified' in err.message:
            return old_message
        elif 'message can\'t be edited' in err.message:
            return await send_message(bot, new_message)
        elif 'message to edit not found' in err.message:
            return await send_message(bot, new_message)
        else:
            raise err


async def remove_kbd(bot: Bot, old_message: Optional[Message]):
    if old_message:
        try:
            await bot.edit_message_reply_markup(
                message_id=old_message.message_id, chat_id=old_message.chat.id
            )
        except TelegramBadRequest as err:
            if 'message is not modified' in err.message:
                pass
            elif 'message can\'t be edited' in err.message:
                pass
            elif 'message to edit not found' in err.message:
                pass
            else:
                raise err


async def send_message(bot: Bot, new_message: NewMessage):
    return await bot.send_message(
        chat_id=new_message.chat.id,
        text=new_message.text,
        reply_markup=new_message.reply_markup,
        parse_mode=new_message.parse_mode,
        disable_web_page_preview=new_message.disable_web_page_preview,
    )
