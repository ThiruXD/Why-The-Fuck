import config
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from FallenMusic import db_mem


def primary_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        InlineKeyboardButton(
                text=f" ▅ ▇ ▆ ▃ ▄ ▁ ▅ ▇ ▅ ",
                callback_data=f"I'ᴠᴇ  Gɪғᴛᴇᴅ  Wᴏʀᴅ's  Aʟʟ  Sᴏɴɢ  Fᴏʀ  Yᴏᴜ  Bʏ  Tʜɪs  Bᴏᴛ  .·  ˚  •  .  ⋆🧚",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT
            ),
            InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ ↺", callback_data=f"close"),
        ],
    ]
    return buttons


audio_markup = InlineKeyboardMarkup(
    [
        InlineKeyboardButton(
                text=f" ▅ ▇ ▆ ▃ ▄ ▁ ▅ ▇ ▅ ",
                callback_data=f"I'ᴠᴇ  Gɪғᴛᴇᴅ  Wᴏʀᴅ's  Aʟʟ  Sᴏɴɢ  Fᴏʀ  Yᴏᴜ  Bʏ  Tʜɪs  Bᴏᴛ  .·  ˚  •  .  ⋆🧚",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton("↻ ᴄʟᴏsᴇ ↺", callback_data="close")],
    ]
)


close_key = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")],
    ]
)
