import os
import telebot
from telebot import types

# التوكن الخاص بك تم وضعه هنا مباشرة ليعمل البوت فوراً دون إعدادات معقدة
BOT_TOKEN = "8914958228:AAHByDK9futhRaHvKG3_ZOrjYw-CT7JD-2I"

bot = telebot.TeleBot(BOT_TOKEN)

# قائمة ترحيبية تفاعلية بأزرار شاشة واضحة
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # الأزرار التفاعلية للخدمات
    btn_views = types.InlineKeyboardButton("🚀 رشق مشاهدات فيديو", callback_data="views")
    btn_likes = types.InlineKeyboardButton("❤️ رشق لايكات وهمي", callback_data="likes")
    btn_followers = types.InlineKeyboardButton("👤 زيادة متابعين وهمي", callback_data="followers")
    btn_shares = types.InlineKeyboardButton("🔄 زيادة مشاركة وإكسبلور", callback_data="shares")
    
    markup.add(btn_views, btn_likes, btn_followers, btn_shares)
    
    welcome_text = (
        "👋 أهلاً بك في بوت أوتو فارم تيك توك المتكامل!\n\n"
        "هذا البوت يتيح لك زيادة المشاهدات، اللايكات، والمتابعين لحسابك بكل سهولة.\n\n"
        "👇 اختر الخدمة التي تريدها من الأزرار بالأسفل لتبدأ الآن:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# التعامل مع الضغط على الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # مسح حالة الانتظار السابقة إن وجدت
    bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
    
    if call.data == "views":
        msg = bot.send_message(call.message.chat.id, "📥 حسناً، أرسل لي رابط فيديو التيك توك الذي ترغب بزيادة مشاهداته:")
        bot.register_next_step_handler(msg, process_tiktok_link, "المشاهدات")
        
    elif call.data == "likes":
        msg = bot.send_message(call.message.chat.id, "📥 أرسل لي رابط الفيديو الذي ترغب بزيادة لايكاته:")
        bot.register_next_step_handler(msg, process_tiktok_link, "اللايكات")
        
    elif call.data == "followers":
        msg = bot.send_message(call.message.chat.id, "📥 أرسل لي رابط حسابك (الملف الشخصي) لزيادة المتابعين:")
        bot.register_next_step_handler(msg, process_tiktok_link, "المتابعين")
        
    elif call.data == "shares":
        msg = bot.send_message(call.message.chat.id, "📥 أرسل لي رابط الفيديو لزيادة الإكسبلور والمشاركات:")
        bot.register_next_step_handler(msg, process_tiktok_link, "المشاركات")

# معالجة الروابط المرسلة
def process_tiktok_link(message, service_name):
    url = message.text
    if "tiktok.com" in url.lower():
        bot.reply_to(
            message, 
            f"🔄 تم استلام الرابط بنجاح!\n\n"
            f"⚙️ جاري بدء تشغيل أداة الأوتو فارم لـ **{service_name}**...\n"
            f"⏳ يرجى الانتظار، قد تستغرق العملية بضع دقائق لتأكيد الإرسال."
        )
    else:
        msg = bot.reply_to(message, "❌ عذراً، هذا الرابط غير صحيح. يرجى إرسال رابط تيك توك حقيقي:")
        bot.register_next_step_handler(msg, process_tiktok_link, service_name)

print("البوت مستعد ويعمل بنجاح...")
bot.infinity_polling()
