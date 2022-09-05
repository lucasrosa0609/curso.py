'''
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
'''

'''
a = -1
b = 11

while a <= 9 and b >= 3:
    a = a + 1
    b = b - 1
    print(a, b)

'''
'''
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
'''

reverso = 10
for index in range(19):
    if index > 8:
        index = index - 9
    print(index, reverso)
    reverso -= 1
    if reverso > 2:
        reverso = 11
