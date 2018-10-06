class InsertionSort():    
    def insertion_sort(self, target_list:list):
        
        for j in range(1,len(target_list)):
            key = target_list[j]
            # target_list[j]をソート済みの列 target_list[0..j-1]に挿入する
            i = j - 1
            while i >= 0 and target_list[i] > key:
                target_list[i+1] = target_list[i]
                i = i - 1
            target_list[i+1] = key
        
        return target_list

target_list = [3,1,5,4,7]
print(target_list)
obj = InsertionSort()
obj.insertion_sort(target_list)
print(target_list)
