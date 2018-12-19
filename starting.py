from bs4 import BeautifulSoup
import requests
import prettytable
from selenium import webdriver
try:
    url = "http://www.pdfdrive.com/"
    html = requests.get(url)
    bs = BeautifulSoup(html.content, 'html.parser')
    title = bs.find("title")
    ul = bs.findAll('a')
    #print(len(ul))
    '''for x in range(35, 86, 2):
        print(str(x) + "::::: " + str(ul[x]['href']))'''
    table = prettytable.PrettyTable()
    table.field_names = ['index of book', 'id of book', 'name of book', 'href-tag']
    i=1
    for x in range(35, 86, 2):
        table.add_row([i, "(" + str(x) + ")", ul[x].text.strip(), ul[x]['href']])
        i+=1
    print(table)
    #print()
    inp = int(input("Select the id of the book you want:"))
    book = requests.get(url+ul[inp]['href'])
    print(book.status_code)
    if book.status_code == 200:
        bookbs = BeautifulSoup(book.content, 'html.parser')
        print(bookbs.find('h1', attrs={'class': 'ebook-title'}).text.strip())
        fileinfo = bookbs.find('div', attrs={'class': 'ebook-file-info'})
        #print(fileinfo)
        ls = fileinfo.find_all('span')
        #print(ls)
        '''for x in ls:
            print(x.text.strip())'''
        print("No.of pages:" + ls[0].text.strip())
        print("Year of publication:" + ls[2].text.strip())
        print("Size of file:" + ls[4].text.strip())
        print("No.of downloads:" + ls[6].text.strip())
        print("Language:" + ls[8].text.strip())
        '''authorinit = bookbs.find('a', attrs={'class' : 'card-author'})
        author = authorinit.find('span')
        print("Author:" + author.text.strip())'''
        buttons = bookbs.find('div', attrs={'class': 'ebook-buttons'})
        download = buttons.find('span', attrs={'id': 'download-button'})
        print("\n\n")
        print("1." + download.find('a').text.strip())
        #print(url+ul[inp]['href'])
        print(url+download.find('a')['href'])
        bookpagehtml = requests.get('http://www.pdfdrive.com/'+download.find('a')['href'])
        print(bookpagehtml.status_code)
        ''' bookpage =BeautifulSoup(bookpagehtml.content, 'html.parser')
        file = bookpage.find('a', attrs={'class': 'btn btn-success btn-responsive'})'''
        bk = BeautifulSoup(bookpagehtml.content, 'html.parser')
        driver = webdriver.Chrome('/media/sachmo/EE3A164B3A161167/WebScraping/chromedriver')
        driver.get(url+download.find('a')['href'])
        
        print(bk)

        driver.close()
except ConnectionError as e:
    print(e)

#bs.prettify()
'''print(title.text)
#print(type(title))
text1 = bs.find('div', attrs={'class': "box-title"})
txt = list(text1)
print(txt[0].strip("\n"), end=' ')
print(txt[1].text.strip())
ul1 = bs.find('div', attrs={'class': "files-new"})
#ul = bs.find('div', attrs={'class': "dialog-left"})
ul = bs.find('img')
innerdiv = bs.find_all('a')
#ahref = [div.find('img') for div in ul]
#ahref = innerdiv.find_all('a')

for a in ul:
    print(a['title'])
#print(type(li))'''
