#to create the file and write with the hep of object
open("demo.txt","w")
file=open("File handling_demo.txt","w")
file.write ("Hello,world!\n")
file.write("Python is great")
file.close()

#writing without object
with open("demo.txt","w")as f:
    f.write("Hello,World!\n")
    f.write("this is text and sentences\n")
    f.write("line 3\n")
    f.close()

# reading the file using object    
fileobj=open("demo.txt","r")
fileobj.read()
fileobj.close()

#reading the file without object
with open("demo.txt","r")as f:
    content=f.read()
    print(content)

with open ("demo.txt","r")as f:
    for line in f:
        print(line.strip())
        
with open("demo.txt","r") as f:
    for line in f:
        print(line)
        
# to read multiple lines of a file       
with open("demo.txt","r")as f:
    lines=f.readlines()
    print(lines)

# to read a single line    
with open("demo.txt","r") as f:
    first=f.readline()
    print(first.strip())

#to append the file
with open("demo.txt","a")as f:
    f.write("New line added!\n")
 
#to read as well as write
with open("demo.txt","r+")as f:
    content=f.read()
    f.write("append via r+\n")
print(content)

#to check file exist or not 
import os 
if os.path.exists("demo.txt"):
    print("File exist!")
    print(f"size:{os.path.getsize ('demo.txt')} bytes")
    
import os 
if os.path.exists("demo.txt"):
    print("File exist!")
    print(f"size:{os.path.getsize ('demo.txt')} bytes")

#to work with multiple files
f=open("input.txt","w")
f.close()
with open("input.txt","r")as fin,\
     open("output.txt","w")as fout:
         for line in fin:
             fout.write(line.upper())
    
