from telethon import TelegramClient, events, sync
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError
from time import sleep
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.contacts import AddContactRequest
from telethon.tl.functions.contacts import GetContactsRequest
from myModuls import ToFrtomFile as Fille
import random as Rang
from random import  randrange, randint
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import functions, types
from telethon.tl.functions.help import GetUserInfoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPeerChat


MyGroupName = 'Your_group_name'



api_id0 = #yourId
api_hash0 = 'yourhash'        
#place for another clients id\hash







client_a = TelegramClient('Name_of_session', api_id0, api_hash0)
#place for another clients objects
#client_1
#client_2
#client_3

#bots = [client_1,client_2,client_3] your bots

print("--------------------------------------STARTING------------------------------------------------")


client_a.start()
for i,bot in enumerate(bots):
    print(bot, "   ", i)
    bot.start()
    



repeat = int(input("How much times you want to repeat? "))

time = int(input("Pause between every bot? "))
time2 = int(input("Pause between every loop? "))




addBot_toGroups = False    
askUser = input("Add bots to Group? _ Y/N ")
if askUser == 'y' or askUser == 'Y':
    addBot_toGroups = True

print("You Choosing a file with Groups, which you need_")
GroupsList = Fille.ReadUserNames() # Выбираем нужный нам список пользователей-конкретной группы
RemovedUsers = []
j = 0
messages = client_a.get_messages(MyGroupName,limit = 10) #
for i,message in enumerate(messages):
    print("____________________________________")
    print(i, " -- " ,message.message)
num_message = int(input("Number of Message? _ "))#
message_id = messages[num_message].id
for i in range (repeat):
    message = None
    print("  You choosed: ", messages[num_message].message)
    print(type(messages[num_message]))
    sleep(2)  
    for bot in bots:
        if addBot_toGroups == True:
            bot(JoinChannelRequest(MyGroupName))
        messages = bot.get_messages(MyGroupName,limit = 100)
        for k in messages:
            if k.id == message_id:
                message = k
        for nb,group in enumerate(GroupsList):
            if addBot_toGroups == True:
                bot(JoinChannelRequest(group))
            try:
                entity = bot.get_entity(group)
                chatt = InputPeerChannel(entity.id,entity.access_hash)
                print("     Group     -        ",entity)
                bot.forward_messages(chatt,[message])
            except Exception as e:
                print(e)
                sleep(5)
                continue  
        print(' All Good: ')
        j = j + 1
        sleep(time)
    sleep(time2)	

