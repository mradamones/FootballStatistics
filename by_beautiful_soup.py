import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/en/players/"

# Pobierz zawartość strony
response = requests.get(url)
content = response.content

# Użyj BeautifulSoup do analizy zawartości
soup = BeautifulSoup(content, "html.parser")

# Tutaj możesz dalej analizować zawartość strony i ekstrahować potrzebne informacje
# Na przykład, możesz znaleźć elementy zawierające linki do poszczególnych piłkarzy

# Przykład: znajdź wszystkie linki do piłkarzy na stronie
player_links = soup.find_all("img", class_="poptip")

# Wyświetl znalezione linki
for link in player_links:
    print(link["data-tip"])
