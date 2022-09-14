#ATM Simulation by PG

import csv


fop = open(r"D:\Python\Newpath\ATM by PG\data.csv","r")
csv_reader = csv.reader(fop)
L=[]
for i in csv_reader:
	L.append(i)

users = []
num = len(L)
for i in range(1,num):
	s=L[i][0]
	users.append(s)
pins = []
for i in range(1,num):
	p=L[i][1]
	pins.append(p)

amounts = []
for i in range(1,num):
	q=L[i][2]
	amounts.append(int(q))

nos100 = int(L[1][4])
nos200 = int(L[1][5])
nos500 = int(L[1][6])
nos2000 = int(L[1][7])
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		for i in range(3):
			if user == users[i]:
				n=i
		break
	else:
		print('----------------')
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		print('----------------')



print('------------------')
print('******************')
for i in range(3,0,-1):
	pin = input('PLEASE ENTER PIN: ')
	print('******************')
	print('------------------')
	if pin == pins[n]:
		break
	else:
		print(f"Incorrect pin, {i} chance Left")
else:
	print("Thanks for using our service")
	exit()
	



	

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')

# Main Block
count = 0
while count==0 :
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDeposit__(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'INR ON YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		a = int(input("Enter the denomination (100/200/500/2000) : "))
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		
		if a==100:
			b = cash_out//100
			print('*********************************************')
			print('---------------------------------------------')
			if cash_out%100 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			elif cash_out > amounts[n]:
				print('-----------------------------')
				print('*****************************')
				print('YOU HAVE INSUFFICIENT BALANCE')
				print('*****************************')
				print('-----------------------------')
			elif nos100<b:
				print('-----------------------------')
				print('*****************************')
				print('DONT HAVE ENOUGH CASH')
				print('*****************************')
				print('-----------------------------')

			else:
				amounts[n] = amounts[n] - cash_out
				nos100 = nos100 - b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		elif a == 200:
			b = cash_out//200
			print('*********************************************')
			print('---------------------------------------------')
			if cash_out%200 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 200 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			elif cash_out > amounts[n]:
				print('-----------------------------')
				print('*****************************')
				print('YOU HAVE INSUFFICIENT BALANCE')
				print('*****************************')
				print('-----------------------------')
				
			elif nos200<b:
				print('-----------------------------')
				print('*****************************')
				print('DONT HAVE ENOUGH CASH')
				print('*****************************')
				print('-----------------------------')

			else:
				amounts[n] = amounts[n] - cash_out
				nos200 = nos200 - b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		elif a==500:
			b = cash_out//500
			print('*********************************************')
			print('---------------------------------------------')
			if cash_out%500 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 500 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			elif cash_out > amounts[n]:
				print('-----------------------------')
				print('*****************************')
				print('YOU HAVE INSUFFICIENT BALANCE')
				print('*****************************')
				print('-----------------------------')
			
			elif nos500<b:
				print('-----------------------------')
				print('*****************************')
				print('DONT HAVE ENOUGH CASH')
				print('*****************************')
				print('-----------------------------')
			else:
				amounts[n] = amounts[n] - cash_out
				nos500 = nos500 - b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		elif a==2000:
			b = cash_out//2000
			print('*********************************************')
			print('---------------------------------------------')
			if cash_out%2000 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 2000 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			elif cash_out > amounts[n]:
				print('-----------------------------')
				print('*****************************')
				print('YOU HAVE INSUFFICIENT BALANCE')
				print('*****************************')
				print('-----------------------------')
			elif nos2000<b:
				print('-----------------------------')
				print('*****************************')
				print('DONT HAVE ENOUGH CASH')
				print('*****************************')
				print('-----------------------------')
			else:
				amounts[n] = amounts[n] - cash_out
				nos2000 = nos2000 - b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		else:
			print("Wrong Denomination")
			

			
	elif response == 'd':
		a = int(input("Enter the denomination (100/200/500/2000) : "))
		cash_in = int(input('ENTER AMOUNT YOU WOULD LIKE TO DEPOSIT : '))
		if a==100:
			b = cash_in//100
			print('*********************************************')
			print('---------------------------------------------')
			if cash_in%100 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 100 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			else:
				amounts[n] = amounts[n] + cash_in
				nos100 = nos100 + b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		elif a == 200:
			b = cash_in//200
			print('*********************************************')
			print('---------------------------------------------')
			if cash_in%200 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 200 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			else:
				amounts[n] = amounts[n] + cash_in
				nos200 = nos200 + b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		elif a==500:
			b = cash_in//500
			print('*********************************************')
			print('---------------------------------------------')
			if cash_in%500 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 500 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			else:
				amounts[n] = amounts[n] + cash_in
				nos500 = nos500 + b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		elif a==2000:
			b = cash_in//2000
			print('*********************************************')
			print('---------------------------------------------')
			if cash_in%2000 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 2000 INR NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
			else:
				amounts[n] = amounts[n] + cash_in
				nos2000 = nos2000 - b
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
				print('***********************************')
				print('-----------------------------------')
		else:
			print("Wrong Denomination")
	elif response == 'p':
		print('-----------------------------')
		print('*****************************')
		new_pin = input('ENTER A NEW PIN : ')
		print('*****************************')
		print('-----------------------------')
		if new_pin != pins[n] and len(new_pin) == 4:
			print('------------------')
			print('******************')
			new_ppin = input('CONFIRM NEW PIN : ')
			print('*******************')
			print('-------------------')
			if new_ppin != new_pin:
				print('------------')
				print('************')
				print('PIN MISMATCH')
				print('************')
				print('------------')
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:
			print('-------------------------------------')
			print('*************************************')
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('*************************************')
			print('-------------------------------------')
	elif response == 'q':
		count=1
		print("Thanks for using our service")
		total_money = 100*nos100 + 200*nos200 + 500*nos500 + 2000*nos2000
		fos = open(r"D:\Python\Newpath\ATM by PG\data.csv","w",newline="")
		s=csv.writer(fos)
		L1=[users[0],str(pins[0]),str(amounts[0]),"",str(nos100),str(nos200),str(nos500),str(nos2000),str(total_money)]
		s.writerow(L[0])
		s.writerow(L1)
		m=len(users)
		for i in range(1,m):
			L2=[users[i],str(pins[i]),str(amounts[i])]
			s.writerow(L2)
		fos.close()
		print("Data Updated")
		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')
		








