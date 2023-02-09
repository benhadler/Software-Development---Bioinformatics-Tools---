def computeSensitivity(l,r,e):
    ans = 1 - (1 -(1 - e)**l)**(r-l+1)
    return ans

def computeSpeedup(l,r):
    ans = (4**l)/(2*(r**2))
    return ans
nums = [5,11,15,20,25,30,35,40]
print('Sensitivities: ')
for num in nums:
    ans = computeSensitivity(num,100,0.15)
    print(num,end='')
    print(':', ans)
print('\nSpeedups: ')
for num in nums:
    ans = computeSpeedup(num,100)
    print(num,end='')
    print(':', ans)