import numpy as np
import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class fligth:
    def __init__(self, distance, departureTime, procedence, destination, name):
        self.name=name
        self.to = None
        self.distance=int(distance)
        self.departureTime=departureTime

        if 250000 > self.distance > 500000:
            aircraft="AT-1200"
            firstClass=50
            economic=250
        elif 100000 > self.distance > 250000:
            aircraft="AT-1000"
            firstClass=40
            economic=160
        elif 50000 > self.distance > 100000:
            aircraft="AT-800"
            firstClass=20
            economic=80
        elif self.distance<50000:
            aircraft="AT-400"
            firstClass=10
            economic=30

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

    def findPaths(self, start, end, path=[], fligth=None):
        if fligth:
            path = path + [fligth]

        if start == end:
            return [path]
        
        if not self.fligths.__contains__(start):
            return []
        paths = []
        for node in self.fligths[start]:
            if node not in path:
                newpaths = self.findPaths(node.to, end, path,node)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end, path=[],fligth=None):
        paths=self.find_all_paths(start, end)
        shortest=None
        if paths:
            for path in paths:
                if not shortest or len(path)<len(shortest):
                    shortest=path
        return shortest

    def dfs(self, start, end):
        stack = [(start, [])]
        while stack:
            (vertex, path) = stack.pop()
            for fligth in self.fligths[vertex] - set(path):
                if fligth.to == end:
                    yield path+[fligth]
                else:
                    stack.append((fligth.to, path + [fligth]))

    def BFS(self, start, visited=None):
        if start==end:
            return visited
        if visited is None:
            visited = set()
        visited.add(node)
        for fligth in self.fligths[node]:
            if fligth not in visited:
                self.BFS(fligth.to, visited)
        return visited
def cifrar(cadena):
    aux = ''
    for i in cadena:
        aux += chr(ord(i)+3)
    return aux

def getUsers():
    with open('users.txt') as file:
        users = []
        for line in file:
            line=line.split("::")
            users.append(line)
    file.close()
    return users

def updateUsers():
    users=getUsers()
    users.sort(key=lambda x: x[1])
    file = open("users.txt","w")
    for user in users:
        file.write(user[0]+"::"+user[1]+"::"+cifrar(user[2])+"::"+"\n")
    file.close()

updateUsers()

"""
vuelos=fligths()

paths=list(vuelos.dfs("Los Angeles","Roma"))
origin="Los Angeles"
for path in paths:
    for fligth in path:
        print(origin+"->"+fligth.to)
        origin=fligth.to
    print()
path=vuelos.findPath("Roma","Nueva York")
for fligth in path:
    print(fligth.to)"""
"""
paths=vuelos.findPaths("Roma","Nueva York")
origin="Roma"
for path in paths:
    for fligth in path:
        print(origin+"->"+fligth.to)
        origin=fligth.to
    print("\n")"""



