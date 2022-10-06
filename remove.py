# remove.py
#
# 

#Takes user input
strng = input("Input your desired word:")
charnull = input("Input the character you would like removed from your word:")

#Holds value of strng
sum = ''

#Omits desired letter
for char in strng:
    if charnull != char:
        sum += char
    else:
        continue

#Output
print(sum)