name = "Harry"

print(name[0:3])

print (name[-4:-1]) # If I see negative slicing
print (name[1:4]) # I will just convert it into positive slicing by counting from zero from start and minus 1 in the end
 
 # both 5 and 6 no. results are same because of corresponding indexes

print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

print(name[:5]) # is same as print(name[0:5])
print(name[0:5])
print (name [1:3:5]) # Practice for better understanding
