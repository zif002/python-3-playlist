age = 25
num = 0



while num < age:
    if num == 0:
        num += 1
        continue
    #block of code
    if num % 2 == 0:
        print(num)
    if num > 10:
        break   
    num +=1