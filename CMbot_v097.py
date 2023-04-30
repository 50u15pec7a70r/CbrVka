from datetime import datetime

#import telebot
import random
import time
import re
import string
import pymorphy2 

# ====================================================================
# Remove special symbols and punctuations
# ====================================================================
def remove_punctuation(lText):
       translator = str.maketrans('', '', string.punctuation)
       return lText.translate(translator)

# ====================================================================
# Normalize Russian 
# ====================================================================
MorphAnalisys = pymorphy2.MorphAnalyzer()
def normalize_R (lText):
    lOutText = []
    lWords = lText.split()
    for lWord in lWords:
        lOutText.append(MorphAnalisys.parse(lWord)[0].normal_form)
    return ' '.join(lOutText)

# ====================================================================
# Loggin to file
# ====================================================================
logFileName = 'logs/mTB-['+ str(datetime.fromtimestamp(time.time())).translate({ord(i): None for i in '-:.'}) +'].log'
def log_print(message_to_print, log_file = logFileName):
    print(message_to_print)
    with open(log_file, 'a') as of:
        of.write(message_to_print + '\n')

# ====================================================================
# Bot secret
# ====================================================================
# Here goes --> BotKey.py
import BotKey
bot = BotKey.lBot

# ====================================================================
# Global default Variables
# ====================================================================
gBotVersion = '0.97'

gbotName = 'comradeMbot'
gbotNameID = 5694562479

gGOD = 'D3AD50u1'
gGODID = 68864580

gADMINz = []
gADMINzID = []

gNIGGERz = []
gNIGGERzID = []

gBotShutUp = 'No'
gBotSeek = 'No'
gBotSniff = 'No'
gBotShow = 'No'
gBotSniff2Chat = 'No'
gScreamPortion = 0.6
gBotAnswerRate = 0.95
gBotChats = []

# ====================================================================
# Statistics initialization
# ====================================================================
gBotStartTime = time.time()
gBotSessionTime  = time.time()
gBotSessionMaxUpTime = 0
gBotRestartCount = 0
gBotShutUpCount = 0
gBotSessionMessageCount = 0
gBotSessionCommandCount = 0
gBotSessionMaxMessageLen = 0
gBotSessionAnsweredMessagesCount = 0
gChatTopPosterName = ''
gChatTopPosterLevel = 0

#================================================
# Configuration and Status tables Structure
#================================================
gChatConfigs = {'ChatID':[], 'Seek':[], 'Sniff':[], 'Show':[], 'Sniff2Chat':[],'ShutUp':[] , 'ScreamLevel':[], 'AnswerRate':[], 'ADMINz': [], 'ADMINzID': [], 'NIGGERz': [], 'NIGGERzID': [] }
gChatSpamControl = {'ChatID':[], 'MessageUserID':[], 'MessageTimeStamp':[] }
gChatStatuses = {'ChatID':[], 'SChatMessageCount':[], 'SChatCommandCount':[], 'SChatMaxMessageLen':[], 'SChatAnsweredMessagesCount':[], 'ChatTopPosterName':[], 'ChatTopPosterLevel':[] }

# ====================================================================
# Dictionaries
# ДОЛЖНО БЫТЬ МИНИМУМ 2 КЛЮЧА НА КАЖДЫЙ НАБОР ОТВЕТОВ!
# ====================================================================

# Here goes --> MainDictionary.py
import MainDictionary
gDictionary = MainDictionary.lDictionary

# ====================================================================
# Словарь для огнемёта
# ====================================================================
gBadDictionary = [
    'Пошёл нахуй!',
    'Ты тут не нужен!',
    'ЗАТКНИСЬ!'
    ]

# ====================================================================
# Словарь ответов на кричалки
# ====================================================================
gScreamDictionary = [
    'Не надо кричать, и так видно, что ты идиот!',
    'Позовите админов, тут опять больной шалит!',
    'Почему все кричат, почему нельзя общаться спокойно?'
    ]

# ====================================================================
# Help Description
# ====================================================================
gHelpDesc = [
    'Команды доступны только админам и хозяину бота.\n'
    'Не все команды доступны админам.\n\n'
    ' /бот помоги - вывести это сообщение\n'
    ' /бот статус - вывести статистику\n'
    ' /бот заткнись - заставить бота замолчать\n'
    ' /бот голос - разрешить боту болтать\n'
    ' /бот кто [ты | хозяин | админ] - имена, явки, пароли\n'
    ' /бот посчитай [админов] - сколько админов у бота\n'
    ' /бот кого наказали - узнать кого бот гнобит\n'
    ' /бот накажи %username% - добавить в список наказанных\n'
    ' /бот прости [%username% | всех] - убрать из наказанных [всех]\n'
    ' /бот слушайся %username% - добавить админа\n'
    ' /бот разжалуй [%username% | всех] - исключить админа [всех админов]\n'
    ' /бот фильтруй (0;1] - настроить уровень реакции\n'
    ' /бот анонсируй - бот анонсирует себя во всех активных чатах\n'
    ' /бот ищи - бот идентифицирует автора пересланного сообщения\n'
    ' /бот покажи - бот показывает структуру следующего сообщения от запросившего\n'
    ' /бот следить [начинай | прекращай] [тут] - бот идентифицирует авторов сообщений из чата и отправляет информацию в чат или в личку\n'
    ' /бот дай доступ - tbd\n'
    ]

