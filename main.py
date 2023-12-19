from bs4 import BeautifulSoup
import requests

def request(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup

def complete_link(url): 
    url_input = "https://notify.moe{}".format(url)
    return url_input

def animes_dictionary():
    soup = request("https://notify.moe/explore")
    anime_names = soup.select("div.explore-anime a img")
    anime_links = soup.select("div.anime-grid-cell a")
    anime_dictionary = {}
    for name, link in zip(anime_names, anime_links):
        anime_name = name.get("alt")
        anime_link = link.get("href")
        anime_dictionary[anime_name] = anime_link
    return anime_dictionary

def get_name(anime_name):
    key,_ = find(anime_name)
    return key

def get_link(anime_name):
    _, link = find(anime_name)
    return link

def find(anime_name):
    anime_dict = animes_dictionary()
    for key, value in anime_dict.items():
        if anime_name.lower() in key.lower():
            return key, value
    return None, None

def get_episode(anime_name, url=None):
    if url is None:
        url = complete_link(get_link(anime_name))
    soup = request(url)
    episodes = soup.select("div.episodes a")
    for episode in episodes:
        if episode.get("data-available") == "true":
            episode_number_element = episode.select_one("div.episode-number span")
            episode_number = episode_number_element.get_text(strip=True) if episode_number_element else None
    return episode_number


