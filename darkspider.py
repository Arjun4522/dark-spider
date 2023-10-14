import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
from stem import Signal
from stem.control import Controller
import socks

# Function to change the IP address through Tor
def change_ip_address():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="16:D1A5FD4AAEFA57B9603244222A2D9481176AC38FA45511453E9E236DB5")
        controller.signal(Signal.NEWNYM)

# Function to scrape .onion links using Tor
def scrape_onion_links(url, max_depth=3, current_depth=1, visited_links=None, max_links_per_page=2):
    if visited_links is None:
        visited_links = set()

    change_ip_address()  # Change to a new IP address through Tor

    # Configure the session with SOCKS proxy
    session = requests.session()
    session.proxies = {
        "http": "socks5h://localhost:9050",  # Replace with your SOCKS proxy configuration
        "https": "socks5h://localhost:9050"
    }

    # Make an HTTP request to the .onion URL through Tor
    try:
        print(f"Scraping: {url}")
        response = session.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and collect links on the page
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Create a dictionary for the current .onion URL
    current_page_links = []

    # Process and append the links, limiting to max_links_per_page
    link_count = 0
    for link in links:
        if link_count >= max_links_per_page:
            break

        absolute_link = urljoin(url, link)
        if absolute_link not in visited_links:
            visited_links.add(absolute_link)
            current_page_links.append(absolute_link)

            # Recursively scrape .onion links up to the specified depth
            if current_depth < max_depth:
                scrape_onion_links(absolute_link, max_depth, current_depth + 1, visited_links, max_links_per_page=max_links_per_page)

    return current_page_links

# Input parameters
root_url = input("\nEnter the root .onion URL: ")
max_depth = int(input("Enter the maximum depth: "))
max_links_per_page = int(input("Enter the maximum links per page: "))

print("\nScraping .onion links...\n")

# Create a set to keep track of visited links
visited_links = set()

# Start scraping from the root .onion URL using Tor
scraped_links = {root_url: scrape_onion_links(root_url, max_depth, 1, visited_links, max_links_per_page=max_links_per_page)}

# Save the result to a JSON file
with open('scraped_onion_links_tree.json', 'w') as json_file:
    json.dump(scraped_links, json_file, indent=4)

print(f'\nResult saved in "scraped_onion_links_tree.json"\n')
