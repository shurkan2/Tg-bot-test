from random import choice
from telebot import TeleBot


TOKEN = "7987526576:AAHUKP7w5kwZG-Pp7tzfLYzxIo6-E2tu2dg"
bot = TeleBot(TOKEN)
game_strings = ["камень", "ножницы", "бумага"]


class Game:
    comp = 0
    user = 0
    def update(self, user_winner):
        if user_winner:
            self.user += 1
            return 'Победил'
        self.comp += 1
        return 'Проиграл'
    def reset(self):
        self.comp = 0
        self.user = 0


gm = Game()
@bot.message_handler(func=lambda x: x.text.lower() in game_strings)
def game(message):
    user_choice = message.text.lower()
    bot_choice = choice(game_strings)
    bot.send_message(message.chat.id, bot_choice)
    if user_choice == "камень" and bot_choice == "ножницы":
        msg = gm.update(user_winner=True)
    elif user_choice == "бумага" and bot_choice == "камень":
        msg = gm.update(user_winner=True)
    elif user_choice == "ножницы" and bot_choice == "бумага":
        msg = gm.update(user_winner=True)
    elif user_choice == bot_choice:
        msg = "ничья"
    else:
        msg = gm.update(user_winner=False)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['points'])
def points(message):
    img = open('game.png', 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()
    bot.send_message(message.chat.id, f"бот: {gm.comp} игрок: {gm.user}")

@bot.message_handler(commands=['reset'])
def reset(message):
    gm.reset()
    bot.send_message(message.chat.id, "Очки обнулены")


if __name__ == '__main__':
    bot.polling(non_stop=True)
