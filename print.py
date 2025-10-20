choice = input("Which file do you want to open? (1 or 2) ")

if choice == '1':
 with open (r"C:\Users\WURUOQING\Desktop\python\helloearth.txt") as f:
   text = f.read().strip()
   clean = ''.join (c for c in text if c not in ',') #"c" for "character", '' before "join" is separator, in this case nothing
   print (clean)
elif choice == '2':
 from datetime import datetime #from module "datetime", import class "datetime"
 with open (r"C:\Users\WURUOQING\Desktop\python\hellomars.txt") as f: #"with" defines context
  text = f.read().strip()
  date_obj = datetime.strptime(text, '%Y%m%d') #"strptime", "string parse time" PARSES string into datetime object (4 digit year, 2 digit month and day)
  formatted_date = date_obj.strftime('%Y-%m-%d')
  print (formatted_date)
else:
 print ("Invalid choice.")

answer = input ("Run again?")

while answer.strip().lower() == 'yes':
 choice = input("Which file do you want to open? (1 or 2) ")

 if choice == '1':
   with open (r"C:\Users\WURUOQING\Desktop\python\helloearth.txt") as f:
    text = f.read().strip()
    clean = ''.join (c for c in text if c not in ',')
    print (clean)
 elif choice == '2':
   from datetime import datetime
   with open (r"C:\Users\WURUOQING\Desktop\python\hellomars.txt") as f:
    text = f.read().strip()
    date_obj = datetime.strptime(text, '%Y%m%d')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    print (formatted_date)
 else:
  print ("Invalid choice.")

 answer = input ("Run again?")
 
 if answer.strip().lower() == 'no':
  break  
print ('Thank you!')

 