# ====================================================================
# About
# ====================================================================
gBotDesc = [
    'Бот является pet-проектом и развивается по мере возможностей\n'
    'Основные функции бота:\n'
    ' - реакции на ключевые слова и пользователей\n'
    ' - сбор общей статистики [по чатам]\n'
    ' - доставление веселья\n'
    ' - автоматизации реакции на отмеченных пользователей\n'
    ' - не любит, когда шумят\n'
    '\n'
    'Ближайшие планы:\n'
    ' - добавить spam-контроль\n'
    ' - прикрутить использование БД\n'
    '\n'
    'Бот пишется факультативно, в меру способностей и желания.\n'
    'В работе бота используются непроверенные решения, запрещённые технологии, а также грязные хаки и hardcoded features (конечно Же нет).\n'
    'У бота есть скрытые пасхалки (это точно).\n'
    'В настоящий момент бот управляется полностью за счёт переменных, все накопленные настройки теряются при полном перезапуске (но не рестарте сессии).\n'
    'Если бот вас обидел, то возможно вы это заслужили.\n'
    '\n'
    'N.B. Бот не хранит и не собирает историю сообщений из чатов, ваши данные не передаются за пределы ноутбука.\n'
    '\n'
    'Если вы хотите что-то предложить, то имеет смысл обратиться к автору -> @D3AD50u1\n'
    ]

# ====================================================================
# Cоздаём новую настроечную таблицу для обнаруженного чата
# ====================================================================
def create_new_chat_config (lMessage):
    global gChatConfigs
    
    global gBotShutUp
    global gNIGGERz
    global gNIGGERzID
    global gADMINz
    global gADMINzID
    global gScreamPortion
    global gBotAnswerRate
    global gBotSeek
    global gBotSniff
    global gBotShow
    global gBotSniff2Chat
    
    gChatConfigs ['ChatID'].append (lMessage.chat.id)
    gChatConfigs ['ShutUp'].append (gBotShutUp)
    gChatConfigs ['ScreamLevel'].append(gScreamPortion)
    gChatConfigs ['AnswerRate'].append(gBotAnswerRate)
    gChatConfigs ['ADMINz'].append([])
    gChatConfigs ['ADMINzID'].append([])
    gChatConfigs ['NIGGERz'].append([])
    gChatConfigs ['NIGGERzID'].append([])
    gChatConfigs ['Seek'].append (gBotSeek)
    gChatConfigs ['Sniff'].append (gBotSniff)
    gChatConfigs ['Show'].append (gBotShow)
    gChatConfigs ['Sniff2Chat'].append (gBotSniff2Chat)
    
    # добавляем значения по умолчанию, наш новый чат -> последний
    lInd = len (gChatConfigs ['ChatID']) - 1
    for lListElement in gADMINz :
        gChatConfigs ['ADMINz'][lInd].append (lListElement)
    for lListElement in gADMINzID :
        gChatConfigs ['ADMINzID'][lInd].append (lListElement)
    for lListElement in gNIGGERz :
        gChatConfigs ['NIGGERz'][lInd].append (lListElement)
    for lListElement in gNIGGERzID :
        gChatConfigs ['NIGGERzID'][lInd].append (lListElement)
    
    msg2logprint = str(datetime.fromtimestamp(time.time())) + ' Новый чат [ID: ' + str (lMessage.chat.id) + ' ], всего чатов известно : ' + str(len (gChatConfigs ['ChatID']))
    log_print (msg2logprint)

# ====================================================================
# Функция-заглушка на скуку
# ====================================================================
def bot_melancholy_pipeline(lMessage):
    bot.send_message(lMessage.chat.id, "Где люди?")
    
# ====================================================================
# Команда помоги
# ====================================================================
def bot_command_help (lCommand):
    global gHelpDesc
    
    lIndex = 0
    while lIndex < len (gHelpDesc) :
        bot.reply_to(lCommand, gHelpDesc [lIndex])
        #bot.send_message(lCommand.chat.id, gHelpDesc [lIndex])
        lIndex +=1

# ====================================================================
# Команда /бот заткнись
# ====================================================================
def bot_command_shutup (lCommand):
    global gBotShutUpCount
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            if gChatConfigs['ShutUp'] [lIndex] == 'No' :
                gChatConfigs['ShutUp'] [lIndex] = 'Yes'
                gBotShutUpCount += 1
                break
            else :
                bot.reply_to(lCommand, "Да молчу я уже!")
        lIndex += 1

# ====================================================================
# Команда /бот голос
# ====================================================================
def bot_command_voice (lCommand):
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            if gChatConfigs['ShutUp'] [lIndex] == 'Yes' :
                gChatConfigs['ShutUp'] [lIndex] = 'No'
                bot.reply_to(lCommand, "Спасибо! Теперь я всё вам выскажу!")
                break
            else :
                bot.reply_to(lCommand, "Я и так могу говорить!")
        lIndex += 1

# ====================================================================
# Команда /бот кто хозяин|админ|ты
# ====================================================================
def bot_command_who (lCommand, lCommandParam):
    global gGOD
    global gBotDesc
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
           lADMINz = gChatConfigs ['ADMINz'] [lIndex]
           lADMINzID = gChatConfigs ['ADMINzID'] [lIndex]
           break
        lIndex +=1
        
    if lCommandParam == 'хозяин' :
        bot.reply_to(lCommand, "Только " + gGOD + ", люблю его!")
    elif lCommandParam == 'админ' :
        if (len(lADMINz) == 0) and (len(lADMINzID) == 0) :
            bot.reply_to(lCommand, "Наших бояр ночью с форанями ищут. В этом чате их нет." )
        else:
            lNames = ''
            if len(lADMINz) > 0:
                lIn = 0
                while lIn < len (lADMINz):
                    lNames += str(lADMINz[lIn])
                    if lIn == (len (lADMINz)-1):
                        if len(lADMINzID) > 0:
                            lNames += ', '
                    else:
                        lNames += ', '
                    lIn += 1
            if len(lADMINzID) > 0:
                lIn = 0
                while lIn < len (lADMINzID):
                    lNames += 'ID:' + str(lADMINzID[lIn])
                    if lIn < (len (lADMINzID)-1):
                        lNames += ', '
                    lIn += 1
            bot.reply_to(lCommand, "В этом чате я слушаюсь "+ str(len(lADMINz)+len(lADMINzID))+": " + lNames )
    elif lCommandParam == 'ты' :
        lIndex = 0
        while lIndex < len (gHelpDesc) :
            bot.reply_to(lCommand, gBotDesc [lIndex])
            #bot.send_message(lCommand.chat.id, gHelpDesc [lIndex])
            lIndex +=1
    else:
        bot.reply_to(lCommand, "Вообще не ебу о ком ты.")

