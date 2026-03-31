### Create a regular expression pattern to extract URLs
# from a given text string. Test it with a sample text
# containing URLs.

import re
def validate_url(url_address):
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+|www.\.[-\w.]+\.[a-zA-Z]{2,}'
    urls = re.findall(url_pattern, url_address)
    return urls

sample_text = input("Write an url address: ")
if validate_url(sample_text):
    print("Valid URL")
else:
    print("Invalid URL")
