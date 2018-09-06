class Sorting:
    def selectionSort(self,list):
        for i in range(len(list)):
            for j in range(i+1,len(list)):
                if list[i] > list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        print(list)
        print(list.extend([3,3,4,5,5,2,3,4,5]))
        print(list)
        print(list.sort())
        print(list.count(9))
        print(list.reverse())
        print(list.remove(9))
        print(list.index(3))
        
if __name__=='__main__':
    list = [7,8,4,6,7,3,8,9,4,9,3,2]
    objSorting = Sorting()
    objSorting.selectionSort(list)
    list = []
    objSorting.selectionSort(list)
