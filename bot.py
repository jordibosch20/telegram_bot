import sys
import pickle
from antlr4 import *
from cl.SkyLexer import SkyLexer
from cl.SkyParser import SkyParser
from cl.TreeVisitor import TreeVisitor
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLine Bot! Made by Jordi Bosch Bosch")


def autor(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="@ Jordi Bosch Bosch, estudiant de la FIB, 2020")


def lst(update, context):
    msg = ""
    for i in context.user_data:
        msg = "Identificador " + str(i)
        msg = msg + " --> "
        area, alcada = context.user_data[i].area_alcada()
        msg = msg + " Area = " + str(area) + ", Alçada = " + str(alcada)
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def clean(update, context):
    context.user_data.clear()


def save(update, context):
    # Ha de guardar un fitxer id.skyline
    msg = update.message.text[6:]
    dades = context.user_data[msg]
    msg_aux = msg + ".sky"
    id_usuari = str(update.effective_chat.id)
    nom_fitxer = id_usuari + "_" + msg_aux
    f = open(nom_fitxer, 'wb')
    pickle.dump(dades, f)
    f.close()


def load(update, context):
    print("executat")
    msg = update.message.text[6:]
    msg_aux = msg + ".sky"
    id_usuari = str(update.effective_chat.id)
    nom_fitxer = id_usuari + "_" + msg_aux
    try:
        f = open(nom_fitxer, 'rb')
        variable = pickle.load(f)
        context.user_data[msg] = variable
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="El fitxer no existeix!")


def help(update, context):
    msg = """/start inicia la conversa amb el Bot.
/help el Bot ha de contestar amb una llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús.
/author el Bot ha d’escriure el nom complet de l’autor del projecte i seu correu electrònic oficial de la facultat.
/lst: mostra els identificadors definits i la seva corresponent àrea.
/clean: esborra tots els identificadors definits.
/save id: ha de guardar un skyline definit amb el nom id.sky.
/load id"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def llegir(update, context):
    msg = update.message.text
    print(msg)

    input_stream = InputStream(msg)
    lexer = SkyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = SkyParser(token_stream)
    tree = parser.root()
    # print(tree.toStringTree(recog=parser))

    dict = context.user_data
    visitor = TreeVisitor(dict)
    # el diccionari es passa per referencia per tant dict se li haura afegit el resultat de l'arbre
    visitor.visit(tree)
    # print(dict)

    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('skyline.png', 'rb'))
    f = open('area_alcada.txt', 'r')
    msg = f.read()
    # for lines in f.readlines():
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)
    f.close()

# handling callbacks functions to the commands

TOKEN = open("token.txt").read().strip()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', autor))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.text, llegir))

updater.start_polling()

# suposem que els retorna un objecte de la classe skyline
