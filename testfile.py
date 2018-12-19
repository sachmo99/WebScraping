from selenium import webdriver
from selenium.webdriver.common.keys import Keys
query = input("Enter the name of the book you want").split()
inp = ""
for x in query[:len(query)-1]:
    inp+=x + "+"

inp+=query[len(query)-1]

#query = "helloworld"
searchurl = "https://www.pdfdrive.com/search?q={}&pagecount=&pubyear=&searchin=&r=1".format(inp)
print(searchurl)