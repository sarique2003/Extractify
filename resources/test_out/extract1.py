from bs4 import BeautifulSoup
import numpy

with open('2206.11900.tei.xml', 'r') as f:
  file = f.read() 
soup = BeautifulSoup(file, 'xml')
names = soup.find_all('head')
data = soup.find_all('p')

find = input("Which section are you looking for:")
for num in names:
   if (num.text == find):
    print(num.text)
    print("----------------------------------------------- \n")

ans =" "
         
find1= str(input("Your dataset starts with? \n"))
for info in data :
    ans = str(info.text)
    if(find1 in ans):
     print(ans) 
    