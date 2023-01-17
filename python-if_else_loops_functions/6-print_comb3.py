#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if j == 9 and i == 8:
            print(str(i) + str(j), end='\n')
        else:
            print(str(i) + str(j), end=', ')
