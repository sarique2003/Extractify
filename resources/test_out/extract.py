from bs4 import BeautifulSoup
from pathlib import Path
import os

path = "/home/ravenclaw/Desktop/IISERK/grobid_client_python/resources/test_out"
def read_xml_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        read_xml_file(file_path)

'''for filepath in Path('').glob('*/*.XML'):
    with filepath.open() as f:
        file = f.read()
        print("*********************88")
        soup = BeautifulSoup(f,'lxml-xml')
    print(soup.prettify())
option = int(input("Choose 1 or 2 for processing file 1 or 2: "))
if(option == 1):
  with open('2108.10341.tei.xml', 'r') as f:
   file = f.read() 
elif(option == 2):
   with open('2206.11900.tei.xml', 'r') as f:
    file = f.read() 

soup = BeautifulSoup(file, 'xml')
names = soup.find_all('head')
data = soup.find_all('p')

items =["effectiveness","frequency","train","datasets"] 
def check(str,count):
   count =0
   for i in range(4):
     if(items[i] in ans):
      count +=1
   return count

print("Available sections are: \n")
for num in names:
   print(num.text)

ans =" "
         
search = True
for info in data :
   ans = str(info.text)
   cnt=0
   if(search):
     flag =check(ans,cnt)
     if(flag >=2):
      print(ans)
      print("\n")
      
'''
#most used words :experiments ,experimentation,dataset/datasets, efectivness/efectivity,efficiency, trained/train



         