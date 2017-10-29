# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:07:14 2017

@author: user
"""

def facebook():
    fp = open('C:/python/project/small_network_data.txt','r')
    n = fp.readline()
    n = int(n)
    network = []
    
    for i in range(n):
        network.append([])
    
    friends = fp.readlines()

    for y in range(len(friends)):
        friends[y] = friends[y].strip()

    for j in friends:
        group = j.split(' ')
        lst = eval(group[0])
        lst2 = eval(group[1])
        network[lst].append(group[1])
        network[lst2].append(group[0])
                
    print(network)
    fp.close()
facebook()

'''
    friends = ':'.join(friends)
    friends = friends.replace(':','')
    new = friends.maketrans(':','')
    friends.translate(new)
    print(friends[0])

'''
'''for x in range(len(friends)):
        friends[x] = friends[x].strip'''