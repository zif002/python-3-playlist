def area(radius):
    return 3.142 * radius * radius

def vol(area, length):
    print(area * length)


length = int(input('enter a radius'))

vol(area(length), length)