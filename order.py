
choice = input("Which file do you want to open? (1 or 2)")

with open (r"C:\Users\WURUOQING\Desktop\python\helloearth.txt") as f: #"with" defines context
 text = f.read().strip()
 number = [int(c) for c in text if c not in ',']
 order = sorted(number,reverse=True) # "reverse=True" -> keyword-value pair
 reference = ','.join (str(int) for int in order) 
if choice == '1':
   print (reference) 
elif choice == '2':
 import os
 filepath = r"C:\Users\WURUOQING\Desktop\python\hellomars.txt"
 with open (filepath,'w') as f:
  f.write(reference)
 os.startfile(filepath)
else:
 print ("Invalid choice.")

answer = input ("Run again?")

while answer.strip().lower() == 'yes':
 choice = input("Which file do you want to open? (1 or 2)")

 if choice == '1':
    with open (r"C:\Users\WURUOQING\Desktop\python\helloearth.txt") as f:
     text = f.read().strip()
     number = [int(c) for c in text if c not in ',']
     order = sorted(number,reverse=True)
     print (order) 
 elif choice == '2':
  import os
  filepath = r"C:\Users\WURUOQING\Desktop\python\hellomars.txt"
  with open (filepath,'w') as f:
   f.write(reference)
  os.startfile(filepath)
 else:
  print ("Invalid choice.")

 answer = input ("Run again?")
 
 if answer.strip().lower() == 'no':
  break  
 
print ('Thank you!')

 