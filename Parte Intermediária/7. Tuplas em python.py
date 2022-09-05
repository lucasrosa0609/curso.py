'''
Tuplas
'''

#  São similares com listas

# t1 = 1,  # essa virgula precisa pra poder ser considerada tupla
'''
t1 = 1,2,'Lucas',4,5
t2 = 6,7,8,9,10
t3 = t1+t2

n1, n2, n3, *_, n10 = t3

print(_)
'''
'''
t1 = (1, 2, 'Lucas', 4, 5)*20

print(t1)
'''

t1 = (1,2,3,4,5)
t1 = list(t1)
t1[1] = 3000

print(t1)