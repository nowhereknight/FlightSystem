import os, sys, time, getpass, random
def clearScreen():
	#Limpia la pantalla dependiendo del sistema operativo del que se trate
	if os.name == 'posix':
		os.system('clear')
	elif os.name == 'nt':
		os.system('cls')

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def convertToBST(sortedlist):
        if len(sortedlist)==0: return None
        mid=len(sortedlist)//2
        root=TreeNode(sortedlist[mid])
        root.left=convertToBST(sortedlist[:mid])
        root.right=convertToBST(sortedlist[mid+1:])
        return root
def descifrar(cadena):
    aux = ''
    for i in cadena:
        aux += chr(ord(i)-3)
    return aux

def cifrar(cadena):
    aux = ''
    for i in cadena:
        aux += chr(ord(i)+3)
    return aux

def Intercambiar(lista, x, y):
    aux = lista[x]
    lista[x] = lista[y]
    lista[y] = aux
    
def Partition(lista, start, end):
    piv = lista[start][2].split(":")
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and lista[left][2].split(":") <= piv:
            left+=1
        while lista[right][2].split(":") >= piv and right >= left:
            right-=1
        if right < left:
            done = True
        else:
            Intercambiar(lista, left, right)
    Intercambiar(lista, start, right)
    return right

def QuickSort(lista, start, end):
    if( start < end):
        pivot = Partition(lista, start, end)
        QuickSort(lista, start, pivot-1)
        QuickSort(lista, pivot+1, end)

########################################################################################
class fligth:
	def __init__(self, distance, departureTime, procedence, destination, name):
		self.to = None
		self.name=name
		self.distance=int(distance)
		self.departureTime=departureTime
		if self.distance > 250000:
			self.aircraft="AT-1200"
			self.firstClass=50
			self.economic=250
		elif 100000 < self.distance < 250000:
			self.aircraft="AT-1000"
			self.firstClass=40
			self.economic=160
		elif 50000 < self.distance < 100000:
			self.aircraft="AT-800"
			self.firstClass=20
			self.economic=80
		elif self.distance<50000:
			self.aircraft="AT-400"
			self.firstClass=10
			self.economic=30
class ticket:
	def __init__(self,vuelo,clase,precio, de, a, username):
		self.vuelo=vuelo
		self.clase=clase
		self.precio=precio
		self.de=de
		self.a=a
		self.username=username

	def getString(self):
		string="AEROMEX\nFlight information\n"+self.vuelo.name+"\t24/11/2017\n"
		string+="Origin: "+self.de+"\t\tDeparture time: "+self.vuelo.departureTime+"\tTerminal: "+str(random.randint(1,8))
		string+="\nDestination: "+self.vuelo.to+"\t\t\t\tSeat: "+chr(random.randint(65,70))+"-"+str(random.randint(1,self.vuelo.economic))
		string+="\n\nPassenger: "+self.username+"\t\tTicket number: "+str(random.randint(100,200))+" "+str(random.randint(10000,20000))
		string+="\nPassport Number: XXXXXXXXXXXXXXX\t\t$"+str(self.precio)+" MXN"
		return string


class fligths:
    def __init__(self):
        self.fligths={'CDMX': set(),
         'Los Angeles': set(),
         'Chicago': set(),
         'Nueva York': set(),
         'Tokio': set(),
         'Toronto': set(),
         'Paris': set(),
         'Madrid': set(),
         'Berlin': set(),
         'Oslo': set(),
         'Roma': set(),
         'Buenos Aires':set()}
        with open('fligths.txt') as file:
            for line in file:
                line=line.split("::")
                distance=int(line[3])
                departureTime=line[2]
                origin=line[0]
                destination=line[1]
                name=line[4]
                vuelo = fligth(distance,departureTime,origin,destination,name)
                vuelo.to = destination
                self.fligths[origin].add(vuelo)
        file.close()

    def displayFligths(self):
        string="Vuelo \t\tOrigen\t\tDestino\t\tHora de salida\n"
        for fligth in self.fligths:
            for f in self.fligths[fligth]:
                string+=f.name+": \t"
                if len(fligth)<10:
                    string += fligth+"\t\t"
                else:
                    string += fligth+"\t"
                if len(f.to)<10:
                    string+=f.to+"\t\t"+f.departureTime+"\n"
                else:
                    string+=f.to+"\t"+f.departureTime+"\n"
        print(string)

    def findPath(self, start, end, path=[], fligth=None):
        if fligth:
            path = path + [fligth]
        if start == end:
            return path
        if not self.fligths.__contains__(start):
             return None
        for fligth in self.fligths[start]:
            if fligth not in path:
                newpath = self.findPath(fligth.to, end, path, fligth)
                if newpath: 
                    return newpath
        return None

    def findPaths(self, start, end):
        stack = [(start, [])]
        while stack:
            (vertex, path) = stack.pop()
            for fligth in self.fligths[vertex] - set(path):
                if fligth.to == end:
                    yield path+[fligth]
                else:
                    stack.append((fligth.to, path + [fligth]))

    def findShortestPath(self, start, end):
        paths=self.findPaths(start, end)
        shortest=None
        if paths:
            for path in paths:
                if not shortest or len(path)<len(shortest):
                    shortest=path
        return shortest