"""
vuelos=fligths()
path=vuelos.find_path("Roma","Tokio")
for fligth in path:
    print(fligth.to)


print("\n")

paths=vuelos.find_all_paths("Roma","Tokio")
for path in paths:
    for fligth in path:
        print(fligth.to)
    print("\n")


path=vuelos.find_shortest_path("Roma","Tokio")
for fligth in path:
    print(fligth.to)
vuelos.displayFligths()
#for fligth in path:
#    print(fligth.to)


def displayFligths():
    string="Origen\t\tDestino\t\tHora de Salida\n"
    fligths=getFligths()
    for fligth in fligths:
        if len(fligth[0])<10:
            string += fligth[0]+"\t\t"
        else:
            string += fligth[0]+"\t"
        if len(fligth[1])<10:
            string += fligth[1]+"\t\t"+fligth[2]+"\n"
        else:
            string += fligth[1]+"\t"+fligth[2]+"\n"
    print(string)
    
class fligths:
    def __init__(self):
        self.fligths = []
        self.num_destinations = len(places)
        i = 0
        while i <= len(places):
            self.fligths.append(None)
            i += 1
        self.num_fligths=0
        with open('fligths.txt') as file:
            for line in file:
                line=line.split("::")
                vuelo = fligth(line[3],line[2],line[0], line[1])

                origin=places[line[0]]
                destination=places[line[1]]

                vuelo.to = destination
                vuelo.prev = self.fligths[origin]
                self.fligths[origin]=vuelo
                self.num_fligths+=1
        file.close()

    def display(self):
        i = 1
        string = "VUELOS\n"
        string+="Origen\t\tDestino\t\tHora de Salida\n"
        while i <= len(places):
            #string += str(inv_places[i])+"\t"
            item = self.fligths[i]
            while item != None:
                if len(str(inv_places[i]))<10:
                    string += str(inv_places[i])+"\t\t"
                else:
                    string += str(inv_places[i])+"\t"
                if len(str(inv_places[item.to]))<10:
                    string += str(inv_places[item.to])+"\t\t"+str(item.departureTime)+"\n"
                else:
                    string += str(inv_places[item.to])+"\t"+str(item.departureTime)+"\n"
                item = item.prev
            i +=1
        print(string)

    def findPath(self,start, end, path=[]):
        start=self.fligths[start]

        while start != None:
            if start.color=="White":
                path.append(start)
                if start.to==end:
                    return path
                start.color="Grey"
                newpath = self.findPath(start.to, end, path)
                if newpath:
                    return newpath
            start = start.prev
        return None

class fligths:
    def __init__(self):
        self.fligths = []
        self.num_destinations = len(places)
        i = 0
        while i <= len(places):
            self.fligths.append(None)
            i += 1
        self.num_fligths=0
        with open('fligths.txt') as file:
            for line in file:
                line=line.split("::")
                vuelo = fligth(int(line[3]),line[2],line[0], line[1])

                origin=places[line[0]]
                destination=places[line[1]]

                vuelo.to = destination
                vuelo.prev = self.fligths[origin]
                self.fligths[origin]=vuelo
                self.num_fligths+=1
        file.close()
    def setWhite():
        i = 0
        while i <= len(places):
            fligth=self.fligths[i]
            while fligth != None:
                fligth.color="White"
                fligth=fligth.prev
            i += 1
    def display(self):
        i = 1
        string = "VUELOS\n"
        string+="Origen\t\tDestino\t\tHora de Salida\n"
        while i <= len(places):
            #string += str(inv_places[i])+"\t"
            item = self.fligths[i]
            while item != None:
                if len(str(inv_places[i]))<10:
                    string += str(inv_places[i])+"\t\t"
                else:
                    string += str(inv_places[i])+"\t"
                if len(str(inv_places[item.to]))<10:
                    string += str(inv_places[item.to])+"\t\t"+str(item.departureTime)+"\n"
                else:
                    string += str(inv_places[item.to])+"\t"+str(item.departureTime)+"\n"
                item = item.prev
            i +=1
        print(string)

    def displayColor(self):
        i = 1
        string = "VUELOS\n"
        string+="Origen\t\tDestino\t\tColor\n"
        while i <= len(places):
            #string += str(inv_places[i])+"\t"
            item = self.fligths[i]
            while item != None:
                if len(str(inv_places[i]))<10:
                    string += str(inv_places[i])+"\t\t"
                else:
                    string += str(inv_places[i])+"\t"
                if len(str(inv_places[item.to]))<10:
                    string += str(inv_places[item.to])+"\t\t"+str(item.color)+"\n"
                else:
                    string += str(inv_places[item.to])+"\t"+str(item.color)+"\n"
                item = item.prev
            i +=1
        print(string)


    def findPath(self,start, end, path=[]):

        start=self.fligths[start]
        
        while start != None:
            if start.color=="White":
                if self.fligths[start.to]!=None and start not in path:
                    path.append(start)
                if start.to==end:
                    return path
                start.color="Grey"
                newpath = self.findPath(start.to, end, path)
                if newpath:
                    return newpath
            start = start.prev
        return None

    def findPaths(self,start, end, path=[]):

        start=self.fligths[start]
        
        while start != None:
            if start.color=="White":

                path.append(start)
                if start.to==end:
                    return path
                start.color="Grey"
                newpath = self.findPath(start.to, end, path)
                if newpath:
                    return newpath
            start = start.prev
        return []

    def findPath2(self, start, end, path=[]):

        start=self.fligths[start]

        queue = Queue()
        queue.enqueue(start)

        while (queue.size() > 0):
            currentFligth = queue.dequeue()

            
            print(currentFligth.to)
            #item = self.fligths[currentFligth.to]
            while currentFligth != None:
                if currentFligth.color == "White":
                    path.append(currentFligth)
                    if currentFligth.to==end:
                        return path
                    currentFligth.color = "Grey"
                    queue.enqueue(self.fligths[currentFligth.to])
                currentFligth = currentFligth.prev
            #CurrentFligth.color="Black"
def findPaths(self, start, end, path=[], fligth=None):
        if fligth:
            path = path + [fligth]

        if start == end:
            return [path]
        
        if not self.fligths.__contains__(start):
            return []
        paths = []
        for node in self.fligths[start]:
            if node not in path:
                newpaths = self.findPaths(node.to, end, path,node)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

places={"CDMX":1, "Los Angeles":2, "Chicago":3, "Nueva York":4, "Tokio":5, "Toronto":6, "Paris":7, "Madrid":8, "Berlin":9, "Oslo":10, "Roma":11, "Buenos Aires":12}
inv_places = {v: k for k, v in places.items()}

vuelos=fligths()

vuelos.displayColor()

fligths=vuelos.findPath(11,5)

for fligth in fligths:
    print(fligth.procedence+"::"+fligth.destination)

print("\n")
fligths=vuelos.findPath2(11,5)
print(fligths)"""




















