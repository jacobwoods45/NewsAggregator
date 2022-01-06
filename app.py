import feedparser
from pymongo import MongoClient

client = MongoClient('mongodb+srv://jacobwoods45:Sharpie78!@newsaggregatorcluster.ncifr.mongodb.net/NewsAggregator?retryWrites=true&w=majority')
db = client["NewsAggregator"]
clips = db["NewsClips"]

feed_links = ["https://rss.nytimes.com/services/xml/rss/nyt/US.xml", "https://feeds.npr.org/1001/rss.xml", "https://www.technologyreview.com/feed/", "http://feeds.bbci.co.uk/news/world/rss.xml"]
feed_names = ["NYT", "NPR", "MIT TECH", "BBC WORLD NEWS"]
def get_news_feed(feed_link, feed_name):
    NewsFeed = feedparser.parse(feed_link)
    
    for post in NewsFeed.entries:
        print (post.title)
        
        print(feed_name)
        print(post.published)
        if feed_name != 'REDDIT':
            print(post.description)
        print(post.link)
        print ("\n")

        post_dict = {
            'title': post.title,
            'feed_name': feed_name,
            'published': post.published,
            'description': post.description,
            'link': post.link 
            }
        
        clips.insert_one(post_dict).inserted_id
def delete_all_feeds():
    clips.delete_many({})
    print("News Feeds Deleted")

def log_all_feed(feed_links, feed_names):
    feed_index = 0
    while(feed_index < len(feed_links)):
        get_news_feed(feed_links[feed_index], feed_names[feed_index] )
        feed_index+=1
    print("News Feeds Logged")

delete_all_feeds()
log_all_feed(feed_links, feed_names)