#######################################################################################################################
def getUsers():
	with open('users.txt') as file:
		users = []
		for line in file:
			users.append(line.split("::"))
	file.close()
	return users

def getFligths():
	with open('fligths.txt') as file:
		fligths = []
		for line in file:
			fligths.append(line.split("::"))
	file.close()
	return fligths

def updateFligths():
	fligths=getFligths()
	QuickSort(fligths,0, len(fligths)-1)
	file = open("fligths.txt","w")
	for fligth in fligths:
		file.write(fligth[0]+"::"+fligth[1]+"::"+fligth[2]+"::"+fligth[3]+"::"+fligth[4]+"::\n")
	file.close()

def updateUsers():
	users=getUsers()
	users.sort(key=lambda x: x[1])
	file = open("users.txt","w")
	for user in users:
		file.write(user[0]+"::"+user[1]+"::"+user[2]+"::\n")
	file.close()

def addUser():
    try:
        user=input("Enter the name of the user you want to add: ")
        password=getpass.getpass("Enter the password: ")
        password_again=getpass.getpass("Enter the password again: ")
        user_type=int(input("What type of user do you want to create?\n1) Administrator\n2) Client \n"))
        if user_type==1:
            user_type="#"
        elif user_type==2:
            user_type="$"
        else:
            print("Please, enter a valid option")
            time.sleep(3)
            clearScreen()
            addUser()
        if password==password_again:
            file = open("users.txt","a")
            file.write(user_type+"::"+user+"::"+cifrar(password)+"::\n")
            file.close()
            updateUsers()
            print("The user ",user," has been created")
            time.sleep(3)
            clearScreen()
        else:
            print("Passwords don't match")
            addUser()
    except ValueError:
        print("Enter only valid options")
        user=password=password_again=user_type=None
        time.sleep(3)
        clearScreen()
        addUser()

def addFligth():
    try:
        lugares=[]
        for i in places:
            lugares.append([places[i],i])
        lugares.sort()
        name=input("Enter the flight code: ")
        print("Select the flight origin: ")
        for i in lugares:
            print(str(i[0])+" : "+i[1])
        origin=int(input())
        if origin>12 or origin<0:
            print("Enter only valid options")
            time.sleep(3)
            clearScreen()
            addFligth()
        origin=inv_places[origin]
        
        print("Select the destination: ")
        for i in lugares:
            print(str(i[0])+" : "+i[1])
        destination=int(input())
        destination=inv_places[destination]
        departure=input("Enter the departure time 'hh:mm' : ")
        distance=input("Enter the flight distance: ")
        file = open("fligths.txt","a")
        file.write(origin+"::"+destination+"::"+departure+"::"+distance+"::"+name+"::"+"\n")
        file.close()
        updateFligths()
        vuelos=None
        vuelos=fligths()
        clearScreen()
        print("Flight has been added succesfully")
    except ValueError:
        print("Enter only valid options")
        time.sleep(3)
        clearScreen()
        addFligth()

