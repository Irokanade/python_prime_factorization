import math

a = int(input('input an integer: '))

for i in range(2, int(math.sqrt(a)+1)):
    if a%i == 0:
        print(f'{a} is not a prime')
        break

    else:
        print(f'{a} is a prime')
        exit()

print('{0}='.format(a), end = "")

firstFactorPrinted = bool(False)

for i in range(2, int(math.sqrt(a)+1)):
    while a%i==0:
        if firstFactorPrinted == False:
            print('{0}'.format(i), end = "")
            firstFactorPrinted = True
            a=a/i
        
        else:
            print('*{0}'.format(i), end = "")
            a=a/i

    
if a > 2:
        print('*{0}'.format(i))