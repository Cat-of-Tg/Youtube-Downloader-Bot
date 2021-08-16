from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔧Support", url="https://t.me/Teamladz_bothub")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Ok_bie_bot")],
        [InlineKeyboardButton(text="Help", callback_data="help_back")],
        [InlineKeyboardButton("🍭Dev", url="https://t.me/Ok_Bie_Bot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
