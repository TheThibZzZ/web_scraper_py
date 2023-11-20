import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = 'https://www.example.com'

# Effectuer la requête HTTP
response = requests.get(url)

# Vérifier si la requête a réussi (statut 200 OK)
if response.status_code == 200:
    # Analyser le contenu HTML avec Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Exemple d'extraction de données
    title = soup.title.text
    print(f'Titre de la page : {title}')

    # Exemple d'utilisation de sélecteurs CSS pour extraire des paragraphes
    paragraphs = soup.select('p')
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print(f'Erreur {response.status_code} lors de la requête HTTP.')
