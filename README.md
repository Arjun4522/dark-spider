# dark-spider

Dark-spider is a dark web crawler designed to navigate and index content on the dark web. It uses the tor service and recursively crawls through the links on various web pages, up to a specified depth. The scraped links are saved in a JSON file for further analysis or use.

## Dependencies

1. requests: To make HTTP requests.
2. BeautifulSoup: For HTML parsing.
3. stem and stem.control.Controller: For controlling and switching IP addresses through the Tor network.
4. socks: For configuring the session with SOCKS proxy to route traffic through Tor.

Install the dependecies using:

`sudo pip install -r requirements.txt`

The tor service should also be installed

`sudo apt install tor`

## Prerequisites

1. Generate 'tor_hash_password' using:

   `tor --hash-password <secretkey>`

2. Edit tor configuration file (/etc/tor/torrc):

   `sudo nano /etc/tor/torrc`

   Append following lines at the end of file:

   `SocksPort 9050`
   
   `ControlPort 9051
    HashedControlPassword 'tor_hash_password'`

## Usage

Run the python script:

   `sudo python3 darkspider.py`

## Results

The scraped links are store in the 'scraped_onion_links_tree.json' file, in a tree structure.
![crawled3](https://github.com/Arjun4522/dark-spider/assets/94633408/fb23c96a-c422-483a-a7e9-14b544c09bca)




    
