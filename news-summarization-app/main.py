from news_retriever import NewsRetriever
from embedding_engine import EmbeddingEngine
from summarizer import Summarizer
from user_manager import UserManager

def main():
    news_retriever = NewsRetriever()
    embedding_engine = EmbeddingEngine()
    summarizer = Summarizer()
    user_manager = UserManager()

    while True:
        print("\nNews Summarization Application")
        print("1. Search for news")
        print("2. Save topic preference")
        print("3. View saved topics")
        print("4. View search history")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            topic = input("Enter topic to search: ")
            articles = news_retriever.get_articles(topic)
            
            if articles:
                embedding_engine.create_embeddings(articles)
                user_manager.add_to_history(topic)
                
                print("\nChoose summary type:")
                print("1. Brief (1-2 sentences)")
                print("2. Detailed (paragraph)")
                summary_type = input("Enter choice (1-2): ")

                for i, article in enumerate(articles, 1):
                    content = f"{article['title']}\n{article['content']}"
                    print(f"\nArticle {i}:")
                    if summary_type == "1":
                        summary = summarizer.create_brief_summary(content)
                    else:
                        summary = summarizer.create_detailed_summary(content)
                    print(summary)
                    print(f"Source: {article['url']}")
            else:
                print("No articles found for this topic.")

        elif choice == "2":
            topic = input("Enter topic to save: ")
            user_manager.add_topic(topic)
            print(f"Topic '{topic}' saved.")

        elif choice == "3":
            topics = user_manager.get_topics()
            print("Saved topics:", ", ".join(topics) if topics else "None")

        elif choice == "4":
            history = user_manager.get_history()
            for item in history:
                print(f"Query: {item['query']} (Time: {item['timestamp']})")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()