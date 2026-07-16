import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💼 Кошелёк", callback_data="wallet"),
         InlineKeyboardButton("💳 Карты", callback_data="cards")],
        [InlineKeyboardButton("📝 Создать сделку", callback_data="order"),
         InlineKeyboardButton("📊 Мои сделки", callback_data="deals")],
        [InlineKeyboardButton("📈 Маркет", callback_data="market"),
         InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("👥 Рефералы", callback_data="referral"),
         InlineKeyboardButton("🌐 Язык", callback_data="language")],
        [InlineKeyboardButton("📞 Поддержка", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = (
        "🔐 <b>Добро пожаловать в Портальчик!</b>\n\n"
        "🏦 Специализированный сервис по обеспечению безопасности внебиржевых сделок.\n\n"
        "⚙️ <b>Наши преимущества:</b>\n"
        "• 🤖 Автоматизированный алгоритм\n"
        "• ⚡ Скорость и автоматизация\n"
        "• 💳 Удобный и быстрый ввод средств\n"
        "• 💰 Комиссия всего <b>1%</b>\n"
        "• 🕐 Режим работы <b>24/7</b>\n"
        "• 📞 Поддержка 24/7\n\n"
        "👇 Выберите нужный раздел:"
    )
    await update.message.reply_html(text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    
    if data == "wallet":
        text = "💳 <b>Кошелёк</b>\n\n💰 Баланс: <b>0.00 USDT</b>\n\n📥 Пополнить: через карты\n📤 Вывести: обратитесь в поддержку\n\n🔒 Безопасность: 2FA не подключена"
    elif data == "cards":
        text = "💳 <b>Привязанные карты</b>\n\n🔹 Карт не найдено.\n\n➕ Чтобы привязать карту, обратитесь в поддержку."
    elif data == "order":
        text = "📝 <b>Создание сделки</b>\n\nВыберите тип сделки:\n🟢 /buy — Купить\n🔴 /sell — Продать\n\nФормат: /order buy 100 USDT"
    elif data == "deals":
        text = "📊 <b>Мои сделки</b>\n\n🕐 История сделок пуста.\n\n📈 Статистика:\n• Всего сделок: 0\n• Успешных: 0\n• Объём: 0.00 USDT"
    elif data == "market":
        text = "📈 <b>Рынок</b>\n\n💰 Актуальные курсы:\n• BTC: $67,432\n• ETH: $3,521\n• USDT: $1.00\n\n🔄 Обновляется каждые 5 минут."
    elif data == "profile":
        user = query.from_user
        text = f"👤 <b>Профиль</b>\n\n🆔 ID: <code>{user.id}</code>\n📛 Имя: {user.first_name}\n🔗 Юзернейм: @{user.username if user.username else 'Не указан'}\n\n💼 Статус: Верифицирован ✅\n💰 Баланс: 0.00 USDT\n📊 Сделок: 0\n⭐ Рейтинг: 5.0"
    elif data == "referral":
        text = f"👥 <b>Реферальная программа</b>\n\n🔗 Ваша ссылка:\n<code>https://t.me/{context.bot.username}?start={query.from_user.id}</code>\n\n💰 Вы получаете 10% от комиссии приглашённых!\n📊 Приглашено: 0\n💵 Заработано: 0.00 USDT"
    elif data == "language":
        text = "🌐 <b>Выбор языка</b>\n\n🇷🇺 Русский (выбран)\n🇬🇧 English\n🇨🇳 中文"
    elif data == "support":
        text = "📞 <b>Поддержка 24/7</b>\n\n👤 @portalchik_support\n📧 support@portalchik.ru\n⏱ Ответ: ~5 минут"
    else:
        text = "Ошибка."
    
    keyboard = [[InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")

async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("💼 Кошелёк", callback_data="wallet"),
         InlineKeyboardButton("💳 Карты", callback_data="cards")],
        [InlineKeyboardButton("📝 Создать сделку", callback_data="order"),InlineKeyboardButton("📊 Мои сделки", callback_data="deals")],
        [InlineKeyboardButton("📈 Маркет", callback_data="market"),
         InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("👥 Рефералы", callback_data="referral"),
         InlineKeyboardButton("🌐 Язык", callback_data="language")],
        [InlineKeyboardButton("📞 Поддержка", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = (
        "🔐 <b>Добро пожаловать в Портальчик!</b>\n\n"
        "🏦 Специализированный сервис по обеспечению безопасности внебиржевых сделок.\n\n"
        "⚙️ <b>Наши преимущества:</b>\n"
        "• 🤖 Автоматизированный алгоритм\n"
        "• ⚡ Скорость и автоматизация\n"
        "• 💳 Удобный и быстрый ввод средств\n"
        "• 💰 Комиссия всего <b>1%</b>\n"
        "• 🕐 Режим работы <b>24/7</b>\n"
        "• 📞 Поддержка 24/7\n\n"
        "👇 Выберите нужный раздел:"
    )
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📋 <b>Команды:</b>\n\n"
        "/start — Главное меню\n"
        "/help — Помощь\n"
        "/profile — Профиль\n"
        "/buy — Купить\n"
        "/sell — Продать\n"
        "/market — Рынок\n"
        "/deals — Сделки\n"
        "/wallet — Кошелёк\n"
        "/cards — Карты\n"
        "/referral — Рефералы\n"
        "/language — Язык\n"
        "/support — Поддержка"
    )
    await update.message.reply_html(text)

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = f"👤 <b>Профиль</b>\n\n🆔 ID: <code>{user.id}</code>\n📛 Имя: {user.first_name}\n💰 Баланс: 0.00 USDT\n📊 Сделок: 0"
    await update.message.reply_html(text)

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("🟢 <b>Покупка</b>\n\nВалюты: BTC, ETH, USDT\nФормат: /order buy 100 USDT")

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("🔴 <b>Продажа</b>\n\nВалюты: BTC, ETH, USDT\nФормат: /order sell 100 USDT")

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("📝 <b>Ордер</b>\n\nФормат: /order buy 100 USDT")

async def deals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("📊 <b>Сделки</b>\n\nСделок пока нет.")

async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("📈 <b>Рынок</b>\n\nBTC: $67,432 | ETH: $3,521 | USDT: $1.00")

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("💳 <b>Кошелёк</b>\n\nБаланс: 0.00 USDT")

async def cards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("💳 <b>Карты</b>\n\nНет карт.")

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("👥 <b>Рефералы</b>\n\nПриглашено: 0 | Заработано: 0.00 USDT")

async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("🌐 <b>Язык</b>\n\n🇷🇺 Русский")

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("📞 <b>Поддержка</b>\n\n👤 @portalchik_support\n📧 support@portalchik.ru")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Используйте /start для меню.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("sell", sell))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("deals", deals))
    app.add_handler(CommandHandler("market", market))
    app.add_handler(CommandHandler("wallet", wallet))
    app.add_handler(CommandHandler("cards", cards))
    app.add_handler(CommandHandler("referral", referral))
    app.add_handler(CommandHandler("language", language))
    app.add_handler(CommandHandler("support", support))
    
    app.add_handler(CallbackQueryHandler(back_to_start, pattern="back_to_start"))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("✅ Бот запущен!")
    app.run_polling()

if name == "__main__":
    main()
