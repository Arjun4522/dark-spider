import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
from stem import Signal
from stem.control import Controller
import socks

def change_ip_address():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="tor_config_password")
        controller.signal(Signal.NEWNYM)

def scrape_onion_links(url, max_depth=3, current_depth=1, visited_links=None, max_links_per_page=2):
    if visited_links is None:
        visited_links = set()

    change_ip_address()  

    session = requests.session()
    session.proxies = {
        "http": "socks5h://localhost:9050", 
        "https": "socks5h://localhost:9050"
    }

    try:
        print(f"Scraping: {url}")
        response = session.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    links = [a['href'] for a in soup.find_all('a', href=True)]

    current_page_links = []

    link_count = 0
    for link in links:
        if link_count >= max_links_per_page:
            break

        absolute_link = urljoin(url, link)
        if absolute_link not in visited_links:
            visited_links.add(absolute_link)
            current_page_links.append(absolute_link)

            if current_depth < max_depth:
                scrape_onion_links(absolute_link, max_depth, current_depth + 1, visited_links, max_links_per_page=max_links_per_page)

    return current_page_links

root_url = input("\nEnter the root .onion URL: ")
max_depth = int(input("Enter the maximum depth: "))
max_links_per_page = int(input("Enter the maximum links per page: "))

print("\nScraping .onion links...\n")

visited_links = set()

scraped_links = {root_url: scrape_onion_links(root_url, max_depth, 1, visited_links, max_links_per_page=max_links_per_page)}

with open('scraped_onion_links_tree.json', 'w') as json_file:
    json.dump(scraped_links, json_file, indent=4)

print(f'\nResult saved in "scraped_onion_links_tree.json"\n')
