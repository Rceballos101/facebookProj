"""
File of function stubs for Projecct 07

@author: Nesquick & the Don
@sidenotes: done while listening to serious EDM (https://www.youtube.com/watch?v=0b0hkCRagR4)
"""

def open_file():
    ''' Prompt the user for a valid filepath to open'''
    global fp
    fp = ''
    while True:
        fileName = input('Enter file path: ')
        try:
            fp = open(fileName,'r')  
            if fp != "":
               break
        except:
           print("\nNo such file, Stop wasting my time!\n")
                  
    return fp

#   C:/Users/Sen/Desktop/Uni/CUS 620 (python)/Proj/small_network_data.txt

def read_file(fp):  
    '''read file and create a list of friend_id per user'''
    # Read n and initizlize the network to have n empty lists -- 
    #    one empty list for each member of the network
    global network
    global n
    
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])  

    for lines in fp:
        line = lines.split()
        user = eval(line[0])
        friend = eval(line[1])

        network[user].append(friend)
        network[friend].append(user)

    return network
    return n
    # You need to write the code to fill in the network as you read the file
    # Hint: append appropriate values to the appropriate lists.
    # Each iteration of the loop will have two appends -- why?

def num_in_common_between_lists(list1, list2):
    '''number of common elements between 2 lists'''
    global friendCount
    
    friendCount = 0
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                friendCount += 1 
    return friendCount


def init_matrix(n):
    '''Create an n x n matrix, initialize with zeros, and return the matrix.'''
    global matrix
    matrix = []
    
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' use the empty n x n matrix and compute the common elements for each x and y combinations'''
    global similarity_matrix
    similarity_matrix = matrix

    for i in range(n):
        for j in range(i+1):
            num_in_common_between_lists(network[i], network[j])
            similarity_matrix[i][j] = friendCount
            similarity_matrix[j][i] = friendCount

    return similarity_matrix



def recommend(user_id,network,matrix):
    ''' Remember the docstring'''
    
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

    print('-'*70)
    for j,ch2 in enumerate(maxListChar):
        if ch2 == bestHitChar:
            print ('user {} recommended friend is user {}'.format(user_id,maxListIndex[j]))
    print('-'*70)   
                
def main():
    global user_id
    
    open_file()
    read_file(fp)
    init_matrix(n)
    calc_similarity_scores(network)
    
    contin = ''
    while str(contin).upper != 'N':
        user_id = eval(input('Enter a number (0:{}): '.format(n)))
        recommend(user_id,network,matrix)
        contin = str(input('\nContinue [Y/N]: ')).upper
    
main()
