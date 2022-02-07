




# def max_subarray(a, window_size):
#     list_sum = []
#     for i in range(len(a) - (window_size-1)):
#         subarray = []
#         for j in range(0, window_size):
#             subarray.append(a[i+j])
#         list_sum.append(sum(subarray))
#         # print(list_sum)
#         print(max(list_sum))

#     print(list_sum)




# inputs =[3, -1, -2, 1, -2, 4, 2, -3, 1, 3, 1]
# max_subarray(inputs, 5)

'''
def max_subarray(mylist):
    sub = []
    for i in range(len(mylist)):
        subarray = []
        for j in range(len(mylist)):
            subarray.append(mylist[j])
    print(subarray)

    subarray = []
    for i in range(1, len(mylist)):
        subarray.append(mylist[i])
    print(subarray)

    subarray = []
    for i in range(2, len(mylist)):
        subarray.append(mylist[i])
    print(subarray)

    subarray = []
    for i in range(3, len(mylist)):
        subarray.append(mylist[i])
    print(subarray)
'''

def max_subarray(a):
    list_sum = []
    for i in range(0, len(a)):
        subarray = []
        for j in range(0, i+1):
            subarray = a[j:i]
            print(subarray)
        list_sum.append(sum(subarray))

    print(list_sum)

inputs = [1,2,-1,1]
max_subarray(inputs)