import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_ID = 7655421861  # You (for future use if needed)

# /start command
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()

    # Forward button with shareable text
    keyboard.add(
        InlineKeyboardButton(
            "📢 Forward",
            url="""https://t.me/share/url?url=😍මොන්ඩිසෝරිය😍%0A%0Aඅපිව මතකයි නේද ඔයාලාට ☺️ කලින් චැනල් එක බැන්ඩ් උන නිසා අපේ අලුත් එකට සෙට් වෙන්න 😋. Share කිරිලි මුකුත් නෑ. ආවා බැලුවා🥰%0A%0A──────────────────────────────────%0A%0A⭐️ ඇන්ටා පාරවල්%0Ahttps://t.me/mondisoriya0%0A%0A⭐️ පෙට්ටි කඩපුවා%0Ahttps://t.me/mondisoriya0%0A%0A⭐️ Video Call Fun දීපුවා%0Ahttps://t.me/mondisoriya0%0A%0A⭐️ School සෙස්%0Ahttps://t.me/mondisoriya0%0A%0A⭐️ ලංකාවේ අලුතින්ම ලීක් වෙන ඒවා%0Ahttps://t.me/mondisoriya0%0A%0A⭐️ Free Cam show%0Ahttps://t.me/mondisoriya0%0A%0A──────────────────────────────────%0A%0Aමේවාගේ සුපිරි බඩු අපි චැනල් එකේ දාලා තියෙන්නේ Join වෙලා බලන්න ඒවගේම Daily අපි විඩීයොස් දානවා%0A%0A✅ https://t.me/mondisoriya0%0A✅ https://t.me/mondisoriya0%0A✅ https://t.me/mondisoriya0"""
        )
    )

    # Done button
    keyboard.add(InlineKeyboardButton("✅ Done", callback_data="done"))

    bot.send_message(
        message.chat.id,
        "➡️ පහල *Forward* button එක click කර Telegram Group 2 කට මෙය share කරන්න.\n\n"
        "📸 පසුව *Done* click කරලා Group දෙකට Share කරපු Massage එකෙ Screenshot 02 එවන්න.\n\n"
        "⚠️*NOTE* - Group *දෙකටම* Share කරපු *Screenshots* එවීම අනිවාර්යයි!⚠️\n\n"
        "⚠️එකම Group එකකට දෙවරක් Share නොකරන්න!",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# ✅ Done button clicked
@bot.callback_query_handler(func=lambda call: call.data == "done")
def done_button(call):
    bot.send_message(
        call.message.chat.id,
        "📸 Screenshot දෙක එවන්න bro, group දෙකකකට share කරාද කියලා බලන්න!",
        parse_mode="Markdown"
    )

# 📸 Handle screenshot
    @bot.message_handler(content_types=['photo'])
    def handle_screenshot(message):
        user_id = message.chat.id

        # Send confirmation to user
        bot.send_message(
            user_id,
            "✅ Screenshot received!\n"
            "You will get the video soon 🔒"
        )

        # Send user ID to you (admin)
        bot.send_message(
            ADMIN_ID,
            f"📸 Screenshot received from user ID: `{user_id}`",
            parse_mode="Markdown"
        )

        # Forward the actual screenshot to you
        bot.forward_message(ADMIN_ID, user_id, message.message_id)

# 🔓 Manually unlock video using /unlock USER_ID
@bot.message_handler(commands=['unlock'])
def unlock_video_command(message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.send_message(message.chat.id, "❌ Usage: `/unlock USER_ID`", parse_mode="Markdown")
            return

        target_user_id = int(parts[1])

        # Replace with your real video file path
        with open("video.mp4", "rb") as video:
            bot.send_video(
                chat_id=target_user_id,
                video=video,
                caption="🎬 Here is your unlocked video. Enjoy!",
                timeout=120
            )

        bot.send_message(message.chat.id, f"✅ Video sent to user `{target_user_id}`", parse_mode="Markdown")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: `{str(e)}`", parse_mode="Markdown")

# Start bot
bot.polling()