# ====================================================================
# Команда /бот посчитай админов
# ====================================================================
def bot_command_count (lCommand, lCommandParam):
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
           lADMINz = gChatConfigs ['ADMINz'] [lIndex]
           lADMINzID = gChatConfigs ['ADMINzID'] [lIndex]
           break
        lIndex +=1
    
    if lCommandParam == 'админов' :
        bot.reply_to(lCommand, "В этом чате у нас их " + str(len(lADMINz) + len(lADMINzID)) + " и я их люблю..." )
        time.sleep(2)
        bot.send_message(lCommand.chat.id, "Не очень.")
    else:
        bot.reply_to(lCommand, "Сам считай, я тебе калькулятор что ли?")

# ====================================================================
# Команда /бот кого наказали
# ====================================================================
def bot_command_banned (lCommand, lCommandParam):
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
           lNIGGERz = gChatConfigs ['NIGGERz'] [lIndex]
           lNIGGERzID = gChatConfigs ['NIGGERzID'] [lIndex]
           break
        lIndex +=1
        
    if lCommandParam == 'наказали' :
        if (len(lNIGGERz) == 0) and (len(lNIGGERzID) == 0) :
            bot.reply_to(lCommand, "В этом чате никого не наказали. Может пора?" )
        else:
            lNames = ''
            if len(lNIGGERz) > 0:
                lIn = 0
                while lIn < len (lNIGGERz):
                    lNames += str(lNIGGERz[lIn])
                    if lIn == (len (lNIGGERz)-1):
                        if len(lNIGGERzID):
                            lNames += ', '
                    else:
                        lNames += ', '
                    lIn += 1
                
            if len(lNIGGERzID) > 0:
                lIn = 0
                while lIn < len (lNIGGERzID):
                    lNames += 'ID:' + str(lNIGGERzID[lIn])
                    if lIn < (len (lNIGGERzID)-1):
                        lNames += ', '
                    lIn += 1
                    
            bot.reply_to(lCommand, "В этом чате наказаны " + str(len(lNIGGERz)+len(lNIGGERzID)) + ": " + lNames)
    else:
        bot.reply_to(lCommand, "Сам считай, я тебе калькулятор что ли?")

# ====================================================================
# Команда /бот накажи
# ====================================================================
def bot_command_addban (lCommand, lCommandWords):
    global gGOD
    global gGODID
    global gbotName
    global gbotNameID
    
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
           lNIGGERz = gChatConfigs ['NIGGERz'] [lIndex]
           lNIGGERzID = gChatConfigs ['NIGGERzID'] [lIndex]
           lADMINz = gChatConfigs ['ADMINz'] [lIndex]
           lADMINzID = gChatConfigs ['ADMINzID'] [lIndex]
           lFoundIndex = lIndex
           break
        lIndex +=1
    
    if (len(lCommandWords) < 3):
        bot.reply_to(lCommand, "А кого наказать?")
    else:
        if lCommandWords [2][0] == '@':
            #по имени
            lNameToBlock = re.sub("@", "", lCommandWords [2] )
            if (lNameToBlock  == gbotName):
                bot.reply_to(lCommand, "Боярин, очки проверь! Себя я пороть не буду!")
            elif (lNameToBlock  == gGOD):
                bot.reply_to(lCommand, "Сейчас тебе таких пиздов дам! Ишь что удумал, смерд!")
            elif (lNameToBlock in lADMINz) :
                bot.reply_to(lCommand, "Бояр пороть не велено!")
            else:
                if (lNameToBlock not in lNIGGERz) :
                    gChatConfigs ['NIGGERz'][lFoundIndex].append (lNameToBlock)
                    bot.reply_to(lCommand, lNameToBlock + " будет наказан в этом чате!")
                else :
                    bot.reply_to(lCommand, lNameToBlock + " уже наказан в этом чате!")
        else:
            #по ID
            try: 
                lIDToBlock = int(lCommandWords [2])              
                if (lIDToBlock == gbotNameID):
                    bot.reply_to(lCommand, "Боярин, очки проверь! Себя я пороть не буду!")
                elif (lIDToBlock == gGODID):
                    bot.reply_to(lCommand, "Сейчас тебе таких пиздов дам! Ишь что удумал, смерд!")
                elif (lIDToBlock in lADMINzID) :
                    bot.reply_to(lCommand, "Бояр пороть не велено!")
                else:     
                    if (lIDToBlock not in lNIGGERzID) :
                        gChatConfigs ['NIGGERzID'][lFoundIndex].append (lIDToBlock)
                        bot.reply_to(lCommand, 'ID:' + str(lIDToBlock) + " будет наказан!")
                    else :
                        bot.reply_to(lCommand, 'ID:' + str(lIDToBlock) + " уже есть в списке!")
            except:
                bot.reply_to(lCommand, 'Дай мне имя (начинаться с @) или ID (целочисленное). Другого я не понимаю.')

# ====================================================================
# Команда /бот дай
# ====================================================================
def bot_command_give (lCommand, lCommandWords):
    
    match lCommandWords [2].lower():
        case "доступ" :
            bot.reply_to(lCommand, "4CC355 D3#1ED")
            lMessageReq = '4CC355 request from Chat.ID: ' + str(lCommand.chat.id) + ' | User.ID: ' + str(lCommand.from_user.id)
            bot.send_message(gGODID, lMessageReq)
        case "пизды" :
            bot.reply_to(lCommand, "Это не по адресу!")
        case _ :
            bot.reply_to(lCommand, "Нет, самому надо!")
            
