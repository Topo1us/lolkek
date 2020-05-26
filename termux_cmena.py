import os

# chmod 777 *
# cd /data/data/com.termux/files/usr/etc/bash.bashrc

def ty():
	if os.name == 'nt':
		_ = os.system ('cls')
	else:
		_ = os.system ('clear')

def kek():
	print ('''
Выполнено.......Termux Cod
Авторы..........WolFak...Topo1us
Сообщество Вк...https://vk.com/termux_cod
''')
	lol= input('Ваш ник: ')
	print('\n[1]\n[2]Белый\n[3]Бирюзовый\n[4]Зеленый\n[5]Желтый\n[6]Фиолетовый\n[7]Фиолетовый\n[8]Черный\n')
	
	color=input('Выберите цвет: ')

	if color=='1':
            to='34m' 
	if color=='2':
	    to='37m' 
	if color=='3':
	    to='36m' 
	if color=='4':
	    to='32m' 
	if color=='5':
	    to='33m' 
	if color=='6':
	    to='31m' 
	if color=='7':
	    to='35m' 
	if color=='8':
	    to='30m' 

	with open ('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w+') as file:
		try:
			file = file.write (r"PS1='\[\e[{0}\]{1}~# \[\e[0m\]'".format (to,lol))
			print ('Nick изменен :)')
		except:
			print ('если имя не изменено значит вы забыли ввести команду "chmod 777 *"')
ty()
kek()
