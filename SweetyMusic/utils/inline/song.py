# Kanged By © @ITZ_STAR_BOY
# Owner ITZ_STAR_BOY
# All rights reserved. © Alisha © Sweety © Yukki




from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• sᴜᴩᴩᴏʀᴛ •", url="https://t.me/DevilsHeavenMF",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
