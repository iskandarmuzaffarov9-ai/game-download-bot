from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8520077536:AAESC4_dwcCJ66iqt_EB36ccoc3V7fz-y9o"


# =========================================================
# O'YINLAR
# [nomi, platforma, description, rasm_url, download_url]
# =========================================================

games = {

    "marvel": [
        ["MARVEL SNAP", "Android / iOS / PC",
         "Marvel qahramonlari bilan karta o'yini.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/1997040/header.jpg",
         "https://marvelsnap.com/"],

        ["Marvel Contest of Champions", "Android / iOS",
         "Marvel qahramonlari bilan jangovar o'yin.",
         "https://placehold.co/800x450/jpg?text=Marvel+Contest",
         "https://play.google.com/store/search?q=Marvel%20Contest%20of%20Champions&c=apps"],

        ["Marvel Future Fight", "Android / iOS",
         "Marvel qahramonlarini yig'ib jamoa tuzing.",
         "https://placehold.co/800x450/jpg?text=Marvel+Future+Fight",
         "https://play.google.com/store/search?q=Marvel%20Future%20Fight&c=apps"],

        ["Marvel Puzzle Quest", "Android / iOS",
         "Marvel qahramonlari bilan puzzle RPG.",
         "https://placehold.co/800x450/jpg?text=Marvel+Puzzle+Quest",
         "https://play.google.com/store/search?q=Marvel%20Puzzle%20Quest&c=apps"],

        ["MARVEL Strike Force", "Android / iOS",
         "Marvel qahramonlari bilan strategik RPG.",
         "https://placehold.co/800x450/jpg?text=Marvel+Strike+Force",
         "https://play.google.com/store/search?q=MARVEL%20Strike%20Force&c=apps"]
    ],

    "survival": [
        ["Minecraft", "Android / iOS / PC",
         "Ochiq dunyo, qurilish va survival.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/251570/header.jpg",
         "https://www.minecraft.net/"],

        ["Terraria", "Android / iOS / PC",
         "2D sandbox adventure va survival.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg",
         "https://play.google.com/store/search?q=Terraria&c=apps"],

        ["Don't Starve", "Android / iOS",
         "Sirli dunyoda omon qolish.",
         "https://placehold.co/800x450/jpg?text=Dont+Starve",
         "https://play.google.com/store/search?q=Dont%20Starve&c=apps"],

        ["Survivalcraft", "Android / iOS",
         "Sandbox survival adventure.",
         "https://placehold.co/800x450/jpg?text=Survivalcraft",
         "https://play.google.com/store/search?q=Survivalcraft&c=apps"],

        ["Last Day on Earth", "Android / iOS",
         "Post-apocalyptic survival.",
         "https://placehold.co/800x450/jpg?text=Last+Day+on+Earth",
         "https://play.google.com/store/search?q=Last%20Day%20on%20Earth&c=apps"]
    ],

    "car": [
        ["Asphalt Legends", "Android / iOS / PC",
         "Supercarlar bilan arcade racing.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/1815780/header.jpg",
         "https://asphaltlegends.com/stores"],

        ["CarX Drift Racing 2", "Android / iOS",
         "Drift va tuning o'yini.",
         "https://placehold.co/800x450/jpg?text=CarX+Drift",
         "https://play.google.com/store/search?q=CarX%20Drift%20Racing%202&c=apps"],

        ["Traffic Rider", "Android / iOS",
         "Mototsikl bilan highway racing.",
         "https://placehold.co/800x450/jpg?text=Traffic+Rider",
         "https://play.google.com/store/search?q=Traffic%20Rider&c=apps"],

        ["Hill Climb Racing 2", "Android / iOS",
         "Physics-based racing.",
         "https://placehold.co/800x450/jpg?text=Hill+Climb+Racing+2",
         "https://play.google.com/store/search?q=Hill%20Climb%20Racing%202&c=apps"],

        ["Real Racing 3", "Android / iOS",
         "Realistik mobil racing.",
         "https://placehold.co/800x450/jpg?text=Real+Racing+3",
         "https://play.google.com/store/search?q=Real%20Racing%203&c=apps"]
    ],

    "shooting": [
        ["Free Fire", "Android / iOS",
         "Mobil battle royale.",
         "https://placehold.co/800x450/jpg?text=Free+Fire",
         "https://play.google.com/store/search?q=Free%20Fire&c=apps"],

        ["Call of Duty Mobile", "Android / iOS",
         "Mobil multiplayer shooter.",
         "https://placehold.co/800x450/jpg?text=Call+of+Duty+Mobile",
         "https://play.google.com/store/search?q=Call%20of%20Duty%20Mobile&c=apps"],

        ["PUBG MOBILE", "Android / iOS",
         "Mobil multiplayer shooter.",
         "https://placehold.co/800x450/jpg?text=PUBG+MOBILE",
         "https://play.google.com/store/search?q=PUBG%20MOBILE&c=apps"],

        ["Brawl Stars", "Android / iOS",
         "Tezkor multiplayer action.",
         "https://placehold.co/800x450/jpg?text=Brawl+Stars",
         "https://play.google.com/store/search?q=Brawl%20Stars&c=apps"],

        ["Zooba", "Android / iOS",
         "Multiplayer action o'yini.",
         "https://placehold.co/800x450/jpg?text=Zooba",
         "https://play.google.com/store/search?q=Zooba&c=apps"]
    ],

    "action": [
        ["Honkai Star Rail", "Android / iOS / PC",
         "Anime uslubidagi action RPG.",
         "https://placehold.co/800x450/jpg?text=Honkai+Star+Rail",
         "https://play.google.com/store/search?q=Honkai%20Star%20Rail&c=apps"],

        ["Genshin Impact", "Android / iOS / PC",
         "Ochiq dunyo action RPG.",
         "https://placehold.co/800x450/jpg?text=Genshin+Impact",
         "https://genshin.hoyoverse.com/"],

        ["Shadow Fight 4", "Android / iOS",
         "Fighting va action o'yini.",
         "https://placehold.co/800x450/jpg?text=Shadow+Fight+4",
         "https://play.google.com/store/search?q=Shadow%20Fight%204&c=apps"],

        ["Soul Knight", "Android / iOS",
         "Pixel-style action adventure.",
         "https://placehold.co/800x450/jpg?text=Soul+Knight",
         "https://play.google.com/store/search?q=Soul%20Knight&c=apps"],

        ["Guardian Tales", "Android / iOS",
         "Pixel RPG adventure.",
         "https://placehold.co/800x450/jpg?text=Guardian+Tales",
         "https://play.google.com/store/search?q=Guardian%20Tales&c=apps"]
    ],

    "racing": [
        ["Asphalt Legends", "Android / iOS / PC",
         "Tezkor arcade racing.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/1815780/header.jpg",
         "https://asphaltlegends.com/stores"],

        ["Need for Speed No Limits", "Android / iOS",
         "Street racing.",
         "https://placehold.co/800x450/jpg?text=NFS+No+Limits",
         "https://play.google.com/store/search?q=Need%20for%20Speed%20No%20Limits&c=apps"],

        ["Real Racing 3", "Android / iOS",
         "Realistik racing.",
         "https://placehold.co/800x450/jpg?text=Real+Racing+3",
         "https://play.google.com/store/search?q=Real%20Racing%203&c=apps"],

        ["CSR Racing 2", "Android / iOS",
         "Drag racing.",
         "https://placehold.co/800x450/jpg?text=CSR+Racing+2",
         "https://play.google.com/store/search?q=CSR%20Racing%202&c=apps"],

        ["Mario Kart Tour", "Android / iOS",
         "Mario qahramonlari bilan racing.",
         "https://placehold.co/800x450/jpg?text=Mario+Kart+Tour",
         "https://play.google.com/store/search?q=Mario%20Kart%20Tour&c=apps"]
    ],

    "adventure": [
        ["Sky Children of the Light", "Android / iOS / PC",
         "Chiroyli exploration adventure.",
         "https://placehold.co/800x450/jpg?text=Sky+Children",
         "https://www.thatskygame.com/"],

        ["The Room", "Android / iOS",
         "Mystery va puzzle adventure.",
         "https://placehold.co/800x450/jpg?text=The+Room",
         "https://play.google.com/store/search?q=The%20Room&c=apps"],

        ["Monument Valley", "Android / iOS",
         "Optical illusion puzzle.",
         "https://placehold.co/800x450/jpg?text=Monument+Valley",
         "https://play.google.com/store/search?q=Monument%20Valley&c=apps"],

        ["Alto's Odyssey", "Android / iOS",
         "Chiroyli endless adventure.",
         "https://placehold.co/800x450/jpg?text=Altos+Odyssey",
         "https://play.google.com/store/search?q=Altos%20Odyssey&c=apps"],

        ["Stardew Valley", "Android / iOS / PC",
         "Farm va adventure RPG.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg",
         "https://play.google.com/store/search?q=Stardew%20Valley&c=apps"]
    ],

    "horror": [
        ["Granny", "Android / iOS",
         "Escape horror adventure.",
         "https://placehold.co/800x450/jpg?text=Granny",
         "https://play.google.com/store/search?q=Granny&c=apps"],

        ["Eyes The Horror Game", "Android / iOS",
         "Horror exploration.",
         "https://placehold.co/800x450/jpg?text=Eyes+Horror",
         "https://play.google.com/store/search?q=Eyes%20The%20Horror%20Game&c=apps"],

        ["Five Nights at Freddy's", "Android / iOS / PC",
         "Classic horror game.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/319510/header.jpg",
         "https://play.google.com/store/search?q=Five%20Nights%20at%20Freddys&c=apps"],

        ["The Baby in Yellow", "Android / iOS",
         "Horror adventure.",
         "https://placehold.co/800x450/jpg?text=The+Baby+in+Yellow",
         "https://play.google.com/store/search?q=The%20Baby%20in%20Yellow&c=apps"],

        ["Hello Neighbor", "Android / iOS / PC",
         "Mystery stealth adventure.",
         "https://placehold.co/800x450/jpg?text=Hello+Neighbor",
         "https://play.google.com/store/search?q=Hello%20Neighbor&c=apps"]
    ],

    "openworld": [
        ["Minecraft", "Android / iOS / PC",
         "Sandbox open-world.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/251570/header.jpg",
         "https://www.minecraft.net/"],

        ["Genshin Impact", "Android / iOS / PC",
         "Open-world RPG.",
         "https://placehold.co/800x450/jpg?text=Genshin+Impact",
         "https://genshin.hoyoverse.com/"],

        ["Roblox", "Android / iOS / PC",
         "Millionlab user-created worlds.",
         "https://placehold.co/800x450/jpg?text=Roblox",
         "https://www.roblox.com/"],

        ["Goat Simulator", "Android / iOS / PC",
         "Crazy open-world simulator.",
         "https://placehold.co/800x450/jpg?text=Goat+Simulator",
         "https://play.google.com/store/search?q=Goat%20Simulator&c=apps"],

        ["Terraria", "Android / iOS / PC",
         "Sandbox open-world adventure.",
         "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg",
         "https://play.google.com/store/search?q=Terraria&c=apps"]
    ],

    "retro": [
        ["Sonic the Hedgehog", "Android / iOS",
         "Classic Sonic platformer.",
         "https://placehold.co/800x450/jpg?text=Sonic",
         "https://play.google.com/store/search?q=Sonic%20the%20Hedgehog&c=apps"],

        ["PAC-MAN", "Android / iOS",
         "Classic arcade game.",
         "https://placehold.co/800x450/jpg?text=PAC-MAN",
         "https://play.google.com/store/search?q=PAC-MAN&c=apps"],

        ["Tetris", "Android / iOS",
         "Classic puzzle game.",
         "https://placehold.co/800x450/jpg?text=Tetris",
         "https://play.google.com/store/search?q=Tetris&c=apps"],

        ["Crossy Road", "Android / iOS",
         "Classic-style arcade game.",
         "https://placehold.co/800x450/jpg?text=Crossy+Road",
         "https://play.google.com/store/search?q=Crossy%20Road&c=apps"],

        ["Angry Birds 2", "Android / iOS",
         "Classic mobile arcade.",
         "https://placehold.co/800x450/jpg?text=Angry+Birds+2",
         "https://play.google.com/store/search?q=Angry%20Birds%202&c=apps"]
    ]
}


