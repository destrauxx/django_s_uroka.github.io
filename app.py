# def encode(string):
#     res = ''
#     for i in string:
#         if i == 'a':
#             res += 'b'
#         elif i == 'b':
#             res += 'a'
#         else:
#             res += i
#     print(res)

# encode('acb')
# encode('aabacbaa')

def elevatorDistance(floors):
    res = 0
    for i in range(len(floors) - 1):
        res += abs(floors[i] - floors[i+1])
        # if floors[i] > floors[i+1]:
        #     res += floors[i] - floors[i+1]
        # elif floors[i] < floors[i+1]:
        #     res += floors[i+1] - floors[i]
    print(res)

elevatorDistance([5, 2, 8])
elevatorDistance([1, 2, 3])
elevatorDistance([7, 1, 7, 1])