import requests
from bs4 import BeautifulSoup

# github_user = input('Input Github User: ') #prosimy uzytkownika o podanie nazwy profilu github
url = 'https://github.com/abrakadabror?tab=repositories'

# url = 'https://github.com/' + github_user #tworzony jest adres URL na podstawie ww. przekazanej nazwy
response = requests.get(url) 
if response.status_code == 200:
    print("Everything's gonna be alright")
elif response.status_code == 404:
    print("Fatall error - it's a faulty operation")
else:
    print('Give me a patience to live in this place...an error occured!')

soup = BeautifulSoup(response.content, 'html.parser')
# profile_image = soup.find('img', {'alt': 'Avatar'})['src']
# print(profile_image)

# logo_github  = soup.find('svg', class_ =  'octicon-mark-github')
# logo_src = logo_github.get('src')
# print(logo_src)
# program do wydrukowania linku do avatara uztkownika github

repositories = soup.find_all(class_ = 'd-inline-block mb-1')
repository_list = []
for repository in repositories:
    repository_name = repository.text.strip()
    repository_list.append(repository_name)
repository_dict = dict(zip(range(1, len(repository_list)+ 1), repository_list)) 
#W powyższym kodzie, repository_dict jest słownikiem, który został utworzony za pomocą funkcji dict() i zip() z listy repository_list
for key, value in repository_dict.items(): # W pętli for, dla każdej iteracji, key przyjmie kolejne klucze  drukujemy wyniki w jednej linii jeden pod drugim
    print(f"Key: {key} , Value: {value}")