# =========================================================
# KATEGORIYALAR
# =========================================================

categories = {
    "marvel": "🦸 Marvel Games",
    "survival": "🌲 Survival Games",
    "car": "🚗 Car Games",
    "shooting": "🎯 Shooting Games",
    "action": "⚔️ Action Games",
    "racing": "🏎️ Racing Games",
    "adventure": "🗺️ Adventure Games",
    "horror": "👻 Horror Games",
    "openworld": "🌍 Open World Games",
    "retro": "🕹️ Retro Games"
}


# =========================================================
# CATEGORY MENU
# =========================================================

def category_keyboard():

    keyboard = []
    items = list(categories.items())

    for i in range(0, len(items), 2):

        row = [
            InlineKeyboardButton(
                items[i][1],
                callback_data=f"cat:{items[i][0]}"
            )
        ]

        if i + 1 < len(items):
            row.append(
                InlineKeyboardButton(
                    items[i + 1][1],
                    callback_data=f"cat:{items[i + 1][0]}"
                )
            )

        keyboard.append(row)

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# START
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎮 <b>GAME DOWNLOAD BOT</b>\n\n"
        "📱 Android / iOS / PC o'yinlar\n\n"
        "🔥 Kategoriyani tanlang:",
        parse_mode="HTML",
        reply_markup=category_keyboard()
    )


