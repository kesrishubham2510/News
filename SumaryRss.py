import feedparser

newsFeed= feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

entry1= newsFeed.entries[1]
for news in newsFeed.entries:
  print(news.title+ "\n")
  print(news.published+ "\n")
  print(news.summary+ '\n')
  print(news.link+ '\n')