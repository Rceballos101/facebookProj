

def facebook():
    fp = open('C:/python/project/small_network_data.txt','r')#location of test data
    #convert to input when final
    n = fp.readline() # number of users in network
    n = int(n)
    network = [] #holds all users friends
    
    for i in range(n):
        network.append([]) #creates a list of each user and there friends
    
    friends = fp.readlines() #list of each user and 1 of there friends

    for y in range(len(friends)):#eliminates white space from each list
        friends[y] = friends[y].strip()

    users = []#list of users
    

    for j in friends:#creates list of users
        group = j.split(' ')#splits row into 2 friends     
        for k in group:
            if k not in users:
                users.append(k)
    print('Our users are ',users)
        
        
    for f in friends:#inputs user followed by his friends in a list
        group = f.split(' ')#splits row into 2 friends
        f1 = eval(group[0])
        f2 = eval(group[1])
        if group[0] not in network[f1]:
            network[f1].append(group[0])
        if group[1] not in network[f2]:   
            network[f2].append(group[1])
        if group[0] not in network[f2]:
            network[f2].append(group[0])
        lst = eval(group[0])#user
        network[lst].append(group[1])
        if group[0] not in network[lst]:
            network[lst].append(group[0])
        
                
    print(network)#testing purposes only
    fp.close()
facebook()
