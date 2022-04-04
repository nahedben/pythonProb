# text = input("Enter your message :")
# cipher = ""
# for e in text :
#   if e== ' ':
#     cipher += e

#   elif e.isalpha()== False:
#     continue
  
#   else:
#     e = e.upper()
#     code = ord(e) +1
#     if code > ord('Z'):
#       code = ord('A')
    
#     cipher += chr(code)


# print("the modified message of ",text," is:",cipher)


text = input('Enter you message : ')

cypher=''

for e in text :
  if e == ' ':
    cypher += ' '
  elif not e.isalpha():
    continue
  else:
    e = e.upper()
    code = ord(e) +1
    # print(code)
    if code > ord('Z'):
      code = ord('A')
      # print(code)
  cypher +=chr(code)
print('the resulted message is :', cypher)

print('this is the new modifications')