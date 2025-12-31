counteven=0
countodd=0
for i in range(1,10):
    if (i%2==0):
        counteven=counteven+1
    else:
        countodd=countodd+1

print("the odd count:",countodd)
print("the even count:",counteven)