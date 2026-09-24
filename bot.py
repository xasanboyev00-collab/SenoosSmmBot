import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 Xizmatlar", callback_data="services")],
        [InlineKeyboardButton("🛒 Buyurtma berish", callback_data="order")],
        [InlineKeyboardButton("📞 Admin bilan bog‘lanish", callback_data="admin")],
    ]

    await update.message.reply_text(
        "👋 Assalomu alaykum!\n\n"
        "🤖 Seenos SMM Bot'ga xush kelibsiz!\n\n"
        "Kerakli bo‘limni tanlang:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "services":
        await query.edit_message_text(
            "📋 Xizmatlar:\n\n"
            "🔹 Instagram xizmatlari\n"
            "🔹 Telegram xizmatlari\n"
            "🔹 TikTok xizmatlari\n"
            "🔹 YouTube xizmatlari\n\n"
            "Buyurtma berish uchun menyudan foydalaning."
        )

    elif query.data == "order":
        await query.edit_message_text(
            "🛒 Buyurtma berish\n\n"
            "Buyurtma berish uchun admin bilan bog‘laning."
        )

    elif query.data == "admin":
        await query.edit_message_text(
            "📞 Admin bilan bog‘lanish\n\n"
            "Admin: @SeenosSmmBot"
        )


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN topilmadi!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