# =========================================================
# CATEGORY
# =========================================================

async def category(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    category_id = query.data.split(":", 1)[1]

    if category_id not in games:
        await query.answer(
            "❌ Kategoriya topilmadi!",
            show_alert=True
        )
        return

    keyboard = []

    for index, game_info in enumerate(games[category_id]):

        keyboard.append([
            InlineKeyboardButton(
                f"🎮 {game_info[0]}",
                callback_data=f"game:{category_id}:{index}"
            )
        ])

    keyboard.append([
        InlineKeyboardButton(
            "⬅️ Kategoriyalar",
            callback_data="home"
        )
    ])

    await query.edit_message_text(
        f"<b>{categories[category_id]}</b>\n\n"
        "🎮 O'yinni tanlang:",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# GAME
# =========================================================

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    try:

        parts = query.data.split(":")

        if len(parts) != 3:
            await query.message.reply_text(
                "❌ O'yin ma'lumotida xatolik."
            )
            return

        category_id = parts[1]
        index = int(parts[2])

        selected = games[category_id][index]

        name = selected[0]
        platform = selected[1]
        description = selected[2]
        image_url = selected[3]
        download_url = selected[4]

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📥 DOWNLOAD",
                    url=download_url
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Orqaga",
                    callback_data=f"cat:{category_id}"
                ),
                InlineKeyboardButton(
                    "🏠 Kategoriyalar",
                    callback_data="home"
                )
            ]
        ])

        caption = (
            f"🎮 <b>{name}</b>\n\n"
            f"📱 <b>Platform:</b> {platform}\n\n"
            f"📝 {description}\n\n"
            "👇 Yuklab olish uchun tugmani bosing:"
        )

        # RASM BILAN YUBORISH
        try:

            await query.message.reply_photo(
                photo=image_url,
                caption=caption,
                parse_mode="HTML",
                reply_markup=keyboard
            )

        except Exception as image_error:

            print("Rasm xatosi:", image_error)

            # Rasm ishlamasa ham o'yin ochiladi
            await query.message.reply_text(
                caption,
                parse_mode="HTML",
                reply_markup=keyboard
            )

    except Exception as error:

        print("GAME ERROR:", error)

        await query.message.reply_text(
            "❌ O'yinni ochishda xatolik yuz berdi."
        )


# =========================================================
# HOME
# =========================================================

async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "🎮 <b>GAME DOWNLOAD BOT</b>\n\n"
        "📱 Android / iOS / PC o'yinlar\n\n"
        "🔥 Kategoriyani tanlang:",
        parse_mode="HTML",
        reply_markup=category_keyboard()
    )


# =========================================================
# HANDLERS
# =========================================================

app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CallbackQueryHandler(
        category,
        pattern=r"^cat:"
    )
)

app.add_handler(
    CallbackQueryHandler(
        game,
        pattern=r"^game:"
    )
)

app.add_handler(
    CallbackQueryHandler(
        home,
        pattern=r"^home$"
    )
)


print("🎮 Game Download Bot ishga tushdi...")

app.run_polling()