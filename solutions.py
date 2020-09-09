import requests
import bs4

# Task: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HTML text
# from the homepage

res = requests.get('http://quotes.toscrape.com')
print(res.text)

# Task: Get the names of all the authors on the first page

soup = bs4.BeautifulSoup(res.text, 'lxml')
authors = set()
for author in soup.select('.author'):
    authors.add(author.text)

print(authors)

# Task: Create a list of all the quotes on the first page

quote_list = []
for quote in soup.select('.quote .text'):
    quote_list.append(quote.text)

print(quote_list)

# Task: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top
# right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath
# each quote, try to find a class only present in the top right tags, perhaps check the span.

top_tags = []
for tag in soup.select('.col-md-4.tags-box a'):
    top_tags.append(tag.text)

print(top_tags)

# Task: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/.
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique
# authors on the website.

all_authors = set()
base_url = 'http://quotes.toscrape.com/page/{}/'
n = 1

while True:
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    if 'No quotes found!' in soup.select('.col-md-8')[1].text:
        break
    else:
        for author in soup.select('.author'):
            all_authors.add(author.text)
    n += 1

print(all_authors)