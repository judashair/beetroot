import telebot
import constanta
from reply_keyboard_markups import Keyboard

bot = telebot.TeleBot(constanta.token)
keyboard = Keyboard(bot)


@bot.message_handler(commands=["start"])
def start(message):
    user = message.from_user.id
    welcome_message = "Привіт, мене щойно створили :)"
    bot.send_message(user, welcome_message)
    keyboard.main_under_chat_menu(message)


@bot.message_handler(func=lambda msg: "👤 Користувачі" == msg.text, content_types=["text"])
def user_control_handler(message):
    keyboard.get_users_list(message)


if __name__ == "__main__":
    bot.polling(none_stop=True)


