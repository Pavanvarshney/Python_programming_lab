import numpy as np
m,n = map(int, input().split())
m1 = []
m2 = []
for i in range(m):
    ele = list(map(int, input().split()))
    m1.append(ele)
for i in range(m):
    ele = list(map(int, input().split()))
    m2.append(ele)
m1 = np.array(m1)
m2 = np.array(m2)

print('add')
print(np.add(m1,m2))

print('subtract')
print(np.subtract(m1,m2))

print('product')
print(np.multiply(m1,m2))

print('division')
print(np.divide(m1,m2))

print('mod')
print(np.mod(m1,m2))

print('power')
print(np.power(m1,m2))