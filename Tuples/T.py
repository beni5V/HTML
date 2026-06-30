my_tuple = ()
print(my_tuple)

my_tuple = (1,2,3)
print(my_tuple)

my_tuple =("mouse", [8,4,6] , (1,2,3,4,5))
print(my_tuple)

my_tuple = ("p","e", "r", "m", "i", "t")
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("mouse", [8,4,6], (1,2,3,))

print(n_tuple[0][3])       
print(n_tuple[1][1])      

# Slicing
print("Sliced :", my_tuple[1:4])

# Iterating through tuple
for letter in (my_tuple):
    print("Hello", letter)