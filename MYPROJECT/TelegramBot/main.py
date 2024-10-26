from typing import Final, Dict
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import datetime
import json
from datetime import datetime
import pytz
import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
)


TOKEN: Final = os.getenv("TELEGRAM_TOKEN", "7764455626:AAFpHYnRwfIm1Ic5jFqSPhu57ZqPGBgWwD0")
BOT_USERNAME: Final = "@Writerzie_bot"

# Dictionary untuk menyimpan data user dan chat history
user_data: Dict = {}
chat_histories: Dict = {}

#untuk menyimpan data user
def save_user_data():
    with open('user_data.json', 'w') as f:
        json.dump(user_data, f)

# untuk memuat data user
def load_user_data():
    try:
        with open('user_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# untuk mendapatkan waktu Indonesia menggunakan pytz
def get_indonesia_time():
    timezone = pytz.timezone('Asia/Jakarta')
    now = datetime.now(timezone)
    return now

def format_time(time):
    hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    
    return f"{hari[time.weekday()]}, {time.day} {bulan[time.month-1]} {time.year}\n⏰ Pukul {time.strftime('%H:%M:%S')} WIB"

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    if user_id not in user_data:
        user_data[user_id] = {
            "name": update.message.from_user.first_name,
            "join_date": str(datetime.now()),
            "message_count": 0
        }
        save_user_data()
        # Initialize chat history for new user
        chat_histories[user_id] = []
    
    keyboard = [
    [InlineKeyboardButton("Help", callback_data='help')],
    [InlineKeyboardButton("Profile", callback_data='profile')],
    [InlineKeyboardButton("Time", callback_data='time')],
    [InlineKeyboardButton("AI Chat", callback_data='ai_chat')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_message = (
        f"Haii {update.message.from_user.first_name}! 👋\n\n"
        "Selamat datang di Writerzie Bot!\n"
        "Saya adalah bot yang siap membantu kamu dengan dukungan AI.\n\n"
        "Silakan pilih menu di bawah ini:"
    )
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📚 *Daftar Perintah*

/start - Memulai bot
/help - Menampilkan bantuan
/profile - Melihat profil kamu
/menu - Menampilkan menu utama
/time - Menampilkan waktu sekarang
/ai - Mulai chat dengan AI
/reset - Reset chat history dengan AI

💡 *Tips*:
- Gunakan /help [perintah] untuk info detail
- Bot akan merespon pertanyaan umum
- Ketik 'menu' untuk melihat semua fitur
- Chat langsung untuk berbicara dengan AI
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def profile_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    user = user_data.get(user_id, {})
    
    profile_text = (
        f"👤 *Profil Pengguna*\n\n"
        f"Nama: {user.get('name', 'Tidak diketahui')}\n"
        f"Bergabung: {user.get('join_date', 'Tidak diketahui')}\n"
        f"Pesan dikirim: {user.get('message_count', 0)}"
    )
    await update.message.reply_text(profile_text, parse_mode='Markdown')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_time = get_indonesia_time()
    time_message = f"📅 Waktu saat ini:\n{format_time(current_time)}"
    await update.message.reply_text(time_message)

async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Chat aktif! Silakan ajukan pertanyaan atau diskusi Anda.\n"
        "Gunakan /reset untuk mengatur ulang riwayat chat."
    )

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    chat_histories[user_id] = []
    await update.message.reply_text("🔄 Riwayat chat telah direset!")

# Callback query handler


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Memberi tahu Telegram bahwa callback telah diterima
    
    if query.data == 'help':
        await help_command(update, context)
    elif query.data == 'profile':
        await profile_command(update, context)
    elif query.data == 'time':
        await time_command(update, context)
    elif query.data == 'ai_chat':
        await ai_command(update, context)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Memberi tahu Telegram bahwa callback telah diterima
    print(f"Button clicked: {query.data}")

async def get_ai_response(user_id: str, user_input: str) -> str:
    try:
        # mendapat history chat
        history = chat_histories.get(user_id, [])
        
        # membuat sesi chat dengan history
        chat = model.start_chat(history=history)
        
        # menfapat response ai
        response = chat.send_message(user_input)
        
        # Mengupdate History Chat
        history.extend([
            {"role": "user", "parts": [user_input]},
            {"role": "model", "parts": [response.text]}
        ])
        chat_histories[user_id] = history
        
        return response.text
    except Exception as e:
        print(f"Error getting AI response: {e}")
        return "Maaf, terjadi kesalahan dalam memproses permintaan Anda. Silakan coba lagi."

def handle_response(text: str, user_id: str) -> str:
    processed: str = text.lower()
    
    # Menambah hitungan pesan
    if user_id in user_data:
        user_data[user_id]['message_count'] += 1
        save_user_data()
    
    # Cek waktu
    time_keywords = ["jam berapa", "waktu sekarang", "jam sekarang", "tanggal sekarang", "hari ini"]
    if any(keyword in processed for keyword in time_keywords):
        current_time = get_indonesia_time()
        return f"📅 Waktu saat ini:\n{format_time(current_time)}"
    
    # Basic responses
    greetings = ["hai", "halo", "hello", "hi"]
    if any(word in processed for word in greetings):
        return f"Haii! Ada yang bisa saya bantu?"
    
    if "terima kasih" in processed or "makasih" in processed:
        return "Sama-sama! Senang bisa membantu! 😊"
    
    # If no predefined response, use AI
    return None

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    user_id = str(update.message.from_user.id)

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text, user_id)
        else:
            return
    else:
        response = handle_response(text, user_id)

    # If no predefined response, use AI
    if response is None:
        response = await get_ai_response(user_id, text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Memulai Bot...")
    user_data = load_user_data()
    
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('profile', profile_command))
    app.add_handler(CommandHandler('time', time_command))
    app.add_handler(CommandHandler('ai', ai_command))
    app.add_handler(CommandHandler('reset', reset_command))
    
    # Callbacks
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    app.add_error_handler(error)

    print("Bot sudah berfungsi...")
    app.run_polling(poll_interval=3)