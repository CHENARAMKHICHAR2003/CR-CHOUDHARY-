from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Start Handler
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Contact Admin", url="https://t.me/courses_hub2_bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    start_message = """FINALIZING
➤ System Status:
✅ Security verified
✅ Data synced
🔍 Checking access...
📊 Progress: 90%

FREE USER
⚠️ Access Restricted
🗒️ Status: Free User
❌ Downloads: Not Available

💡 To Download Videos:
➤ 🌟 Purchase Premium Plan
➤ 📞 Contact Admin

✨ Benefits:
🚀 Instant Downloads
🎥 HD Quality Videos
🔐 Secure Access
⏰ 24/7 Support
➡️ /upgrade - Upgrade Plan & More Details
"""
    await update.message.reply_text(start_message, reply_markup=reply_markup)

# DRM Handler
async def drm_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    drm_message = """🌟 DRM BOT 🌟
➤ Welcome to Premium DRM Bot!

Available Services:

🔒 LEVEL 1 PREMIUM 🔒
- Physics Wallah
- Study IQ
- IFRAME MediaDelivery
- CP VOD
- Terabox
- YouTube
- Testbook
- Abhinay Math
- Ojha IAS
- Appx ZIP
- Spayee/Graphy Video (.m3u8HLS_KEY)
- Spayee/Graphy PDF (.pdfPSWD)
- Pallycon DRM
💰 Monthly: ₹300/-

🔒 LEVEL 2 PREMIUM 🔒
🎯 TP Stream:
- Forum IAS
- Insight IAS
🎯 VdoCrypt:
- Next IAS
- Kalam Academy
- Utkarsh
- MadeEasy
💰 Monthly: ₹500/-

🔒 LEVEL 3 PREMIUM 🔒
🎯 VdoCipher:
- Vision IAS
- Vajiram & Ravi
- Forum IAS (New)
- LevelUp IAS
- Raus IAS
- Sunya IAS
- OTT Platforms
💰 Monthly: ₹800/-
"""
    await update.message.reply_text(drm_message)

# Main Function
def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
    
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("drm", drm_handler))
    
    app.run_polling()

if __name__ == '__main__':
    main()
