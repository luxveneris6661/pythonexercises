import os

choice = input("Which file do you want to open? (1 or 2) ")

if choice == '1':
 filename = r"C:\Users\WURUOQING\Desktop\python\helloearth.txt"
elif choice == '2':
 filename = r"C:\Users\WURUOQING\Desktop\python\hellomars.txt"
else:
 print("Invalid choice.")
 filename = None

if filename:
 os.startfile(filename)