from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

class NewsRetriever:
    def __init__(self):
        self.api_key = os.getenv("NEWSAPI_KEY")
        self.newsapi = NewsApiClient(api_key=self.api_key)

    def get_articles(self, topic, max_articles=10):
        """Retrieve articles for a given topic."""
        try:
            response = self.newsapi.get_everything(
                q=topic,
                language='en',
                sort_by='relevancy',
                page_size=max_articles
            )
            
            if response['status'] == 'ok':
                return [{
                    'title': article['title'],
                    'content': article['content'] or article['description'],
                    'url': article['url']
                } for article in response['articles']]
            return []
        except Exception as e:
            print(f"Error retrieving articles: {e}")
            return []
