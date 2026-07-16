import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

TOKEN = os.environ.get("TOKEN")

# ===== СТАРТ С КНОПКАМИ =====
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

# ===== ОБРАБОТКА КНОПОК =====
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "wallet":
        text = (
            "💳 <b>Кошелёк</b>\n\n"
            "💰 Баланс: <b>0.00 USDT</b>\n\n"
            "📥 Пополнить: через карты\n"
            "📤 Вывести: обратитесь в поддержку\n\n"
            "🔒 Безопасность: 2FA не подключена"
        )
    elif data == "cards":
        text = (
            "💳 <b>Привязанные карты</b>\n\n"
            "🔹 Карт не найдено.\n\n"
            "➕ Чтобы привязать карту, обратитесь в поддержку."
        )
    elif data == "order":
        text = (
            "📝 <b>Создание сделки</b>\n\n"
            "Выберите тип сделки:\n"
            "🟢 /buy — Купить\n"
            "🔴 /sell — Продать\n\n"
            "Формат: /order [тип] [сумма] [валюта]\n"
            "Пример: /order buy 100 USDT"
        )
    elif data == "deals":
        text = (
            "📊 <b>Мои сделки</b>\n\n"
            "🕐 История сделок пуста.\n"
            "Создайте первую сделку через меню!\n\n"
            "📈 Статистика:\n"
            "• Всего сделок: 0\n"
            "• Успешных: 0\n"
            "• Объём: 0.00 USDT"
        )
    elif data == "market":
        text = (
            "📈 <b>Рынок</b>\n\n"
            "💰 Актуальные курсы:\n"
            "• BTC: $67,432.18\n"
            "• ETH: $3,521.09\n"
            "• USDT: $1.00\n\n"
            "🔄 Обновляется каждые 5 минут."
        )
    elif data == "profile":
        user = query.from_user
        text = (
            f"👤 <b>Профиль пользователя</b>\n\n"
            f"🆔 ID: <code>{user.id}</code>\n"
            f"📛 Имя: {user.first_name}\n"
            f"🔗 Юзернейм: @{user.username if user.username else 'Не указан'}\n\n"
            f"💼 Статус: Верифицирован ✅\n"
            f"💰 Баланс: 0.00 USDT\n"
            f"📊 Сделок: 0\n"
            f"⭐ Рейтинг: 5.0"
        )
    elif data == "referral":
        text = (
            "👥 <b>Реферальная программа</b>\n\n"
            "🔗 Ваша ссылка:\n"
            f"<code>https://t.me/{context.bot.username}?start={query.from_user.id}</code>\n\n"
            "💰 Вы получаете 10% от комиссии приглашённых пользователей!\n"
            "📊 Приглашено: 0 человек\n"
            "💵 Заработано: 0.00 USDT"
        )
    elif data == "language":
        text = ("🌐 <b>Выбор языка</b>\n\n"
            "🇷🇺 Русский (выбран)\n"
            "🇬🇧 English\n"
            "🇨🇳 中文\n\n"
            "💡 Скоро добавим больше языков!"
        )
    elif data == "support":
        text = (
            "📞 <b>Поддержка 24/7</b>\n\n"
            "По всем вопросам обращайтесь:\n"
            "👤 @portalchik_support\n\n"
            "⏱ Среднее время ответа: 5 минут\n"
            "📧 Email: support@portalchik.ru"
        )
    else:
        text = "Неизвестная команда."
    
    # Кнопка "Назад в меню"
    keyboard = [[InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")

# ===== КНОПКА НАЗАД =====
async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
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
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")

# ===== HELP =====
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📋 <b>Список команд:</b>\n\n"
        "/start — Главное меню\n"
        "/help — Помощь\n"
        "/profile — Профиль\n"
        "/buy — Купить\n"
        "/sell — Продать\n"
        "/market — Рынок\n"
        "/deals — Мои сделки\n"
        "/wallet — Кошелёк\n"
        "/cards — Карты\n"
        "/referral — Рефералы\n"
        "/language — Язык\n"
        "/support — Поддержка"
    )
    await update.message.reply_html(text)

# ===== ОСТАЛЬНЫЕ КОМАНДЫ =====
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"👤 <b>Профиль пользователя</b>\n\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"📛 Имя: {user.first_name}\n"
        f"🔗 Юзернейм: @{user.username if user.username else 'Не указан'}\n\n"
        f"💼 Статус: Верифицирован ✅\n"
        f"💰 Баланс: 0.00 USDT\n"
        f"📊 Сделок: 0\n"
        f"⭐ Рейтинг: 5.0"
    )
    await update.message.reply_html(text)

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "🟢 <b>Покупка</b>\n\nВыберите валюту: BTC, ETH, USDT\nФормат: /order buy [сумма] [валюта]"
    await update.message.reply_html(text)

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "🔴 <b>Продажа</b>\n\nВыберите валюту: BTC, ETH, USDT\nФормат: /order sell [сумма] [валюта]"
    await update.message.reply_html(text)

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📝 Формат: /order [buy/sell] [сумма] [валюта]\nПример: /order buy 100 USDT"
    await update.message.reply_html(text)

async def deals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📊 <b>Мои сделки</b>\n\nСделок пока нет."
    await update.message.reply_html(text)

async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📈 <b>Рынок</b>\n\nBTC: $67,432 | ETH: $3,521 | USDT: $1.00"
    await update.message.reply_html(text)

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "💳 <b>Кошелёк</b>\n\nБаланс: 0.00 USDT"
    await update.message.reply_html(text)

async def cards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "💳 <b>Карты</b>\n\nНет привязанных карт."
    await update.message.reply_html(text)

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "👥 <b>Рефералы</b>\n\nПриглашено: 0 | Заработано: 0.00 USDT"
    await update.message.reply_html(text)

async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "🌐 <b>Язык</b>\n\n🇷🇺 Русский"
    await update.message.reply_html(text)

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📞 <b>Поддержка 24/7</b>\n\n👤 @portalchik_support\n📧 support@portalchik.ru"
    await update.message.reply_html(text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Используйте /start для открытия меню.")

# ===== ЗАПУСК =====
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Команды
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
    
    # Кнопки
    app.add_handler(CallbackQueryHandler(back_to_start, pattern="back_to_start"))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    # Обычные сообщения
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("✅ Портальчик запущен!")
    app.run_polling()

if name == "__main__":
    main()
