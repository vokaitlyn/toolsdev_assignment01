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

keyword = input("Please enter any keyword (press enter to continue):")
print("You entered the keyword: ", keyword)


#The Verge
for article in verge_news.articles:
	title = article.title
	author = article.authors
	summary = article.summary
	article.download()
	article.parse()
	article.nlp()
	article.keywords
	article.html

	if keyword in article.keywords:
		print(article.title, ' - ', article.authors)
		print(article.summary)
		print('\n')

		summary.write(aritcle.title)
		summary.write(' - ')
		summary.write(article.authors)
		summary.write('\n')
		summary.write(article.summary)
		summary.write('\n')
		summary.write('\n')

#Polygon
for article in polyg_news.articles:
	title = article.title
	author = article.authors
	summary = article.summary
	article.download()
	article.parse()
	article.nlp()
	article.keywords
	article.html

	if keyword in article.keywords:
		print(article.title, ' - ', article.authors)
		print(article.summary)
		print('\n')

		summary.write(aritcle.title)
		summary.write(' - ')
		summary.write(article.authors)
		summary.write('\n')
		summary.write(article.summary)
		summary.write('\n')
		summary.write('\n')

#Games
for article in games_news.articles:
	title = article.title
	author = article.authors
	summary = article.summary
	article.download()
	article.parse()
	article.nlp()
	article.keywords
	article.html

	if keyword in article.keywords:
		print(article.title, ' - ', article.authors)
		print(article.summary)
		print('\n')

		summary.write(aritcle.title)
		summary.write(' - ')
		summary.write(article.authors)
		summary.write('\n')
		summary.write(article.summary)
		summary.write('\n')
		summary.write('\n')


summary.close()
