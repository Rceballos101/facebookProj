"""
Group 7: Sen Varghese & Reyes Ceballos
Project: 1,  Facebook: Suggest Facebook friends using real, but heavily anonymised data.

User enters a user id and the program will suggest the most probable user to befriend based upon the intersection of your common friends. 
The user that that is suggested to Person A is the person who has the most friends in common with Person A, but who currently is not friends with Person A
"""


def open_file():
    ''' Prompt the user for a valid filepath to open where network data is saved'''
    global fp
    fp = ''
    while fp == '':
        fileName = input('Enter file path: ')#path where data is saved
        fp = open(fileName,'r')    
    return fp

#   'C:/python/project/facebook_1000_data.txt'
#   'C:/python/project/small_network_data.txt'

def read_file(fp):  
    '''read file and create a list of friend_id per user'''
    # Read n and initialize the network to have n empty lists -- 
    #    one empty list for each member of the network
    global network
    global n
    
    n = fp.readline()#total number of users
    n = int(n)
    network = []
    for i in range(n):
        network.append([])#create a list for each user  

    for lines in fp:
        line = lines.split()
        user = eval(line[0])
        friend = eval(line[1])

        network[user].append(friend)#appends friend to user1's list
        network[friend].append(user)#appends user1 to friends list

    return network
    return n
    # You need to write the code to fill in the network as you read the file
    # Hint: append appropriate values to the appropriate lists.
    # Each iteration of the loop will have two appends -- why?

def init_matrix(n):
    '''Create an n x n matrix, initialize with zeros, and return the matrix.
    '''
    global matrix
    matrix = []
    
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix


def num_in_common_between_lists(list1, list2):
    '''number of common friends between all of a user's friends'''
    global friendCount
    
    friendCount = 0
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                friendCount += 1 
    return friendCount

   
def calc_similarity_scores(network):  
    ''' use the empty n x n matrix and compute the common elements for each x and y combinations'''
    global similarity_matrix
    similarity_matrix = matrix

    for i in range(n):#each user
        for j in range(i+1):#number of friends for each user
            num_in_common_between_lists(network[i], network[j])#i is users friends, j is friends friends
            similarity_matrix[i][j] = friendCount
            similarity_matrix[j][i] = friendCount

    return similarity_matrix



def recommend(user_id,network,matrix):
    ''' Program goes through the previous matrix and returns the common friend that is not the original user'''
    
    global recommendedFriend   
    possibleFriends = similarity_matrix[user_id]
    
    maxListIndex = []
    maxListChar = []

    for i, ch in enumerate(possibleFriends):
        if i != user_id:
            if i not in network[user_id]:
                maxListIndex.append(i)
                maxListChar.append(ch)

    bestHitChar = max(maxListChar)
    bestHitIndex = maxListChar.index(bestHitChar)
    recommendedFriend = maxListIndex[bestHitIndex]

    print ('\nUser {} recommended friend is user {}'.format(user_id,recommendedFriend))
    
                
def main():
    global user_id
    
    open_file()
    read_file(fp)
    init_matrix(n)
    calc_similarity_scores(network)
    
    
    contin = ''
    while contin != 'N':
        user_id = 15
        while type(user_id) != int or int(user_id) > n or int(user_id) < 0:
            try:
                user_id = int(input('\nEnter an integer in the range 0 to {}: '.format(n)))
            except:
                print('This is not an integer ')
                
        
        recommend(user_id,network,matrix)
        contin = input('\nDo you wish to ontinue? [Y/N]: ')
        contin = contin.upper()
        
    
main()