def getPaths(username):
	try:
		clearScreen()
		lugares=[]
		for i in places:
			lugares.append([places[i],i])
		lugares.sort()

		print("Welcome "+username)
		print("Please choose the origin of your flight")
		for i in lugares:
			print(str(i[0])+") "+i[1])
		origin=int(input())
		if origin>12 or origin<0:
			print("Enter a valid option")
			time.sleep(3)
			clearScreen()
			getPaths(username)
		origin=inv_places[origin]

		print("Select a destination: ")
		for i in lugares:
			print(str(i[0])+") "+i[1])
		destination=int(input())
		if destination>12 or destination<0:
			print("Enter a valid option")
			time.sleep(3)
			clearScreen()
			getPaths(username)
		destination=inv_places[destination]

		paths=list(vuelos.findPaths(origin,destination))
		paths.sort(key=len)
		if paths:
			i=1
			aux=origin
			string=""
			for path in paths:
				string+="Option "+str(i)+":\n"
				string+="Flight\tOrigin\t\tDestination\t\tDeparture time\n"
				for fligth in path:
					string+=fligth.name+"\t"
					if len(origin)<10:
						string += origin+"\t\t"
					else:
						string += origin+"\t"
					if len(fligth.to)<10:
						string+=fligth.to+"\t\t"+fligth.departureTime+"\n"
					else:
						string+=fligth.to+"\t"+fligth.departureTime+"\n"
					origin=fligth.to
				string+="\n"
				i+=1
				origin=aux
			print(string)
			j=int(input("Enter the option you want: "))
			if j>len(paths) or j<0:
				print("Enter a valid option")
				time.sleep(3)
				clearScreen()
				getPaths(username)
			path=paths[j-1]

			setPrices(path, aux, username)
		else:
			print("For the moment there are no available flights for that destination")
			time.sleep(2)
			clearScreen()
			getPaths(username)
	except ValueError:
		print("Enter only valid options")
		time.sleep(3)
		clearScreen()
		getPaths(username)

def setPrices(path, origin, username):
	try:
		print("The chosen option is: ")
		string="Flight\tOrigin\t\tDestination\t\tDeparture time\n"
		for fligth in path:
			string+=fligth.name+"\t"
			if len(origin)<10:
				string += origin+"\t\t"
			else:
				string += origin+"\t"
			if len(fligth.to)<10:
				string+=fligth.to+"\t\t"+fligth.departureTime+"\n"
			else:
				string+=fligth.to+"\t"+fligth.departureTime+"\n"
			origin=fligth.to
			string+="\n"
		print(string)
		tickets=[]
		for fligth in path:
			print("For the flight "+fligth.name+" de "+origin+" a "+fligth.to+", choose if you want first or economy class")
			if fligth.aircraft=="AT-1200":
				firstClass=1250
				economic=1000
			elif fligth.aircraft=="AT-1000":
				firstClass=700
				economic=500
			elif fligth.aircraft=="AT-800":
				firstClass=400
				economic=300
			elif fligth.aircraft=="AT-400":
				firstClass=300
				economic=200
			origin2=fligth.to
			print("The price of an economy class ticket is $"+str(economic)+".00\nThe price of a first class ticket is: $"+str(firstClass)+".00")
			clase=int(input("1) Primera clase \n2) Económica\n:"))
			if clase>2 or clase<0:
				print("Enter only a valid option")
				time.sleep(3)
				clearScreen()
				setPrices(path, origin, username)
			if clase==1:
				price=firstClass
				clase="First class"
				fligth.firstClass-=1
			elif clase==2:
				price=economic
				clase="Economy"
				fligth.economic-=1
			else:
				print("Enter the appropiate option")
				time.sleep(2)
				clearScreen()
				setPrices(path)
			boleto=ticket(fligth,clase,price,origin,fligth.to,username)
			tickets.append(boleto)
			origin=fligth.to
		displayTickets(tickets)
		saveTickets(tickets)
	except ValueError:
		print("Enter only valid options")
		time.sleep(3)
		clearScreen()
		setPrices(path, origin, username)

def displayTickets(tickets):
    clearScreen()   
    print("Thanks for choosing Aeromex. This is your flight information and your tickets are ready to be printed\n")
    for ticket in tickets:
        print(ticket.getString())
        print("\n\n\n")
def saveTickets(tickets):
	i=1
	for ticket in tickets:
		nameOfFile=ticket.username+ticket.de+ticket.a+"("+str(i)+").txt"
		file=open(nameOfFile,"w")
		file.write(ticket.getString())
		file.close()

