# Kaitlyn Vo
# ATCM 3311.0U1 - Assignment 01 
# June 12, 2020
import nltk
import newspaper
from newspaper import Article 


#News Articles 
verge_news = newspaper.build('https://www.theverge.com/', memoize_articles = False)
polyg_news = newspaper.build('https://www.polygon.com/', memoize_articles = False)
games_news = newspaper.build('https://www.gamespot.com/', memoize_articles = False)

summary = open('news_summary.txt', 'w')

nltk.download('punkt')

keyword = input("Please enter any keyword (press enter to continue): ")
print("You entered the keyword: ", keyword)

def printSummary(news):
#The Verge
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
		if summary != '':
			print(summary)
		if count > 5:
			break
		count += 1

printSummary(verge_news)
printSummary(polyg_news)
printSummary(games_news)

summary.close()
