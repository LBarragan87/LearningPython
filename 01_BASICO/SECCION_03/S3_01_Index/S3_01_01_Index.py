my_str = "Hola Mundo"

'''
x=(dir(my_str)) -> dir, return metodos aplicables al elemento
for y in x:
    print(y)
'''
my_str_length=len(my_str)
my_str_upper = my_str.upper()
my_str_lower = my_str.lower()
my_str_repeated_letter = my_str.count("a")
print (my_str_upper)
print (my_str_lower)
print (my_str.index("M"))
print (my_str[2])
print (my_str_length)
print (my_str_repeated_letter)