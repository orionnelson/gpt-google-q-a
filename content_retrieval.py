from google import search
from bs4 import BeautifulSoup as soup
from ai4 import request as gpt3_response
import pickle as pkl
import hashlib
import os

SEARCHED_LOC = os.path.join(os.path.dirname(__file__), "searched")
if not os.path.exists(SEARCHED_LOC):
    os.mkdir(SEARCHED_LOC)

def encode(item):
	return hashlib.md5(item.encode('utf-8')).hexdigest()

def get_query_filename(query):
    return str(encode(query))+".pkl"

def check_query_exists(query):
    return os.path.exists(os.path.join(SEARCHED_LOC ,get_query_filename(query)))

def save_data(data, filename):
    with open(filename, 'wb') as f:
        pkl.dump(data, f)

def load_data(filename):
    with open(filename, 'rb') as f:
        return pkl.load(f)

# Process the HTML content of the search results.
def process_html_content_array(html_content,level="stupid"):
    response = ""
    if level == "stupid":
        for item in html_content:
            s = soup(item, 'html.parser')
            response += s.get_text()
    
    return response




# Ask the user for a search query.
text = ""
query = ""
while True and __name__ == "__main__" and text=="" and not check_query_exists(query):
    text = ""
    query = input("Enter your search: ")
    if query:
        urls, html_content =  search(' '.join(query.split()), 1)
        text = process_html_content_array(html_content)

# We Recieve a response from the user
if not check_query_exists(query):
    save_data((urls, html_content,text), os.path.join(SEARCHED_LOC ,get_query_filename(query)))
else:
    urls, html_content,text = load_data(os.path.join(SEARCHED_LOC ,get_query_filename(query)))
    #text = process_html_content_array(html_content)
#print(text)
if query:
    response = gpt3_response(text + "\n\n"+query + "\n The")
    print(response)
    while True:
        query = input("Enter your gpt-6b Query from Scraped Data or [CTL+C]: ")
        response = gpt3_response(text + "\n\n"+query + "\n The")
        print(response)
        print("\n\n\n")
