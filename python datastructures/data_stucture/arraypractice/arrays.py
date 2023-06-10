try:
    # import numpy as np
    # my_arr = np.array([45,24.4],ndmin=1)
    # # print(my_arr)
    # for item in my_arr:
    #     print(item)
    # # print(type(my_arr))
    # # print(my_arr[0])
    # # del my_arr[0]
    # # print(my_arr[0])
    # l = [0,1,3]
    # del l[0]
    # print(l[0])


    # # appending at last of array 
    # l.append(69)
    # l2=[0,1,3]

    # # concatinating
    # print(l+l2)
    # # extending
    # l.extend(l2)
    # print("l:",l)

    # # copy function
    # res = [3545] + l.copy()
    # print(res)

    # # remove functions removes the first appearance of th element
    # l.remove(1)
    # # pop removes the last item of list
    # l.pop()
    # print(l)

    # # reverse
    # l.reverse()
    # print("L reversed:",l)

    # # sort
    # l.append(-89)
    # l.sort()
    # print(l)

    #  ----LIST COMPREHENSION----
    num = [24,4,6,7,82,64,23,54,253]
    newl = [i for i in num if i%2 ==0]
    print(newl)

    names = ['patrick', 'jojo','denji','tanjiro','mob']
    fil = [ n for n in names if n.startswith("m")]
    print(fil)





except Exception as e:
    print(e)