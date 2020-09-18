from bs4 import BeautifulSoup
import requests
import lxml
import time


#Retrieves HTML, parses it and stores recent users from MyAnimeList in text file
def scrapper():
    user_list = open("user_list.txt", "a+")
    source = requests.get('https://myanimelist.net/users.php').text

    #Convers HTML to lxml in preparation for parsing
    soup = BeautifulSoup(source, 'lxml')

    #Parses HTML to retrieve and store usernames
    for user in soup.find_all('div', style='margin-bottom: 7px;'):
        username = "\n" + user.text
        user_list.write(username)



def main():
    a = True
    count = 0

    while(a):
        count += 1
        scrapper()
        print("Getting wave of users number " + str(count))
        time.sleep(2)

main()