# ====================================================================
# Команда /бот слушайся
# ====================================================================    
def bot_command_promote (lCommand, lCommandWords):
    global gGOD
    global gGODID
    global gbotName
    global gbotNameID
    
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            lNIGGERz = gChatConfigs ['NIGGERz'] [lIndex]
            lNIGGERzID = gChatConfigs ['NIGGERzID'] [lIndex]
            lADMINz = gChatConfigs ['ADMINz'] [lIndex]
            lADMINzID = gChatConfigs ['ADMINzID'] [lIndex]
            iFoundIndex = lIndex
            break
        lIndex +=1
    
    if (lCommand.from_user.username == gGOD) or (lCommand.from_user.id == gGODID) :
        if (len(lCommandWords) < 3):
            bot.reply_to(lCommand, "А кого слушать?")
        else:
            if lCommandWords [2][0] == '@':
                #по имени
                lNameToListen = re.sub("@", "", lCommandWords [2] )
                if (lNameToListen  == gbotName):
                    bot.reply_to(lCommand, "Не по чину мне в боярах ходить. Не по чину!")
                elif (lNameToListen == gGOD):
                    bot.reply_to(lCommand, "Он хозяин!")
                elif (lNameToListen in lADMINz) :
                    bot.reply_to(lCommand, lNameToListen + " и так уже боярин, чего ж ему, псу, ещё надо?")
                else:
                    if (lNameToListen not in lNIGGERz) :
                        gChatConfigs ['ADMINz'][iFoundIndex].append (lNameToListen)
                        bot.reply_to(lCommand, "Чин пожаловал, теперь " + lNameToListen + " в этом чате боярин.")
                    else :
                        bot.reply_to(lCommand, lNameToListen + " наказан, нельзя ему быть боярином!")
            else:
                #по ID
                try: 
                    lIDToListen = int(lCommandWords [2])              
                    if (lIDToListen == gbotNameID):
                        bot.reply_to(lCommand, "Не по чину мне в боярах ходить. Не по чину!")
                    elif (lIDToListen == gGODID):
                        bot.reply_to(lCommand, "Он хозяин!")
                    elif (lIDToListen in lADMINzID) :
                        bot.reply_to(lCommand, 'ID:'+ str(lIDToListen) + " и так уже боярин, чего ж ему, псу, ещё надо?")
                    else:
                        if (lIDToListen not in lNIGGERzID) :
                            gChatConfigs ['ADMINzID'][iFoundIndex].append (lIDToListen)
                            bot.reply_to(lCommand, "Чин пожаловал, теперь ID:" + str(lIDToListen) + " в этом чате боярин.")
                        else :
                            bot.reply_to(lCommand, "ID:" + lIDToListen + " наказан, нельзя ему быть боярином!")
                except:
                    bot.reply_to(lCommand, 'Дай мне имя (начинаться с @) или ID (целочисленное). Другого я не понимаю.')
    else:
        bot.reply_to(lCommand, "You have no power here!")

# ====================================================================
# Команда /бот прости
# ==================================================================== 
def bot_command_unban (lCommand, lCommandWords):
    global gGOD
    global gGODID
    global gbotName
    global gbotNameID
    
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            lNIGGERz = gChatConfigs ['NIGGERz'] [lIndex]
            lNIGGERzID = gChatConfigs ['NIGGERzID'] [lIndex]
            iFoundIndex = lIndex
            break
        lIndex += 1

    if (len(lCommandWords) < 3):
        bot.reply_to(lCommand, "А кого простить-то?")
    else:
        if lCommandWords [2] == "всех" :
            if (lCommand.from_user.username == gGOD) or (lCommand.from_user.id == gGODID):
                gChatConfigs ['NIGGERz'] [iFoundIndex].clear()
                gChatConfigs ['NIGGERzID'] [iFoundIndex].clear()
                bot.reply_to(lCommand, "Прощаю в этом чате всех!")
                time.sleep(2)
                bot.send_message(lCommand.chat.id, "Ох и добрый ты, хозяин. Я бы не простил.")
            else :
                bot.reply_to(lCommand, "Извини, боярин, но тебе это не по чину.")
        else :
            if lCommandWords [2][0] == '@':
                lNameToUnBlock = re.sub("@", "", lCommandWords [2] ) 
                if (lNameToUnBlock in lNIGGERz):
                    gChatConfigs ['NIGGERz'] [iFoundIndex].remove(lNameToUnBlock)
                    bot.reply_to(lCommand, "Как знаешь, простил его...")
                else :
                    bot.reply_to(lCommand, "Нету такого. В списке не значится.")
            else:
                try: 
                    lIDToUnBlock = int(lCommandWords [2])              
                    if (lIDToUnBlock in lNIGGERzID):
                        gChatConfigs ['NIGGERzID'] [iFoundIndex].remove(lIDToUnBlock)
                        bot.reply_to(lCommand, "Как знаешь, простил его...")
                    else :
                        bot.reply_to(lCommand, "Нету такого. В списке не значится.")
                except:
                    bot.reply_to(lCommand, 'Дай мне имя (начинаться с @) или ID (целочисленное). Другого я не понимаю.')

