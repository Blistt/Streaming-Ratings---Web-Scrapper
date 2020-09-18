import requests
import json
import csv
import time
import random



# Retrieves HTML, parses it and stores recent users from MyAnimeList in text file
def scrapper(username):
    # Concatenates url for this user's list
    url = 'https://myanimelist.net/animelist/' + username + '/load.json?status=7&offset='

    response = "."
    counter = 0

    ratings = [username]

    # Iterates through all anime's in json response to extract the desired info from each
    while response:
        response = requests.get(url + str(counter)).json()
        if isinstance(response, dict):
            return

        if response:
            for anime in response:
                ratings.append(anime['anime_title'])
                ratings.append(str(anime['score']))
                ratings.append(str(anime['anime_id']))
                ratings.append(str(anime['status']))

        counter += 300

    #Stores user's anime ratings in csv file
    with open('ratings_matrix.csv', 'a+', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(ratings)

def line_counter(file):
    tempfile = open('ratings_matrix.csv', 'r', newline='', encoding="utf-8")
    lines = tempfile.readlines()
    print("te quedaste en " + str(len(lines)) + " inepto de mierda")
    return len(lines)



def main():
    # Initializes file with list of usernames
    user_list = open("user_list.txt", "r").readlines()

    # Counts the number of users in your file in case myanimelist detects us
    current_user = line_counter('user_matrix.csv') + 1

    for i in range(current_user, len(user_list)):
        scrapper(user_list[i].rstrip('\n'))
        print("Getting list of user " + str(i))

        # Sets a random time interval between 1 and 13 seconds to avoid detection (random step is of .2 seconds)
        sleep_interval = random.randint(5, 70) / 5
        time.sleep(sleep_interval)


main()


