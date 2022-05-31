import numpy as np
m,n = map(int, input().split())
m1 = []
for i in range(m):
    ele = list(map(int, input().split()))
    m1.append(ele)
m1 = np.array(m1)
print(m1)
print('transpose')
print(m1.T)

print('flatten')
print(m1.flatten())