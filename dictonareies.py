def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')
# def ninja_intro(dictonary):
#     for key, val in dictonary.items():
#         print(f'I am {key} and I am {val} belt')


ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name: ')
    ninja_belt = input('enter a belt colour: ')
    ninja_belts[ninja_name] = ninja_belt


    another = input('add anthoer? (y/n)')

    if another == 'y':
        continue
    else:
        break

belt_count(ninja_belts)