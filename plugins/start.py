from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support Group", url="https://t.me/Mercy_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Mercy_Bots")],
       [InlineKeyboardButton("🍭Dev", url="https://t.me/ok_bie_bot)]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
