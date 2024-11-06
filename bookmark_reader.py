from bs4 import BeautifulSoup

soup = BeautifulSoup()
with open('bookmarks_11_6_24.html', encoding="utf-8") as f:
    #  soup = BeautifulSoup(f.read(), 'lxml')
    soup = BeautifulSoup(f, features="html.parser")

dt = soup.find_all('dt')
folder_name =''
for i in dt:
    n = i.find_next()
    if n.name == 'h3':
        folder_name = n.text
        continue
    else:
        print(f'url = {n.get("href")}')
        print(f'website name = {n.text}')
        print(f'add date = {n.get("add_date")}')
        print(f'folder name = {folder_name}')
    print()