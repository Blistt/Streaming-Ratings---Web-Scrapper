from bs4 import BeautifulSoup
import requests
import time


#Retrieves HTML, parses it and stores recent users from MyAnimeList in text file
def scrapper():
    #Initializes file were ratings will be stored
    rating_matrix = open("ratings_matrix.txt", "a+")

    source = requests.get('https://myanimelist.net/animelist/blisk?status=2').text

    #Convers HTML to lxml in preparation for parsing
    soup = BeautifulSoup(source, 'lxml')

    #Parses HTML to retrieve and store usernames
    unsplit_list = soup.find('table', class_='list-table')["data-items"]

    #Manually parses ; delimited anime list data
    split_list = unsplit_list.split(",")


    for i in split_list:
        print(i)

    score_index = 1
    title_index = 5
    id_index = 8

    # while title_index < (len(split_list) - 24):
    #     # If anime_title's last character is not " then concatenate next line to anime title
    #     # and add 1 to title index count
    #     if split_list[title_index][len(split_list[title_index])-1] != "\"":
    #         split_list[title_index] = split_list[title_index] + split_list[title_index + 1]
    #         score_index += 1
    #         title_index += 1
    #         id_index += 1
    #
    #     print(split_list[title_index])
    #     title_index += 28

def main():
    #Initializes file with list of usernames
    user_list = open("user_list.txt", "r")


    scrapper()
    print("Getting list of user no.: ")
    time.sleep(2)

main()




