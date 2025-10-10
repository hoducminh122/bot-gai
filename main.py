import telebot
import requests
from telebot import types
import time
from datetime import datetime, timedelta

# 💎 TOKEN BOT
TOKEN = "8404415280:AAGvc7OvMZvXP88c7s48S_BK4uEIl_gTHH4"
bot = telebot.TeleBot(TOKEN)

# 🕒 Thời điểm bot khởi động
start_time = datetime.now()

# 📊 Bộ đếm (Đã thêm bộ đếm cho các chức năng mới)
usage_count = {
    "anhgai": 0, "anhgaisexy": 0, "videogai": 0, "regarena": 0,
    "hentai2d": 0, "hentai3d": 0
}
LOADING_GIF = "https://media.tenor.com/On7kvXhzml4AAAAj/loading-gif.gif"

# 🪄 Hiệu ứng loading
def show_loading(chat_id, text="⏳ Đang xử lý yêu cầu..."):
    msg = bot.send_animation(chat_id, LOADING_GIF, caption=text)
    time.sleep(1.8)
    bot.delete_message(chat_id, msg.message_id)

# 🏠 Menu chính (Đã thêm các nút chức năng mới)
@bot.message_handler(commands=["start", "menu"])
def show_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💖 Ảnh Gái Xinh", callback_data="anhgai"),
        types.InlineKeyboardButton("🔥 Ảnh Sexy", callback_data="anhgaisexy"),
        types.InlineKeyboardButton("🎬 Video Gái", callback_data="videogai"),
        types.InlineKeyboardButton("🎬 Video 2D", callback_data="hentai2d"),
        types.InlineKeyboardButton("🎬 Video 3D", callback_data="hentai3d"),
        types.InlineKeyboardButton("🎮 Reg Garena", callback_data="regarena"),
        types.InlineKeyboardButton("👑 About Bot", callback_data="about"),
        types.InlineKeyboardButton("⏰ Uptime Bot", callback_data="uptime"),
        types.InlineKeyboardButton("🕒 Giờ VN", callback_data="current_time")
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

# ⚙️ Callback menu (Đã thêm xử lý cho các callback mới)
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
    elif call.data == "uptime":
        bot_uptime(call.message)
    # ===== CHỨC NĂNG MỚI ĐƯỢC THÊM VÀO =====
    elif call.data == "hentai2d":
        show_loading(call.message.chat.id)
        send_hentai_2d(call.message)
    elif call.data == "hentai3d":
        show_loading(call.message.chat.id)
        send_hentai_3d(call.message)
    elif call.data == "current_time":
        show_current_time(call.message)
    # =========================================

# ===================================================================
# CÁC CHỨC NĂNG GỐC TỪ main2.py (GIỮ NGUYÊN)
# ===================================================================

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
💻 Developer: <b>Zhee💢</b>
🌐 API: Zhee - Bot Vip
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

# ===================================================================
# CÁC CHỨC NĂNG MỚI ĐƯỢC CHUYỂN THỂ TỪ bot.py
# ===================================================================

# 🎬 Video 2D
def send_hentai_2d(message):
    usage_count["hentai2d"] += 1
    try:
        res = requests.get("https://web-production-12dc6.up.railway.app/api/hentai2d", timeout=20).json()
        video_url = res.get("video") or res.get("url")

        if video_url:
            caption = f"""
┏━━━━━━━━━━━━━━━━━┓
🎥 <b>VIDEO ANIME 2D</b>
┗━━━━━━━━━━━━━━━━━┛
📊 Lượt xem: <b>{usage_count['hentai2d']}</b>
💬 Chúc bạn xem vui vẻ nhé 💕
"""
            bot.send_video(message.chat.id, video_url, caption=caption, parse_mode="HTML")
        else:
            bot.reply_to(message, "❌ API không trả về video 2D.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi khi lấy video 2D: {e}")

# 🎬 Video 3D
def send_hentai_3d(message):
    usage_count["hentai3d"] += 1
    try:
        res = requests.get("https://web-production-12dc6.up.railway.app/api/hentai3d", timeout=20).json()
        video_url = res.get("video") or res.get("url")

        if video_url:
            caption = f"""
┏━━━━━━━━━━━━━━━━━┓
💿 <b>VIDEO ANIME 3D</b>
┗━━━━━━━━━━━━━━━━━┛
📊 Lượt xem: <b>{usage_count['hentai3d']}</b>
💬 Chúc bạn xem vui vẻ nhé 💕
"""
            bot.send_video(message.chat.id, video_url, caption=caption, parse_mode="HTML")
        else:
            bot.reply_to(message, "❌ API không trả về video 3D.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Lỗi khi lấy video 3D: {e}")

# 🕒 Xem giờ Việt Nam
def show_current_time(message):
    vn_time = datetime.utcnow() + timedelta(hours=7)
    formatted = vn_time.strftime("🕒 %H:%M:%S\n📅 %d/%m/%Y")
    text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━┓
⏰ <b>GIỜ HIỆN TẠI (VN)</b> 🇻🇳
┗━━━━━━━━━━━━━━━━━━━━━━┛
{formatted}
💡 Hãy tận dụng thời gian thật hiệu quả!
"""
    bot.send_message(message.chat.id, text, parse_mode="HTML")


# 🚀 Run bot
print("🤖 BOT LUXURY PRO+ v3.0 đang hoạt động...")
bot.remove_webhook()
bot.infinity_polling(timeout=60, long_polling_timeout=5)
