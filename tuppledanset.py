#Tupple dan set

data_list = [1,2,3,4,5]
print(data_list)

data_tuple = (1,2,3,4,5,6,7)
#data_tuple.pop() ← has no attribute
for index,data in enumerate(data_tuple):
    print(f"index = {index}, data = {data}")
print(data_tuple)#index work
#data_tuple.extend(data_list) otput{no attribute}
#tidak bisa di ubah isinya menggunakan append,extend,pop,dll

data_sets = {1,2,3,4,5,6,7}
print(data_sets)
#print(f"Index = {data_sets[0]}") → error
#hanya tidak memiliki index