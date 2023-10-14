# dark-spider

Dark-spider is a dark web crawler designed to navigate and index content on the dark web. It crawls through .onion web pages, and scrapes all the hyperlinks on those pages. The crawler goes on recursively upto a certain depth, and stores the links in a tree-like structure in json format, for futher analysis.

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

Visual representation of the .json file.
![crawled3](https://github.com/Arjun4522/dark-spider/assets/94633408/fb23c96a-c422-483a-a7e9-14b544c09bca)




    
