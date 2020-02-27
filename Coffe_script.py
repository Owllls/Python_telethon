from telethon import TelegramClient, events, sync
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from time import sleep
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.contacts import AddContactRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import UserStatusOffline
from telethon.tl.types import UserStatusRecently
from myModuls import ToFrtomFile as Fille
import random as Rang
from random import  randrange, randint
from telethon.tl.types import User as Person
from datetime import datetime, timedelta
from telethon.tl.functions.channels import GetParticipantsRequest

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon import TelegramClient, events, sync
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from time import sleep
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.contacts import AddContactRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import UserStatusOffline
from telethon.tl.types import UserStatusRecently
from myModuls import ToFrtomFile as Fille
import random as Rang
from random import  randrange, randint
from telethon.tl.types import User as Person
from datetime import datetime, timedelta


queryKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','א','ב','ג','ר','ק','ש','ד','ג','כ','ע','ח','ל','ו','ט','ו','ע','ז','י','ר','ח','ה','נ','ש','ס','נ','ו']
all_participants = []


api_id =  #place for your api_id
api_hash = '' #place for you api_hash

	 
last_date = None
chunk_size = 15000



client_1 = TelegramClient('session_Tus', api_id, api_hash) #Акк ариэль тус


ListOfLists = []
Users_from_ShikShukAll = set()
Target_Users = set()
Target_Groups = []
MyGroupUsers = set()
Final = set()
Users = set()
chats = [] # Тут хранятся мегагруппы
groups=[]  # Тут хранятся все группы

Time_border = datetime.today().date()

print(Time_border)
monthAgo = datetime(2020,1,13).date()
monthdelta = Time_border - monthAgo 
print(monthdelta)
Time_border = Time_border - monthdelta
print(Time_border)



              
def  makelist(users_fromGroup):	#Получает список пользователей и переберает их создавая новое типизированное множество
	
	for user in users_fromGroup:
		if type(user.status) == UserStatusOffline:
			if user.status.was_online.date() > Time_border:
				Users.add(user.username)
		elif type(user.status) == UserStatusRecently:
				Users.add(str(user.username))
	#Target_Groups.append(Users)

def  makeList(users_fromGroup):	#Получает список пользователей и переберает их создавая новое типизированное множество
    #print(type(users_fromGroup))
    #print("Ok")
	IntoUsers = [users_fromGroup.users]
	#print(type(IntoUsers))
	for i in IntoUsers:
		for user in i:
			if type(user.status) == UserStatusOffline:
				if user.status.was_online.date() > Time_border:
					Users.add(user.username)
			elif type(user.status) == UserStatusRecently:
				Users.add(str(user.username))
        #ListOfLists.append(Users)



client_1.start()
Users_from_ShikShukAll = set(Fille.ReadUserNames())
for i,b in enumerate(Users_from_ShikShukAll):
	print(i,b)
print(len(Users_from_ShikShukAll))







result = client_1.get_dialogs()
for i,dialog in enumerate(result):
    print(i," - " ,'{:>14}: {}'.format(dialog.id, dialog.title))
	
#print(result)
print(type(result))
chats.extend(result) #Тут хранятся все чаты
askUser = input("Only Megagroups? -Y ")

number_of_Groups = int(input('How much groups you want to Add '))

for i in range(number_of_Groups):
		i=0		 
		for group in groups:
			print(str(i) + '- ' + group.title)
			i+=1
		Target_group = result[int(input('Chose number of gropup '))]
		try:
			for key in queryKey:
				offset = 0
				limit = 10000
				limit=None
				makeList(client_1(GetParticipantsRequest(Target_group, ChannelParticipantsSearch(key), offset, limit=10000 ,hash=0)))
			makelist(client_1.get_participants(Target_group.title, aggressive = True))	#Передаем список следующему методу	#Передаем список следующему методу
		except Exception as e:
			print(type(e))
			print(e)
			continue
		    

	

		




    
print('Users lenght - ',len(Users))
print('My List lenght ',len(Users_from_ShikShukAll))
Final.update(Users- Users_from_ShikShukAll)
print('Final lenght  - '  ,len(Final))
Fille.Write_UserNames(Final)