import requests
import bs4
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize

url = 'https://jamesclear.com/great-speeches/make-your-bed-by-admiral-william-h-mcraven'

page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
p_elems = [element.text for element in soup.find_all('p')]
speech = ''
for p in p_elems:
    speech += p

print("\nSummary of Make Your Bed speech:")
##print(summarize(speech, word_count=)) # or ratio=0.015
summary = summarize(speech, word_count=225)  # 190 is better
sentences = sent_tokenize(summary)
sents = set(sentences)
print(' '.join(sents))


