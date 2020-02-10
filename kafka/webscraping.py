import sys
from time import sleep
import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }

def get_movies(url):
    movies_list = []
    print("Fetching movies ...")

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            links = soup.select('.card-right')
            idx = 0
            for link in links:
                if idx > 5:
                    continue
                movie_name=link.h4.text
                day = link.span.select('.day')[0].text
                sleep(2)
                movies_list.append(movie_name+':'+day)
                idx += 1
    except Exception as ex:
        print('Exception in get_recipes')
        print(str(ex))
    finally:
        return movies_list


if __name__ == '__main__':
    all_movies = get_movies('https://in.bookmyshow.com/bengaluru/movies/comingsoon')
    print(all_movies)
