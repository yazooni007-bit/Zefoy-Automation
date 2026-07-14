import os
import telebot
import subprocess

# جلب توكن البوت تلقائياً من إعدادات Render
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك في بوت زيادة مشاهدات تيك توك! 🚀\n\nأرسل لي رابط الفيديو الآن وسأقوم بالعمل تلقائياً.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if "tiktok.com" in url:
        bot.reply_to(message, "تم استلام الرابط! جاري تشغيل السكربت لزيادة المشاهدات... ⏳")
        try:
            # تشغيل السكربت الرئيسي مع إرسال الرابط كمدخل
            process = subprocess.Popen(
                ['python', 'main.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            # إرسال الرابط وتخطي الاختيارات تلقائياً
            stdout, stderr = process.communicate(input=f"{url}\n")
            bot.reply_to(message, "اكتملت العملية! تحقق من مشاهدات الفيديو الآن. 🎉")
        except Exception as e:
            bot.reply_to(message, f"حدث خطأ أثناء التشغيل: {str(e)}")
    else:
        bot.reply_to(message, "عذراً، يرجى إرسال رابط فيديو تيك توك صحيح.")

print("البوت يعمل الآن ومستعد لاستقبال الرسائل...")
bot.infinity_polling()
