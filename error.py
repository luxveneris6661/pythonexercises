#error management in python: how do I let the program understand that there's a character in the file
#and have it output "invalid request" from detecting the character

choice = input("Which file do you want to open? (1 or 2)")
def error(text):
 if any ( not c.isdecimal() for c in text):
  return True
 else:
  return False
 
with open (r"C:\Users\WURUOQING\Desktop\python\helloearth.txt", encoding='utf-8') as f: #"with" defines context
   text = f.read().strip().replace('\n','').split(',')
if choice == '1': 
 if error(text):
  print ('Error: Unsupported Characters.')
 else:
  number = [int(c) for c in text]
  order = sorted(number,reverse=True) # "reverse=True" -> keyword-value pair
  reference = ','.join (str(int) for int in order) 
  print (reference) 
elif choice == '2':
 import os
 with open (r"C:\Users\WURUOQING\Desktop\python\helloearth.txt", encoding='utf-8') as f: 
  text = f.read().strip().replace('\n','').split(',')
  filepath = r"C:\Users\WURUOQING\Desktop\python\hellomars.txt"
  if error(text):
   print ('Error: Unsupported Characters.')
  else:
   number = [int(c) for c in text]
   order = sorted(number,reverse=True) 
   reference = ','.join (str(int) for int in order) 
   with open (filepath,'w') as f:
    f.write(reference)
    os.startfile(filepath)
else:
 print ("Invalid choice.")
 

