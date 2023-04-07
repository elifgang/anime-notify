from bs4 import BeautifulSoup
import requests
import re
import datetime
from notifypy import Notify

# Obtenemos todo el código HTML
def request(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup

# Obtenemos un link completo (ej. /anime/{id} 
def complete_link(url): # We return the complete link
    url_input = "https://notify.moe{}".format(url)
    return url_input

def search_Anime(name):
    try:
        soup = request("https://notify.moe/explore")
        anime_names = soup.select("div.image-title")
        list_of_animes = ()
        for names in anime_names:
            if name.lower() in names.text.lower():  
                list_of_animes += (names.text,)
        return list_of_animes
    except Exception:
        return f"Hubo un error: {Exception}"
    
# Obtenemos la {id} del anime
def get_AnimeLink(inputAnime): # Obtain the sought anime link (ex: /anime/asGd86)
    try:
        soup = request("https://notify.moe/explore")
        anime_links = soup.select("div.anime-grid-cell a")
        dic_links = {}
        for anime_link in anime_links:
            dic_links[anime_link.find('img')['alt'].lower()] = anime_link['href']
        anime_name = next((key for key in dic_links.keys() if inputAnime in key.lower()), None)
        return dic_links.get(anime_name) 
    except:
        return "Error 42: Fallo al obtener el link del anime."

# Obtenemos el nombre (refactor)
def get_AnimeName(link):
    try:
        soup = request(complete_link(link))
        return soup.find("h1", class_="anime-title mountable").text
    except:
        return "Error 43: Fallo al obtener el nombre."

# def get_AnimeEpisode(url, episode=None):
#     try:
#         soup = request(complete_link(url))
#         latest_episode = soup.select("div.episodes a[data-available=true]")
#         count = len(latest_episode)
#         if episode is not None:
#             episode_number = count - episode
#             if episode_number >= 0:
#                 return episode_number + 1
#             else:
#                 return "Error: Episodio no disponible"
#         else:
#             return count
#     except:
#         return "Error: Fallo al obtener el episodio."

def get_AnimeEpisode(url):
    try:
        soup = request(complete_link(url))
        latest_episode = soup.select("div.episodes a[data-available=true]")
        count = len(latest_episode)
        return count
    except:
        return "Error 44: Fallo al obtener el episodio."
    
def get_state_episode(url): # Obtain episode state
    try:
        soup = request(complete_link(url))
        latest_episode = soup.select_one("div.episodes a[data-available='true'] span.episode-title")
        if latest_episode and latest_episode.get_text() == "-":
            return True
        else:
            return False
    except:
        return "Error 45: Fallo al obtener el estado del episodio."

def get_restTime(url, episode):
    try:
        soup = request(complete_link(url))
        dates = [elem.text for elem in soup.select("div.episodes a")]
        match = re.search(r'.*(\w{3}, \d{2} \w{3} \d{4})', dates[episode])
        if match:
            date_str = match.group(1)
            date = datetime.datetime.strptime(date_str, "%a, %d %b %Y")
            now = datetime.datetime.now()
            date1 = datetime.date(date.year, date.month, date.day)
            date2 = datetime.date(now.year, now.month, now.day)
            daysLeft = abs(date2 - date1)
            return daysLeft.days
    except:
        return "Error 46: Fallo al obtener el tiempo restante."

# enviar notificacion
def send_notification(title, message):
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.send()


# def main():
#     try:
#         inputAnime = input("What anime is going to be notifiyed? \n") # Anime to search
#         links = get_AnimeLink(inputAnime)
#         anime_name = get_AnimeName(links)
#         episode_number = get_AnimeEpisode(links)
#         state = get_state_episode(links)
#         time = get_restTime(links, episode_number)
#         if state == False:
#             send_notification("Anime Notification", f"Episode {episode_number+1} of {anime_name} is avaiable.{time}")
#         else:
#             send_notification("Anime Notification", f"Episode {episode_number+1} of {anime_name} it`s not avaiable, it`s going to air in {time} days.")
#     except requests.exceptions.RequestException as exceptMessage:
#         raise("[378 Error]:", exceptMessage)
        
# main()