def modifyFligths():
    fligths=getFligths()
    print("\nWhich flight do you wish to modify?\n")
    string="\tOrigin\t\tDestination\t\tDeparture time\n\n"
    for i in range(0, len(fligths)):
        string+=str(i+1)+") \t"
        if len(fligths[i][0])<10:
            string+=fligths[i][0]+"\t\t"
        else:
            string+=fligths[i][0]+"\t"
        if len(fligths[i][1])<10:
            string+=fligths[i][1]+"\t\t"+fligths[i][2]+"\n"
        else:
            string+=fligths[i][1]+"\t"+fligths[i][2]+"\n"
    print(string)
    try:
        j=int(input())-1
        fligth=fligths[j]
        parameter=int(input("What parameter do you wish to change?\n 1) Origin\n2) Destination\n3) Flight distance\n4) Departure time\n: "))
		
        lugares=[]
        for i in places:
            lugares.append([places[i],i])
        lugares.sort()
        if parameter==1:
            print("Select the new origin: ")
            for i in lugares:
                print(str(i[0])+" : "+i[1])
            origin=int(input())
            if origin>12 or origin<0:
                print("Enter only valid options")
                time.sleep(3)
                clearScreen()
                modifyFligths()
            origin=inv_places[origin]			
            fligth[0]=origin
        elif parameter==2:
            print("Select the new destination: ")
            for i in lugares:
                print(str(i[0])+" : "+i[1])
            destination=int(input())
            if destination>12 or destination<0:
                print("Enter only valid options")
                time.sleep(3)
                clearScreen()
                modifyFligths()
            destination=inv_places[destination]
            fligth[1]=destination
        elif parameter==3:
            distance=input("Enter the distance the flight will take: ")
            fligth[3]=distance
        elif parameter==4:
            departureTime=input("Enter new departure time: ")
            fligth[2]=departureTime
        else:
            print("Enter a valid option")
            time.sleep(3)
            clearScreen()
            modifyFligths()
        fligths=fligths[:j]+fligths[j+1:]
        fligths.append(fligth)
        QuickSort(fligths,0, len(fligths)-1)
        file = open("fligths.txt","w")
        for fligth in fligths:
            file.write(fligth[0]+"::"+fligth[1]+"::"+fligth[2]+"::"+fligth[3]+"::"+fligth[4]+"::\n")
        file.close()
        print("The flight has been modified")
        time.sleep(3)
        clearScreen()
    except ValueError:
        print("Enter only valid options")
        time.sleep(3)
        clearScreen()
        modifyFligths()

def displayAdminMenu(username):
	global vuelos
	print("Bienvenido administrador",username)
	try:
		answer=int(input("\nWhat do you wish to do today?\n1) Add user\n2) Add flight\n3) Check flights\n4) Modify flights\n5) Exit\n"))
		if answer == 1:
			addUser()
		elif answer == 2:
			addFligth()
		elif answer == 3:
			vuelos.displayFligths()
		elif answer == 4:
			modifyFligths()
		elif answer == 5:
			print("Thanks for your visit")
			return
		else:
			print("Number out of range. Please try again.")
			time.sleep(5)
			clearScreen()
		displayAdminMenu(username)
	except ValueError:
		print("Enter only valid options")
		time.sleep(3)
		clearScreen()
		displayAdminMenu(username)

def displayUserMenu(username):
	global vuelos
	print("Welcome user ",username)
	try:
		answer=int(input("\nWhat do you wish to do today\n1) Check available routes\n2) Check flights\n3) Exit\n"))
		if answer == 1:
			getPaths(username)
		elif answer == 2:
			vuelos=fligths()
			vuelos.displayFligths()
		elif answer == 3:
			print("Thanks for your visit")
			return
		else:
			print("Number out of range. Please try again.")
			time.sleep(5)
			clearScreen()
		displayUserMenu(username)
	except ValueError:
		print("Enter only valid options")
		time.sleep(3)
		clearScreen()
		displayUserMenu(username)

def userSearch(head, username, password):
	if head==None:
		return None
	if head.val[1]==username:
		if head.val[2]==cifrar(password):
			return head.val
		else:
			return None
	elif username < head.val[1]:
		return userSearch(head.left, username, password)
	elif username > head.val[1]:
		return userSearch(head.right, username, password)

def login():
	print("Welcome to AeroMex\n")
	username = input("Enter the following information.\n\nUser:\n")
	password = getpass.getpass("Password:\n")
	if username=="quit":
		return
	users=getUsers()
	head=convertToBST(users)
	user=userSearch(head, username, password)
	if user:
		if user[0]=="#":
				clearScreen()
				return displayAdminMenu(username)
		elif user[0]=="$":
				clearScreen()
				return displayUserMenu(username)
	else:
		print("User or Password incorrect. Please try again.")
		time.sleep(2)
		clearScreen()
		login()

def main():
	login()

places={"CDMX":1, "Los Angeles":2, "Chicago":3, "Nueva York":4, "Tokio":5, "Toronto":6, "Paris":7, "Madrid":8, "Berlin":9, "Oslo":10, "Roma":11, "Buenos Aires":12}
inv_places = {v: k for k, v in places.items()}
vuelos=fligths()
main()


