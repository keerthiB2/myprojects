alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key=3
newmessage=''
message=input("please enter message:")

for character in  message:
	if character in  alphabet:
		position=alphabet.find(character)
		newposition=(position+key)%26
		
		newcharacter=alphabet[newposition]
		
		newmessage+=newcharacter
	elif character in  alphabet1:
		position=alphabet1.find(character)
		newposition=(position+key)%26
		
		newcharacter=alphabet1[newposition]
		
		newmessage+=newcharacter
		

	else:
		newmessage+=character
print("your msg is :",newmessage)
import requests
import json
def set_firebase(data1):
	data={'keerthi':data1}
	url1='https://sameer-cde0d.firebaseio.com/.json'
	r = json.dumps(data)
	to_database = json.loads(r)
	try:
		requests.patch(url = url1 , json = to_database)
	except Exception as e:
		print('internet not connected')
		return 0

set_firebase(newmessage)
