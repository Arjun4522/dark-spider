# dark-spider

## Introduction

Dark-spider is a dark web crawler designed to navigate and index content on the dark web. It uses the tor service and crawls through the links on various web pages recursively, up to a specified depth. The scraped links are saved in a JSON file for further analysis or use.

## Dependencies

1. requests: To make HTTP requests.
2. BeautifulSoup: For HTML parsing.
3. stem and stem.control.Controller: For controlling and switching IP addresses through the Tor network.
4. socks: For configuring the session with SOCKS proxy to route traffic through Tor.

Install the dependecies using:

`pip install -r requirements.txt`
