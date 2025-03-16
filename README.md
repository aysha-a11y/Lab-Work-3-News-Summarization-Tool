# Lab-Work-3-News-Summarization-Tool
News Retrieval: Fetches articles from NewsAPI based on user input.

Embeddings & Search: Uses TF-IDF for efficient text embeddings, stored in ChromaDB.

Summarization: Provides both brief and detailed summaries using Groq’s mixtral-8x7b-32768 model.

User Preferences: Saves preferred topics and tracks search history.

Simple CLI Interface: Offers an easy-to-use command-line menu for interaction.


--------------------------------Implementation Steps----------------------------------------------------

Project Setup: Installed necessary dependencies (langchain, langchain-groq, requests, scikit-learn, langchain-chroma)


****API Integration:

Retrieved news using NewsAPI

Used Groq for text summarization instead of OpenAI

****Embedding and Storage:

Implemented TF-IDF embeddings for efficient search

Stored embeddings using ChromaDB

****Summarization:

Created brief and detailed summaries with Groq

Optimized performance with RunnableSequence for chaining

****User Preferences and History:

Implemented a system to store and retrieve user preferences

Tracked past searches for a personalized experience

****Error Handling & Debugging:

Fixed API key loading issues

Resolved embedding dimension mismatches by standardizing TF-IDF vector size

----CLI Menu Options----

Search for News: Enter a topic and receive summarized news

Save Preferred Topics: Store topics for future reference

View Saved Topics: See previously saved topics

View Search History: Check past searches

Exit: Close the application
