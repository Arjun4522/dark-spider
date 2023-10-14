# dark-spider

Dark-spider is a dark web crawler designed to navigate and index content on the dark web. It uses the tor service and crawls through the links on various web pages recursively, up to a specified depth. The scraped links are saved in a JSON file for further analysis or use.

## Dependencies

requests: To make HTTP requests.
BeautifulSoup: For HTML parsing.
stem and stem.control.Controller: For controlling and switching IP addresses through the Tor network.
socks: For configuring the session with SOCKS proxy to route traffic through Tor.
