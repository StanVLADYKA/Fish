# плывущая рыбка в матрицу

import time
import copy



#for i in list:
#        i1 = str(i).replace(",", " ")
#        i2 = i1.replace("'", "")
#        i3 = i2.replace("[", "")
#        i4 =i3.replace("]", "")
#        print(i4)
#        #print(i, end="\n")


def Fish(list):
    for j in range(len(list)):
        for v in range(len(list[0])):
      #  try:
            ins=list[j][v]
            #print(ins)
      #  except: IndexError
            try:
                list2[j][v+1]=ins
            except: IndexError
    for p in range(len(list)):  # для переноса последнго столбца в начало
        insl = list[p][-1]
    #print(insl)
        list2[p][0] = insl
        return list2


#for n in list2:
#    print(n, end="\n")


def maneger():
    list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, '*', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['*', 0, '*', '*', '*', '*', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['*', 0, '*', '*', '*', '*', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, '*', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    list2 = []
    for z in range(len(list)):
        list2.append(["-"] * len(list[0]))


    while True:
        for n in Fish(list):
            n1 = str(n).replace(",", " ")
            n2 = n1.replace("'", "")
            n3 = n2.replace("[", "")
            n4 = n3.replace("]", "")
            print(n4)

        time.sleep(1)
    list=copy.copy(list2)
maneger()


#for n in list2:
#    n1=str(n).replace(","," ")
#    n2=n1.replace("'", "")
#    n3 = n2.replace("[", "")
#    n4 = n3.replace("]", "")
#    print(n4)



"""def sdvig(list1, a):
    return list1[a:] + list1[:a]


def manager():
    list = [[1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8]]
    newMatr = []
    a = int(input("vv"))
    for i in range(len(list)):
        newMatr.append(sdvig(list[0], a))
        a += 1

    vyvod(newMatr)


def vyvod(matr):
    for i in matr:
        print(i, end="\n")


manager()"""
