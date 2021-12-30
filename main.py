import telebot

CHAVE_API = '5002420485:AAFIjfSy9qp_8DjNA1ignZwYUzp3c05CY0o'

#links
tormentaFicha = 'https://drive.google.com/file/d/1-S55dIn5PLjmkw5CrMsZw5FjkKjTlH--/view?usp=sharing'
tormentaManual = 'https://drive.google.com/file/d/1-GS_hpstFK_-jpJk8IXbPzoWYFcF37wL/view?usp=sharing'
tormenta20Manual = 'https://drive.google.com/file/d/1RxcYBTA0lwV8eIeHx73fEhQBJ7Ko4cWl/view?usp=sharing'
tormenta20Ficha = 'https://drive.google.com/file/d/1-TY3Y-Gx2GtZNmzyIETsjUi3lst0zqlG/view?usp=sharing'
mutantes3eManual = 'https://drive.google.com/file/d/1-IPAbLVVjBcTF-GDDem7fXLndMNFOnTT/view?usp=sharing'
mutantes3eFicha = 'https://drive.google.com/file/d/1-WYe31MwJN_FQabz8xNTLrLGb-Rrsptq/view?usp=sharing'
mutantes2eManual = 'https://drive.google.com/file/d/1-OebU5P8OSMdesN4u6eLySipV-UqyFgw/view?usp=sharing'
mutantes2eFicha = 'https://drive.google.com/file/d/1-czRU_p8YtlNar0LWv7wAHQVz2J_F9aH/view?usp=sharing'


bot = telebot.TeleBot(CHAVE_API)
#comandos

@bot.message_handler(commands=['TormentaRPG'])
def TormentaRPG(mensagem):
    bot.send_message(mensagem.chat.id, f''' Manual do Jogo:
{tormentaManual}

Ficha de Personagem:
{tormentaFicha}''')


@bot.message_handler(commands=['Tormenta20'])
def Tormenta20(mensagem):
    bot.send_message(mensagem.chat.id, f''' Manual do Jogo:
{tormenta20Manual}

Ficha de Personagem:
{tormenta20Ficha}''')

@bot.message_handler(commands=['Mutantes_e_Malfeitores3e'])
def Mutantes_e_Malfeitores3e(mensagem):
    bot.send_message(mensagem.chat.id, f''' Manual do Jogo:
{mutantes3eManual}

Ficha de Personagem:
{mutantes3eFicha}''')

@bot.message_handler(commands=['Mutantes_e_Malfeitores2e'])
def Mutantes_e_Malfeitores2e(mensagem):
    bot.send_message(mensagem.chat.id, f''' Manual do Jogo:
{mutantes2eManual}

Ficha de Personagem:
{mutantes2eFicha}''')



@bot.message_handler(commands=['Ajuda'])
def Ajuda(mensagem):
    bot.send_message(mensagem.chat.id, 'Ao clicar em uma das opções acima você receberá um link para o download do manual ou ficha de personagem do RPG escolhido')


#mensagem de inicio

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '''Olá Bem Vindo, a biblioteca de RPG, clique em uma das opções abaixo para escolher o RPG desejado.
/TormentaRPG
/Tormenta20
/Mutantes_e_Malfeitores3e
/Mutantes_e_Malfeitores2e
/Ajuda'''
    bot.reply_to(mensagem, texto)



bot.polling()