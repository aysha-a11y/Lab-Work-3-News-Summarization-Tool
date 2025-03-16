from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document

class Summarizer:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0,
            model_name="gpt-3.5-turbo"
        )

    def create_brief_summary(self, content):
        """Create a brief 1-2 sentence summary."""
        docs = [Document(page_content=content)]
        chain = load_summarize_chain(
            self.llm,
            chain_type="stuff",
            prompt="Summarize this content in 1-2 sentences."
        )
        return chain.run(docs)

    def create_detailed_summary(self, content):
        """Create a detailed paragraph summary."""
        docs = [Document(page_content=content)]
        chain = load_summarize_chain(
            self.llm,
            chain_type="map_reduce",
            prompt="Provide a detailed paragraph summary of this content."
        )
        return chain.run(docs)