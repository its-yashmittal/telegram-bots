from requests import get
from bs4 import BeautifulSoup
movie_info = {}
def scraper(movie_name):
    search_url="https://www.imdb.com/find?q="+movie_name+"&ref_=nv_sr_sm"
    search_response = get(search_url)
    search_soup = BeautifulSoup(search_response.text, 'html.parser')
    search_result = search_soup.find('td', attrs={'class':'result_text'})
    print(search_result)
    movie_url = "https://www.imdb.com" + search_result.a['href']
    movie_response = get(movie_url)
    movie_soup = BeautifulSoup(movie_response.text, 'html.parser')
    movie_name = movie_soup.find('h1').text
    movie_info.update({'name':movie_name.replace('\xa0',' ')})
    movie_duration = movie_soup.find('time').text.strip()
    movie_info.update({'duration':movie_duration})
    release_date = movie_soup.find('a', attrs={'title':'See more release dates'}).text
    movie_info.update({'release date': release_date.strip()})
    storyline = movie_soup.find('div', attrs={'id':'titleStoryLine'})
    movie_info.update({'storyline':storyline.div.p.span.text.strip()})
    movie_genres = movie_soup.find('div', attrs={'class':'subtext'}).find_all('a')
    genre_list = []
    for genre in movie_genres:
        genre_list.append(genre.text)
    genre_list.pop()
    movie_info.update({'genres':genre_list})
    movie_cast = movie_soup.find('table', attrs={'class':'cast_list'}).find_all('a')
    cast_list = []
    for actor in movie_cast:
        cast_list.append(actor.text.strip())
    movie_info.update({'cast':cast_list})
    print(movie_info)
    return movie_info

scraper("avengers")