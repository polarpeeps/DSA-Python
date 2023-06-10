def swap(a,i,j):
    a[i],a[j] = a[j], a[i]
    return a 

def arr_sort(a,pivot=1):
    i = 0
    j = 0
    k = len(a)-1
    # mid = (i+k)//2
    while j <= k:
        if a[j] <= pivot:
            swap(a,i,j)
            i = i + 1
            j = j + 1
        elif a[j] > pivot:
            swap(a,j,k)
            k = k - 1
            j+=1
        else:
            i+=1
            j += 1
    return a

            

if __name__=='__main__':
    s = int(input("ENTER SIZE OF ARRAY:"))
    arr = []
    for i in range(1,s+1):
        e = int(input(f"ENTER ELEMENT {i} :"))
        arr.append(e)
    print(f"THE ENTERED ARRAY IS-\n{arr}")
    asl =[] + arr_sort(arr)
    print(asl)