# ====================================================================
# Команда /бот разжалуй
# ==================================================================== 
def bot_command_depromote (lCommand, lCommandWords):
    global gGOD
    global gGODID
    
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            lADMINz = gChatConfigs ['ADMINz'] [lIndex]
            lADMINzID = gChatConfigs ['ADMINzID'] [lIndex]
            iFoundIndex = lIndex
            break
        lIndex += 1
    
    if (len(lCommandWords) < 3):
        bot.reply_to(lCommand, "А кого разжаловать-то?")
    else:
        if lCommandWords [2] == "всех" :
            if (lCommand.from_user.username == gGOD) or (lCommand.from_user.id == gGODID):
                gChatConfigs ['ADMINz'] [iFoundIndex].clear()
                gChatConfigs ['ADMINzID'] [iFoundIndex].clear()
                bot.reply_to(lCommand, "Слово и дело государево! Админов в этом чате не осталось...")
                time.sleep(2)
                bot.send_message(lCommand.chat.id, "Только хозяин, только hardcore!")
            else :
                bot.reply_to(lCommand, "А по носу не дать?!")
        else :
            if lCommandWords [2][0] == '@':
                lNameToDone = re.sub("@", "", lCommandWords [2] ) 
                if (lNameToUnDone in lADMINz):
                    gChatConfigs ['ADMINz'] [iFoundIndex].remove(lNameToUnDone)
                    bot.reply_to(lCommand, "Разжалован! Теперь " + lNameToUnDone + " - простолюдин.")
                else :
                    bot.reply_to(lCommand, lNameToUnDone + " не числится среди бояр.")
            else:
                try: 
                    lIDToUnDone = int(lCommandWords [2])              
                    if (lIDToUnDone in lADMINzID):
                        gChatConfigs ['ADMINzID'] [iFoundIndex].remove(lIDToUnDone)
                        bot.reply_to(lCommand, "Вычеркнул его...")
                    else :
                        bot.reply_to(lCommand, "Нету такого. В списке бояр не значится.")
                except:
                    bot.reply_to(lCommand, 'Дай мне имя (начинаться с @) или ID (целочисленное). Другого я не понимаю.')

# ====================================================================
# Команда /бот фильтруй
# ====================================================================
def bot_command_filter (lCommand, lCommandWords) :
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            iFoundIndex = lIndex
            break
        lIndex += 1
    
    try :
        lAnswerRate = float(lCommandWords [2])
        if (lAnswerRate > 1) or (lAnswerRate == 0):
            bot.reply_to(lCommand, "Ты просишь невыполнимого.")
        else:
            gChatConfigs ['AnswerRate'] [lIndex] = lAnswerRate
            bot.reply_to(lCommand, "Принято для этого чата.")
    except:
        bot.reply_to(lCommand, 'Дай значение в пределах (0;1]. Другого я не понимаю.')
            
# ====================================================================
# Команда /бот статус
# ====================================================================
def bot_command_status(lCommand, lCommandWords) :
    global gBotStartTime 
    global gBotSessionTime
    global gBotRestartCount
    global gBotShutUpCount
    global gBotVersion
    global gBotSessionMessageCount
    global gBotSessionCommandCount
    global gBotSessionMaxMessageLen
    global gBotAnswerRate
    global gBotSessionAnsweredMessagesCount
    global gBotChats
    global gBotSessionMaxUpTime
   
    global gChatConfigs
    
    # извлекаем переменные из структуры
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            lBotShutUp = gChatConfigs ['ShutUp'] [lIndex]
            iFoundIndex = lIndex
            if lBotShutUp == 'No':
                lBotShutUp = 'Нет'
            else :
                lBotShutUp = 'Да'
        lIndex += 1
    
    lBotStartDateTime = datetime.fromtimestamp(gBotStartTime)
    lBotSessionTime = datetime.fromtimestamp(gBotSessionTime)
    
    lBotSessionUpTime = datetime.fromtimestamp(time.time()) - lBotSessionTime
    lBotSessionUpTimeInMunutes = int(round(lBotSessionUpTime.total_seconds() / 60))
    
    if (gBotRestartCount == 0) or (lBotSessionUpTimeInMunutes > gBotSessionMaxUpTime) :
        lBotSessionUpMaxTimeInMunutes = lBotSessionUpTimeInMunutes
    else :
        #lBotSessionUpTime = datetime.fromtimestamp(time.time()) - lBotSessionTime
        lBotSessionUpMaxTimeInMunutes = gBotSessionMaxUpTime
    
    lStat = []
    lStat.append (str('Версия бота: ' + gBotVersion + '\n'))
    lStat.append (str('Время запуска: ' + str(lBotStartDateTime) + '\n'))
    lStat.append (str('Файл журнала: ' + logFileName + '\n'))
    lStat.append (str(' Всего сбоев: ' + str(gBotRestartCount) + '\n'))
    lStat.append (str(' Самая длинная сессия (мин.): ' + str(lBotSessionUpMaxTimeInMunutes) + '\n'))
    lStat.append (str(' Замечено чатов: ' + str(len(gBotChats)) + '\n\n'))
    
    lStat.append (str('Текущая сессия запущена в: ' + str(lBotSessionTime)  + '\n'))
    lStat.append (str(' Продолжительность (мин.): ' + str(lBotSessionUpTimeInMunutes) + '\n'))
    lStat.append (str(' За текущую сессию (все чаты):\n'))
    lStat.append (str('  Текстовых сообщений замечено: ' + str(gBotSessionMessageCount) + '\n'))
    lStat.append (str('  Текстовых сообщений отвечено: ' + str(gBotSessionAnsweredMessagesCount) + '\n'))
    lStat.append (str('  Команд замечено: ' + str (gBotSessionCommandCount) + '\n'))
    lStat.append (str('  Бота просили заткнуться: ' + str (gBotShutUpCount) + '\n'))
    lStat.append (str('  Символов в самом длинном сообщении: ' + str (gBotSessionMaxMessageLen) + '\n\n'))

    lStat.append (str('Статус в этом чате:\n'))
    lStat.append (str(' Уровень реакции: ' + str (gChatConfigs ['AnswerRate'][iFoundIndex]) + '\n'))
    lStat.append (str(' Молчит: ' + (lBotShutUp) + '\n\n'))
    
    bot.reply_to(lCommand, ''.join(lStat) )

