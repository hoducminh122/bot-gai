import os
import time
import requests
import telebot
from telebot import types
from flask import Flask, request

# ====== 🔐 CẤU HÌNH ======
TOKEN = os.getenv("BOT_TOKEN", "8404415280:AAGvc7OvMZvXP88c7s48S_BK4uEIl_gTHH4")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# ====== 💾 ĐẾM LƯỢT DÙNG ======
usage_count = {"anhgai": 0, "anhgaisexy": 0, "videogai": 0, "regarena": 0}
LOADING_GIF = "https://media.tenor.com/On7kvXhzml4AAAAj/loading-gif.gif"

# ====== 🪄 HÀM PHỤ TRỢ ======
def show_loading(chat_id, text="⏳ Đang xử lý yêu cầu..."):
    msg = bot.send_animation(chat_id, LOADING_GIF, caption=text)
    time.sleep(1.8)
    return msg

# ====== 🌸 MENU CHÍNH ======
@bot.message_handler(commands=["start", "menu"])
def show_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💖 Ảnh Gái Xinh", callback_data="anhgai"),
        types.InlineKeyboardButton("🔥 Ảnh Sexy", callback_data="anhgaisexy"),
        types.InlineKeyboardButton("🎬 Video Gái", callback_data="videogai"),
        types.InlineKeyboardButton("🎮 Reg Garena", callback_data="regarena"),
        types.InlineKeyboardButton("👑 About Bot", callback_data="about")
    )

    bot.send_message(
        message.chat.id,
        f"🌸 *Xin chào {message.from_user.first_name or 'bạn'}!*\n"
        "Tôi là **BOT ĐA NĂNG LUXURY PRO+** 💎\n\n"
        "Chọn tính năng bạn muốn 👇",
        parse_mode="Markdown",
        reply_markup=markup
    )

# ====== ⚙️ CALLBACK ======
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data in ["anhgai", "anhgaisexy", "videogai", "regarena"]:
        msg = show_loading(call.message.chat.id)

        if call.data == "anhgai":
            send_anhgai(call.message)
        elif call.data == "anhgaisexy":
            send_anhgaisexy(call.message)
        elif call.data == "videogai":
            send_videogai(call.message)
        elif call.data == "regarena":
            handle_reggarena(call.message)

        bot.delete_message(call.message.chat.id, msg.message_id)

    elif call.data == "about":
        show_about(call.message)

# ====== 💖 ẢNH GÁI XINH ======
def send_anhgai(message):
    usage_count["anhgai"] += 1
    try:
        res = requests.get("https://api.zeidteam.xyz/images/gai").json()
        if res.get("status") and res.get("data"):
            bot.send_photo(
                message.chat.id,
                res["data"],
                caption=f"💞 *Gái xinh #{res.get('count','?')}*\n📊 Lượt xem: `{usage_count['anhgai']}`",
                parse_mode="Markdown"
            )
        else:
            bot.reply_to(message, "❌ API không trả về ảnh.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: `{e}`", parse_mode="Markdown")

# ====== 🔥 ẢNH GÁI SEXY ======
def send_anhgaisexy(message):
    usage_count["anhgaisexy"] += 1
    try:
        res = requests.get("https://api.zeidteam.xyz/images/gaisexy").json()
        if res.get("status") and res.get("data"):
            bot.send_photo(
                message.chat.id,
                res["data"],
                caption=f"🔥 *Ảnh sexy* 🔥\n📊 Lượt xem: `{usage_count['anhgaisexy']}`",
                parse_mode="Markdown"
            )
        else:
            bot.reply_to(message, "❌ API không trả về ảnh.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: `{e}`", parse_mode="Markdown")

# ====== 🎬 VIDEO GÁI ======
def send_videogai(message):
    usage_count["videogai"] += 1
    try:
        res = requests.get("https://api.zeidteam.xyz/videos/gai").json()
        if res.get("status") and res.get("data"):
            bot.send_video(
                message.chat.id,
                res["data"],
                caption=f"🎥 Video dễ thương 💕\n📊 `{usage_count['videogai']}` lượt xem",
                parse_mode="Markdown"
            )
        else:
            bot.reply_to(message, "❌ API không trả về video.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: `{e}`", parse_mode="Markdown")

# ====== 🎮 REG GARENA ======
def handle_reggarena(message):
    usage_count["regarena"] += 1
    try:
        res = requests.get("https://keyherlyswar.x10.mx/Apidocs/reglq.php").json()
        if res.get("status") and res.get("result"):
            acc = res["result"][0]
            text = (
                "🎮 *Tài khoản Garena đã tạo thành công!*\n\n"
                f"👤 User: `{acc['account']}`\n"
                f"🔑 Pass: `{acc['password']}`\n"
                f"📊 Lượt tạo: `{usage_count['regarena']}`\n"
                "⚠️ Hãy đổi mật khẩu sau khi đăng nhập!"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")
        else:
            bot.reply_to(message, "❌ API không phản hồi hợp lệ.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: `{e}`", parse_mode="Markdown")

# ====== 👑 ABOUT ======
def show_about(message):
    text = (
        "👑 *BOT GÁI XINH\n"
        "─────────────────────────────\n"
        "💻 Dev: @minhiosfefe\n"
        "🌐 API: ZeidTeam & HerlysWar\n"
        "📆 Phiên bản: V2.5\n\n"
        "✨ Gõ /menu để bắt đầu lại 🎉"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# ====== 🌐 FLASK WEBHOOK ======
@app.route("/" + TOKEN, methods=["POST"])
def getMessage():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME', 'your-app-name.up.railway.app')}/{TOKEN}")
    return "Webhook set ✅", 200

# ====== 🚀 CHẠY APP ======
if __name__ == "__main__":
    print("🤖 BOT LUXURY PRO+ đang hoạt động trên Railway...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
