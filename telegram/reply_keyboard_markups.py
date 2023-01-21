import telebot
# import constanta


class Keyboard:

    def __init__(self, bot):
        self.bot = bot

    def main_menu(self, message, edit=False):
        main_control_menu = [[telebot.types.InlineKeyboardButton("👋 Про нас", callback_data="m_c_1")],
                             [telebot.types.InlineKeyboardButton("👤 Користувачі", callback_data="m_c_2")],
                             ]

        markup = telebot.types.InlineKeyboardMarkup(main_control_menu)

        if not edit:
            self.bot.send_message(message.chat.id, text="Оберіть пункт меню:", reply_markup=markup)
        else:
            self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                       text="Оберіть пункт меню:", reply_markup=markup)

    def main_under_chat_menu(self, message):
        main_menu_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        main_menu_markup.row("👋 Про нас")
        main_menu_markup.row("👤 Користувачі")
        self.bot.send_message(message.chat.id, text="Оберіть пункт меню:", reply_markup=main_menu_markup)

    def get_users_list(self, call):
        # Деяка інформація з юзерів, яку наприклад взяли із бази даних
        users = [{"username": "Andrew", "user_id": 1273234, "user_role": "Admin"},
                 {"username": "Daniel", "user_id": 7278213, "user_role": "Moderator"},
                 ]

        users_list_markup = []
        for i in range(len(users)):
            button_text = users[i]["username"] + " - " + str(users[i]["user_id"]) + " - " + users[i]["user_role"]
            button = telebot.types.InlineKeyboardButton(button_text, callback_data=f"show_user_profile_{users[i]['user_id']}")
            users_list_markup.append([button])

        markup = telebot.types.InlineKeyboardMarkup(users_list_markup)

        self.bot.send_message(chat_id=call.from_user.id, text="Список користувачів:", reply_markup=markup)