# ====================================================================
# Команда /бот анонсируй
# ====================================================================
def bot_command_anonce (lCommand, lCommandWords) :
    global gBotChats
    global gGOD
    global gBotVersion
    
    if (lCommand.from_user.username == gGOD) :
        for lChatID in gBotChats :
            bot.send_message(lChatID, "*** [U R SP34K1#' 2 B07 V3R$10# " + gBotVersion + "] ***")

# ====================================================================
# Команда /бот покажи
# ====================================================================
def bot_command_show (lCommand):
    global gChatConfigs
    
    # извлекаем переменные из структуры
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            iFoundIndex = lIndex
        lIndex += 1
        
    if (lCommand.from_user.username == gGOD) or (lCommand.from_user.id == gGODID) :
        if gChatConfigs ['Show'] [iFoundIndex] == 'No':
            gChatConfigs ['Show'] [iFoundIndex] = str(lCommand.from_user.id)
            bot.reply_to(lCommand,'Давай сообщение, я его выверну наизнанку.')
        else:
            if gChatConfigs ['Show'] [iFoundIndex] == str(lCommand.from_user.id) :
                bot.reply_to(lCommand,'Я жду. Дай мне сообщение.')
            else :
                bot.reply_to(lCommand,'Я пока занят. Подожди своей очереди.')
    else:
        bot.reply_to(lCommand,'Не положено.')

# ====================================================================
# Команда /бот ищи
# ====================================================================
def bot_command_seek (lCommand):
    global gChatConfigs
    
    # извлекаем переменные из структуры
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            iFoundIndex = lIndex
        lIndex += 1
        
    if gChatConfigs ['Seek'] [iFoundIndex] == 'No':
        gChatConfigs ['Seek'] [iFoundIndex] = str(lCommand.from_user.id)
        bot.reply_to(lCommand,'Давай сообщение, скажу кто автор.')
    else:
        if gChatConfigs ['Seek'] [iFoundIndex] == str(lCommand.from_user.id) :
            bot.reply_to(lCommand,'Я и так ищу. Дай мне чужое сообщение.')
        else :
            bot.reply_to(lCommand,'Я пока занят. Подожди своей очереди.')

# ====================================================================
# Команда /бот следить начинай|прекращай
# ====================================================================
def bot_command_sniff (lCommand, lCommandWords):
    global gChatConfigs
    
    # извлекаем переменные из структуры
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lCommand.chat.id :
            iFoundIndex = lIndex
        lIndex += 1
    
    if (len(lCommandWords) < 3):
        bot.reply_to(lCommand, "Шта?")
    else:
        if lCommandWords [2] == "начинай" :
            if gChatConfigs ['Sniff'] [iFoundIndex] == 'No':
                gChatConfigs ['Sniff'] [iFoundIndex] = str(lCommand.from_user.id)
                
                if len (lCommandWords) >= 4 :
                    if lCommandWords [3] == "тут" :
                        gChatConfigs ['Sniff2Chat'] [iFoundIndex] = 'Yes'
                        bot.reply_to(lCommand,'Слежу. Отвечать буду тут.')
                else :
                    bot.reply_to(lCommand,'Слежу. Буду отвечать в личку.')
            else:               
                
                if gChatConfigs ['Sniff'] [iFoundIndex] == str(lCommand.from_user.id) :
                    if gChatConfigs ['Sniff2Chat'] [iFoundIndex] == "No" :
                        bot.reply_to(lCommand,'Уже слежу. Ищи мои пояснения в чате.')
                    else :
                        bot.reply_to(lCommand,'Уже слежу. Ищи мои ответы в личке.')
                else :
                    bot.reply_to(lCommand,'Уже слежу. Подожди своей очереди.')

        elif lCommandWords [2] == "прекращай" :
            if gChatConfigs ['Sniff'] [iFoundIndex] == str(lCommand.from_user.id):
                gChatConfigs ['Sniff'] [iFoundIndex] = 'No'
                if gChatConfigs ['Sniff2Chat'] [iFoundIndex] == "No" :
                    bot.reply_to(lCommand,'Прекратил.')
                else :
                    gChatConfigs ['Sniff2Chat'] [iFoundIndex] = "No"
                    bot.reply_to(lCommand,'Прекратил.')
            elif gChatConfigs ['Sniff'] [iFoundIndex] == 'No':
                bot.reply_to(lCommand,'Ничего плохого не делаю, починяю примус.')
            else:
                bot.reply_to(lCommand,'Я занят, подожди своей очереди.')
        else :
            bot.reply_to(lCommand, "Шта?")

