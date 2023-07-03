import time
import statistics


class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []      
 
    # function to add an edge to graph
    def addEdge(self, u, v, w, cityone, citytwo,vertexes):
        self.graph.append([u, v, w,cityone,citytwo])
        if cityone not in vertexes:
            vertexes[u]=cityone
        if citytwo not in vertexes:
            vertexes[v]=citytwo

    # utility function used to print the solution
    def printArr(self, dist, start, vertexes,cities):
        first_word = start.split()[0] #starting city

        for i in range(len(vertexes)):
            cityname=vertexes[i].split()[0]
            if (cityname!=first_word and dist[i]!=0):
                if (cityname in cities):
                    idx=cities.index(cityname)
                    if (dist[idx]<dist[i]):
                        continue
                    else:
                        cities[i]=cityname
                        cities[idx]=""
                else:                   
                    cities[i]=cityname
            
            else:
                continue
        for i in range(len(cities)):
            if(cities[i]!=""):
                print("From", vertexes[0], "to", cities[i] , "=" , dist[i])    
     
    #from one source to all other sources
    def BellmanFord(self, src, start, vertexes, cities):
 
        #initialize all the distance array values to infinity
        dist = [float("Inf")] * self.V
        dist[src] = 0

        #relax all the edges |V-1| times
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w, cityone, citytwo in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        
        # print all distance
        self.printArr(dist,start,vertexes,cities)


'''
#GIVE INPUTS BY ANSWERING THE QUESTIONS (THERE IS A SECOND WAY DOWN)
stations=int(input("How many stations are there? "))

g = Graph(stations) 
vertexes = [""] * stations   # stations = number of vertices (stations) (for example 1 train station in a particular city is 1 vertex and bus station in the same city is another vertex)
cities = [""] * stations     # name of the cities to go
stationlist=[""] * stations

for i in range(stations):
    stop=input("Enter stations one by one (Enter your starting station first): " )
    stationlist[i]=stop

while (True):
    station1=input("Give station 1 (if no stations are left type no): ")
    if(station1 == "no"):
        break
    else:
        station2=input("Give station 2: ")
        dstnc=int(input("Distance between these 2 stations? "))
    idx1=stationlist.index(station1)
    idx2=stationlist.index(station2)
    g.addEdge(idx1, idx2, dstnc,stationlist[idx1], stationlist[idx2],vertexes)
    g.addEdge(idx2, idx1, dstnc,stationlist[idx2], stationlist[idx1],vertexes)


start_time = time.time()

g.BellmanFord(0,stationlist[0],vertexes,cities) # give the starting destination name

end_time=time.time()
timecheck=end_time-start_time
print("Process finished in: ", timecheck, "seconds")

'''

#GIVE INPUTS BY PUTTING THEM INTO A TXT FILE

#IMPORTANT TXT FORMAT:
#FIRST LINE OF TXT HAS TO BE THE NUMBER OF STATIONS
#SECOND LINE HAS TO BE THE STARTING LOCATION
#LIST THE STATION NAMES ONE BY ONE
#ONCE ALL THE STATIONS ARE DONE TYPE "ROUTES:" TO A NEW LINE
#THE DISTANCE BETWEEN TWO STATIONS FORMAT IS AS FOLLOWS: (EXAMPLE)
#IST BUS-IST TRAIN=10

textfile = []
with open(r'C:\Users\user\Desktop\cs301_hw4\maps\map5.txt') as f: #HAVE TO SPECIFY THE PATH IF USING THE TXT SOLUTION
    textfile = f.readlines()


stationnum=int(textfile[0])

g = Graph(stationnum) 
vertexes = [""] * stationnum  # stations = number of vertices (stations) (for example 1 train station in a particular city is 1 vertex and bus station in the same city is another vertex)
cities = [""] * stationnum     # name of the cities to go
stationlist=[""] * stationnum


i=0
for line in textfile:
    i=i+1
    
txt=[""]*i

j=0
for line in textfile:
    if(line[-1]=='\n'):
        txt[j]=line[:-1]
    else:
        txt[j]=line
    j=j+1

firststation=txt[1]

idx1=txt.index("ROUTES:")

stationlist = [""] * (idx1-1)
for k in range (idx1-1):
    stationlist[k]=txt[k+1]

z=idx1+1
m=i-(z)

for h in range(m):
    idx=txt[z].index("-")  
    index1=stationlist.index(txt[z][0:idx])
    idx2=txt[z].index("=")
    index2=stationlist.index(txt[z][idx+1:idx2])
    dstnc=int(txt[z][idx2+1:])
    g.addEdge(index1, index2, dstnc,stationlist[index1], stationlist[index2],vertexes) # give the starting destination name
    g.addEdge(index2, index1, dstnc,stationlist[index2], stationlist[index1],vertexes)
    z=z+1

g.BellmanFord(0,firststation,vertexes,cities) # give the starting destination name

