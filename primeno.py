x = int(input())
if x>1:
    for i in range(1,x):
        if x % i == 0:
            print('x is a prime no.')
        else:
            print("x is not a prime no.")