
# k = []
# k.append(ls.reverse())
# print("THE REVERSED ARRAY IS:",k)
# k = ls.reverse()
def reverse(lst):
    # lst.reverse()
    # print('The reversed array is:',lst)
    lst = list(lst)

    star_index = 0

    end_index = len(lst) - 1

    while star_index < end_index:
       
       lst[star_index], lst[end_index] = lst[end_index],lst[star_index]
       star_index = star_index + 1
       end_index = end_index - 1
    return lst



if __name__=='__main__':
    s = int(input("Enter Size of Array"))
    ls = []
    for i in range(s):
      e = input("enter element:")
      ls.append(e)
    print("THE ENTERED ARRAY IS:",ls)
    print(reverse(ls))

    