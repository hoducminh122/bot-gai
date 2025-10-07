import telebot
import requests
from telebot import types
import time
from datetime import datetime

# 💎 TOKEN BOT
TOKEN = "8404415280:AAGvc7OvMZvXP88c7s48S_BK4uEIl_gTHH4"
bot = telebot.TeleBot(TOKEN)

# 🕒 Thời điểm bot khởi động
start_time = datetime.now()

# 📊 Bộ đếm
usage_count = {"anhgai": 0, "anhgaisexy": 0, "videogai": 0, "regarena": 0}
LOADING_GIF = "https://media.tenor.com/On7kvXhzml4AAAAj/loading-gif.gif"

# 🪄 Hiệu ứng loading
def show_loading(chat_id, text="⏳ Đang xử lý yêu cầu..."):
    msg = bot.send_animation(chat_id, LOADING_GIF, caption=text)
    time.sleep(1.8)
    bot.delete_message(chat_id, msg.message_id)

# 🏠 Menu chính
@bot.message_handler(commands=["start", "menu"])
def show_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💖 Ảnh Gái Xinh", callback_data="anhgai"),
        types.InlineKeyboardButton("🔥 Ảnh Sexy", callback_data="anhgaisexy"),
        types.InlineKeyboardButton("🎬 Video Gái", callback_data="videogai"),
        types.InlineKeyboardButton("🎮 Reg Garena", callback_data="regarena"),
        types.InlineKeyboardButton("👑 About Bot", callback_data="about"),
        types.InlineKeyboardButton("⏰ Thời gian bot", callback_data="time")
    )

    bot.send_message(
        message.chat.id,
        f"""
<b>🌸 Xin chào {message.from_user.first_name or 'bạn'}! 💎</b>
┏━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🤖 <b>BOT LUXURY PRO+ v3.0</b> ┃
┗━━━━━━━━━━━━━━━━━━━━━━┛
✨ Chọn tính năng bạn muốn dùng bên dưới 👇
""",
        parse_mode="HTML",
        reply_markup=markup,
    )

# ⚙️ Callback menu
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "anhgai":
        show_loading(call.message.chat.id)
        send_anhgai(call.message)
    elif call.data == "anhgaisexy":
        show_loading(call.message.chat.id)
        send_anhgaisexy(call.message)
    elif call.data == "videogai":
        show_loading(call.message.chat.id)
        send_videogai(call.message)
    elif call.data == "regarena":
        show_loading(call.message.chat.id)
        handle_reggarena(call.message)
    elif call.data == "about":
        show_about(call.message)
    elif call.data == "time":
        bot_uptime(call.message)

# 💖 Ảnh Gái Xinh
def send_anhgai(message):
    usage_count["anhgai"] += 1
    try:
        res = requests.get("https://api.zeidteam.xyz/images/gai").json()
        if res.get("status") and res.get("data"):
            caption = f"""
┏━━━━━━━━━━━━━━━━━┓
💞 <b>GÁI XINH #{res.get('count','?')}</b>
┗━━━━━━━━━━━━━━━━━┛
📊 Lượt xem: <b>{usage_count['anhgai']}</b>
🌷 Vẻ đẹp tự nhiên khiến tim tan chảy 💗
"""
            bot.send_photo(message.chat.id, res["data"], caption=caption, parse_mode="HTML")
        else:
            bot.reply_to(message, "❌ API không trả về ảnh.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: {e}")

# 🔥 Ảnh Sexy
def send_anhgaisexy(message):
    usage_count["anhgaisexy"] += 1
    try:
        res = requests.get("https://api.zeidteam.xyz/images/gaisexy").json()
        if res.get("status") and res.get("data"):
            caption = f"""
┏━━━━━━━━━━━━━━━━┓
🔥 <b>ẢNH SEXY CỰC ĐẸP</b>
┗━━━━━━━━━━━━━━━━┛
📊 Lượt xem: <b>{usage_count['anhgaisexy']}</b>
💃 Sức hấp dẫn không thể chối từ 💋
"""
            bot.send_photo(message.chat.id, res["data"], caption=caption, parse_mode="HTML")
        else:
            bot.reply_to(message, "❌ API không trả về ảnh.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: {e}")

# 🎬 Video Gái
def send_videogai(message):
    usage_count["videogai"] += 1
    try:
        res = requests.get("https://api.zeidteam.xyz/videos/gai").json()
        if res.get("status") and res.get("data"):
            caption = f"""
┏━━━━━━━━━━━━━━━━━━┓
🎥 <b>VIDEO GÁI DỄ THƯƠNG</b>
┗━━━━━━━━━━━━━━━━━━┛
📊 Lượt xem: <b>{usage_count['videogai']}</b>
✨ Xem và chill một chút nào 💕
"""
            bot.send_video(message.chat.id, res["data"], caption=caption, parse_mode="HTML")
        else:
            bot.reply_to(message, "❌ API không trả về video.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: {e}")

# 🎮 Reg Garena
def handle_reggarena(message):
    usage_count["regarena"] += 1
    try:
        res = requests.get("https://keyherlyswar.x10.mx/Apidocs/reglq.php").json()
        if res.get("status") and res.get("result"):
            acc = res["result"][0]
            text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━┓
🎮 <b>TÀI KHOẢN GARENA</b>
┗━━━━━━━━━━━━━━━━━━━━━━┛
👤 Tài khoản: <code>{acc['account']}</code>
🔑 Mật khẩu: <code>{acc['password']}</code>
📊 Tổng lượt tạo: <b>{usage_count['regarena']}</b>
⚠️ Hãy đổi mật khẩu ngay sau khi đăng nhập!
"""
            bot.send_message(message.chat.id, text, parse_mode="HTML")
        else:
            bot.reply_to(message, "❌ API không phản hồi hợp lệ.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi: {e}")

# 👑 About Bot
def show_about(message):
    text = """
┏━━━━━━━━━━━━━━━━━━━━━━┓
👑 <b>BOT LUXURY PRO+ v3.0</b>
┗━━━━━━━━━━━━━━━━━━━━━━┛
💻 Developer: <b>@minhiosfefe</b>
🌐 API: ZeidTeam & HerlysWar
📆 Phiên bản: <b>3.0 (Polling)</b>
✨ Cảm ơn bạn đã sử dụng bot 🎉
"""
    bot.send_message(message.chat.id, text, parse_mode="HTML")

# 🕒 /time – xem thời gian hoạt động
@bot.message_handler(commands=["time"])
def bot_uptime(message):
    now = datetime.now()
    uptime = now - start_time
    h, r = divmod(int(uptime.total_seconds()), 3600)
    m, s = divmod(r, 60)
    start_str = start_time.strftime("%d/%m/%Y - %H:%M:%S")

    text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━┓
⏰ <b>THỜI GIAN HOẠT ĐỘNG</b>
┗━━━━━━━━━━━━━━━━━━━━━━┛
🕒 Đã hoạt động: <b>{h}h {m}m {s}s</b>
📆 Bắt đầu từ: <b>{start_str}</b>
⚙️ Trạng thái: <b>Hoạt động ổn định ✅</b>
"""
    bot.send_message(message.chat.id, text, parse_mode="HTML")

# 🚀 Run bot
print("🤖 BOT LUXURY PRO+ v3.0 đang hoạt động...")
bot.remove_webhook()
bot.infinity_polling(timeout=60, long_polling_timeout=5)
