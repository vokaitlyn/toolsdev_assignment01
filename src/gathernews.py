# Kaitlyn Vo
# ATCM 3311.0U1 - Assignment 01 
# June 12, 2020


import nltk
import newspaper
from newspaper import Article 
import webbrowser


# Articles 
verge_news = newspaper.build('https://www.theverge.com/search?q=', memoize_articles = False)
polyg_news = newspaper.build('https://www.polygon.com/search?q=', memoize_articles = False)
games_news = newspaper.build('https://www.pcgamer.com/search/?searchTerm=', memoize_articles = False)

summary = open('news_summary.txt', 'w')

nltk.download('punkt')

keyword = input("Please enter any keyword (press enter to continue): ")
print("You entered the keyword: ", keyword)

# Function
def printSummary(news):
	print(len(news.articles))
	count = 0
	for article in news.articles:
		title = article.title
		author = article.authors
		summary = article.summary
		article.download()
		article.parse()
		article.nlp()
		article.keywords
		article.html
		article.text
		if keyword in article.keywords:
			summary = (article.title)
			summary += (' - ')
			summary += (str(article.authors))
			summary += ('\n')
			summary += (article.summary)
			summary += ('\n')
			summary += ('\n')
		if summary != '':
			print(summary)
		if count > 10:
			break
		count += 1

printSummary(verge_news)
printSummary(polyg_news)
printSummary(games_news)

summary.close()

# Open up search results in browser
print("Opening Search Results in Browser :D")
webbrowser.open(verge_news.url + keyword)
webbrowser.open(polyg_news.url + keyword)
webbrowser.open(games_news.url + keyword)