# ====================================================================
# Обработка команд
# ====================================================================
def bot_command_pipeline (lCommand):

    lCommandWords = lCommand.text.split() # разбить на слова
    
    # заглушка на /бот
    if len (lCommandWords) < 2 :
        bot.reply_to(lCommand, "Я не пониматЪ!")
        return
    
    #lCWs = lCommand.text.lower().split() # разбить на слова с понижением региста
    
    match lCommandWords [1].lower():
        case "помоги" :
            bot_command_help (lCommand)
            
        case "заткнись" :
            bot_command_shutup (lCommand)
            
        case "голос" :
            bot_command_voice (lCommand)
            
        case "кто" :
            bot_command_who (lCommand, lCommandWords [2].lower())
            
        case "посчитай" :
            bot_command_count (lCommand, lCommandWords [2].lower())
                
        case "кого" :
            bot_command_banned (lCommand, lCommandWords [2].lower())
            
        case "накажи" :
            bot_command_addban (lCommand, lCommandWords)

        case "дай" :
            bot_command_give (lCommand, lCommandWords)

        case "слушайся" :
            bot_command_promote (lCommand, lCommandWords)

        case "прости" :
            bot_command_unban (lCommand, lCommandWords)
        
        case "разжалуй" :
            bot_command_depromote (lCommand, lCommandWords)
            
        case "статус" :
            bot_command_status (lCommand, lCommandWords)
            
        case "фильтруй" :
            bot_command_filter (lCommand, lCommandWords)
        
        case "анонсируй" :
            #bot.reply_to(lCommand, lCommand.from_user.id)
            bot_command_anonce (lCommand, lCommandWords)
        
        case "ищи" :
            #bot.reply_to(lCommand, lCommand.from_user.id)
            bot_command_seek (lCommand)
        
        case "следить" :
            #bot.reply_to(lCommand, lCommand.from_user.id)
            bot_command_sniff (lCommand, lCommandWords)
            
        case "покажи" :
            #bot.reply_to(lCommand, lCommand.from_user.id)
            bot_command_show (lCommand)

        case _: #unknown word
            bot.reply_to(lCommand, "Я не пониматЪ!")

# ====================================================================
# ОГНЕМЁТ (пока работает по словарю)
# ====================================================================
def bot_torture_pipeline (lMessage):
    global gBadDictionary
    
    random.seed(None,2)
    bot.reply_to(lMessage, gBadDictionary[ random.randrange(len(gBadDictionary) ) ])

# ====================================================================
# Реакция на КРИКИ
# ====================================================================
def bot_check_scream (lMessage) :
    global gScreamDictionary
    global gChatConfigs
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lMessage.chat.id :
            iFoundIndex = lIndex
            break
        lIndex += 1
    
    random.seed(None,2)
    
    lUpperCase = sum( 1 for lC in lMessage.text if lC.isupper() )
    lPortion = lUpperCase / len(lMessage.text)
    
    if (len(lMessage.text) > 1) and (lPortion > gChatConfigs ['ScreamLevel'] [iFoundIndex]) :
        bot.send_message(lMessage.chat.id, gScreamDictionary [random.randrange( len (gScreamDictionary))])

# ====================================================================
# Обработка текстовых сообщений из чата
# ====================================================================
def bot_message_pipeline (lMessage):
    
    global gDictionary
    global gBotAnswerRate
    global gBotSessionAnsweredMessagesCount
    global gBotSessionMessageCount
    
    lMessageAllWords = normalize_R(remove_punctuation(lMessage.text.lower()))
    lMessageWords = lMessageAllWords.split()
    
    msg2logprint = str(datetime.fromtimestamp(time.time())) + ' Слова в сообщении: '+ str (lMessageWords)
    log_print (msg2logprint)
    
    lMFoundWords = []
    
    random.seed(None,2)
    lIndex = 0
    lAnswered = 0
    lFoundWords = 0
    
    # Ищем ключевые слова в сообщении, формируе список найденных слов
    while lIndex < len (lMessageWords):
        for lKeys, lV in gDictionary.items ():
            lI = 0
            while lI < len (lKeys):
                if lMessageWords [lIndex] == lKeys[lI] :
                    lFoundWords +=1
                    lMFoundWords.append(lMessageWords [lIndex])
                    lI +=1
                else:
                    lI +=1
        lIndex +=1
    
    if len (lMFoundWords) :
        # Делаем словарь слов с указанием количества
        lWFCount = {lWF: lMessageAllWords.count(lWF) for lWF in lMFoundWords}
        
        lWFMax = lWFCount.values() # список только из значений количеств
        lWFMaxCount = max(lWFMax)  # Наибольшее из совпадений

        # Делаем список слов, у которых максимальное количество повторений
        lWFAnsw = [k for k, lValue in lWFCount.items() if lValue == lWFMaxCount ]
        
        # Формируем список ответов для всех повторяющихся слов
        lInDX = 0
        lListOfAnswers = []
        while lInDX < len (lWFAnsw) :
            for lKeys, lV in gDictionary.items ():
                if lWFAnsw[lInDX] in lKeys :
                    lLOfAs = next((v for k, v in gDictionary.items() if (lKeys == k) or (isinstance(k,tuple) and lKeys in k)), None)
            lListOfAnswers.extend (lLOfAs)
            lInDX += 1
        
        msg2logprint = str(datetime.fromtimestamp(time.time())) + ' Слова с большим весом: ' + str(lWFAnsw)
        log_print (msg2logprint)

        if gBotAnswerRate > (gBotSessionAnsweredMessagesCount/gBotSessionMessageCount):
            gBotSessionAnsweredMessagesCount +=1
            bot.reply_to(lMessage, lListOfAnswers [random.randrange( len (lListOfAnswers))])
        else :
            msg2logprint = str(datetime.fromtimestamp(time.time()))+ ' Слишком много болтаю, помолчу...'
            log_print (msg2logprint)

    else :
        msg2logprint = str(datetime.fromtimestamp(time.time())) + ' Я не вижу знакомые слова!'
        log_print (msg2logprint)


# ====================================================================
##@bot.message_handler(content_types=['text', 'document', 'audio'])
# ====================================================================
# TEXT MESSAGE HANDLER ++
# ====================================================================
@bot.message_handler(content_types=['text'])

