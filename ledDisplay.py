## Display stars in number shapes

baselist={'0':['# # #','#   #','#   #','#   #','# # #'],
          '1':['   # ','   # ','   # ','   # ','   # '],
          '2':['# # #','    #','# # #','#    ','# # #'],
          '3':['# # #','    #','# # #','    #','# # #'],
          '4':['#   #','#   #','# # #','    #','    #'],
          '5':['# # #','#    ','# # #','    #','# # #'],
          '6':['# # #','#    ','# # #','#   #','# # #'],
          '7':['# # #','    #','    #','    #','    #'],
          '8':['# # #','#   #','# # #','#   #','# # #'],
          '9':['# # #','#   #','# # #','    #','# # #']}

def disp(l): 
  for n in range(5):
    print()
    for i in l:
      print(i[n],end='  ')
  print()

def sevenSegment(num):
  resl=[]
  l=[]
  if type(num)!='string':
    num =str(num)
  
  for e in num :
    l.append(e)

  for n in l:
    resl.append(baselist[n])

  return disp(resl)

   

sevenSegment(9457102)
sevenSegment(775710)
print(" A new modification on the python ")