def get_text_messages(lMessage):     
    global gGOD
    global gGODID
    global gBotSessionMessageCount
    global gBotSessionCommandCount
    global gBotSessionMaxMessageLen
    global gBotChats
    global gChatConfigs
    
    msg2logprint = str(datetime.fromtimestamp(time.time())) + ' | Chat.ID: ' + str(lMessage.chat.id) + ' | User.ID: ' + str(lMessage.from_user.id) + ' | Message: ' + str(lMessage.text)
    log_print (msg2logprint)
    
    if lMessage.chat.id not in gBotChats :
        gBotChats.append (lMessage.chat.id)
        create_new_chat_config (lMessage)
    
    lIndex = 0
    while lIndex < len (gChatConfigs ['ChatID']) :
        if gChatConfigs ['ChatID'] [lIndex] == lMessage.chat.id :
            lNIGGERz = gChatConfigs ['NIGGERz'] [lIndex]
            lNIGGERzID = gChatConfigs ['NIGGERzID'] [lIndex]
            lADMINz = gChatConfigs ['ADMINz'] [lIndex]
            lADMINzID = gChatConfigs ['ADMINzID'] [lIndex]
            iFoundIndex = lIndex
            break
        lIndex +=1
    
    lIsForward = 0
    if lMessage.forward_from != None: # проверяем было ли сообщение переслано
        lIsForward = 1
        
    if gChatConfigs ['Seek'] [iFoundIndex] == str(lMessage.from_user.id): # Ищем? Проверяем, кто дал команду, только ему отвечаем.
        if lIsForward:
            lNameText = ''
            lNameText += 'First name: ' + str(lMessage.forward_from.first_name) + '\n'
            lNameText += 'Last name: ' + str(lMessage.forward_from.last_name) + '\n'
            lNameText += 'Username: ' + str(lMessage.forward_from.username) + '\n'
            lNameText += 'User ID: ' + str(lMessage.forward_from.id) + '\n'
            bot.send_message(lMessage.chat.id, lNameText)
            gChatConfigs ['Seek'] [iFoundIndex] = 'No'
    
    if gChatConfigs ['Show'] [iFoundIndex] == str(lMessage.from_user.id): # Ищем? Проверяем, кто дал команду, только ему отвечаем.
        bot.send_message(lMessage.chat.id, str(lMessage))
        gChatConfigs ['Show'] [iFoundIndex] = 'No'
    
    if lIsForward == 0 : # не реагируем на пересланные сообщения
        lMessageWords = lMessage.text.lower().split() # разбить на слова
        
        if lMessageWords[0] == '/бот' :
            gBotSessionCommandCount += 1 #count commands
            if (lMessage.from_user.username in lADMINz) or (lMessage.from_user.username == gGOD) or (lMessage.from_user.id == gGODID) :
                bot_command_pipeline (lMessage)
            elif (lMessage.from_user.username in lNIGGERz) or (lMessage.from_user.id in lNIGGERzID):
                bot.reply_to(lMessage, "Как смеешь ты обращаться ко мне, проклятый!")
                bot_torture_pipeline (lMessage)
            else :
                bot.reply_to(lMessage, "Я тебя не знаю. Ты мне не коммандир!")
        else :
            gBotSessionMessageCount += 1 # count messages
            
            if gChatConfigs ['Sniff'] [iFoundIndex] != 'No' :
                lNameText = ''
                lNameText += 'First name: ' + str(lMessage.from_user.first_name) + '\n'
                lNameText += 'Last name: ' + str(lMessage.from_user.last_name) + '\n'
                lNameText += 'Username: ' + str(lMessage.from_user.username) + '\n'
                lNameText += 'User ID: ' + str(lMessage.from_user.id) + '\n'
                if gChatConfigs ['Sniff2Chat'] [iFoundIndex] == 'No':
                    bot.send_message(gChatConfigs ['Sniff'] [iFoundIndex], lNameText)
                else :
                    bot.send_message(lMessage.chat.id, lNameText)
            
            # извлекаем переменные из структуры
            lIndex = 0
            while lIndex < len (gChatConfigs ['ChatID']) :
                if gChatConfigs ['ChatID'] [lIndex] == lMessage.chat.id :
                    lBotShutUp = gChatConfigs ['ShutUp'] [lIndex]
                lIndex += 1
            
            if len (lMessage.text) > gBotSessionMaxMessageLen :
                gBotSessionMaxMessageLen = len (lMessage.text)
                
            if (lMessage.from_user.username in lNIGGERz) or (lMessage.from_user.id in lNIGGERzID) :
                bot_torture_pipeline (lMessage)
            elif lBotShutUp == 'No' :
                bot_check_scream (lMessage)
                bot_message_pipeline (lMessage)
        
# ====================================================================
# RUN SECTION
# ====================================================================
#bot.polling(none_stop=True, interval=0)

while True:
    try:
        msg2logprint = str(datetime.fromtimestamp(time.time())) + ' [ON]'
        log_print (msg2logprint)
        
        bot.send_message(gGODID, msg2logprint)
        msg2logFileName = 'Log file: ' + logFileName
        bot.send_message(gGODID, msg2logFileName)
        
        bot.polling(none_stop=True, interval=0)
    except:
        msg2logprint = str(datetime.fromtimestamp(time.time())) + ' [OFF]'
        log_print(msg2logprint)
        bot.send_message(gGODID, msg2logprint)
        
        gBotRestartCount +=1
        
        gBotSessionMessageCount = 0
        gBotSessionCommandCount = 0
        gBotSessionMaxMessageLen = 0
        gBotSessionAnsweredMessagesCount = 0
        gBotShutUpCount = 0
        
        lBotSessionTime = datetime.fromtimestamp(gBotSessionTime)
              
        lBotSessionUpTime = datetime.fromtimestamp(time.time()) - lBotSessionTime
        lBotSessionUpTimeInMunutes = int(round(lBotSessionUpTime.total_seconds() / 60))
        
        if lBotSessionUpTimeInMunutes > gBotSessionMaxUpTime :
            gBotSessionMaxUpTime = lBotSessionUpTimeInMunutes
        
        gBotSessionTime  = time.time()
        
        time.sleep(5)
        msg2logprint = str(datetime.fromtimestamp(time.time())) + ' [Restarting]'
        log_print(msg2logprint)
        bot.send_message(gGODID, msg2logprint)
