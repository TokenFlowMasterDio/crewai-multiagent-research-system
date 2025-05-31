import requests
import json
from typing import List, Dict, Any
from abc import ABC, abstractmethod

class BaseTool(ABC):
    """Simple base tool class compatible with CrewAI."""
    
    def __init__(self):
        self.name = "base_tool"
        self.description = "Base tool"
    
    @abstractmethod
    def _run(self, query: str) -> str:
        """Run the tool with a query."""
        pass

class SerperSearchTool(BaseTool):
    """Real web search using Serper API (Google Search)."""
    
    def __init__(self, api_key: str):
        super().__init__()
        self.name = "serper_search"
        self.description = "Search the web using Serper API for real-time information"
        self.api_key = api_key
        self.base_url = "https://google.serper.dev/search"
    
    def _run(self, query: str) -> str:
        """Execute real web search using Serper."""
        try:
            headers = {
                "X-API-KEY": self.api_key,
                "Content-Type": "application/json"
            }
            
            payload = {
                "q": query,
                "num": 5
            }
            
            response = requests.post(self.base_url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            results = []
            if "organic" in data:
                for i, result in enumerate(data["organic"][:5], 1):
                    title = result.get("title", "")
                    link = result.get("link", "")
                    snippet = result.get("snippet", "")
                    
                    results.append(f"**Source {i}: {title}**\nURL: {link}\nSummary: {snippet}\n---")
            
            if results:
                return f"Web Search Results for '{query}':\n\n" + "\n".join(results)
            else:
                return f"No results found for '{query}'"
                
        except Exception as e:
            return f"Search error: {str(e)}"

class TavilySearchTool(BaseTool):
    """Real web search using Tavily API."""
    
    def __init__(self, api_key: str):
        super().__init__()
        self.name = "tavily_search"
        self.description = "Search the web using Tavily API for AI-optimized results"
        self.api_key = api_key
        self.base_url = "https://api.tavily.com/search"
    
    def _run(self, query: str) -> str:
        """Execute web search using Tavily."""
        try:
            headers = {
                "Content-Type": "application/json"
            }
            
            payload = {
                "api_key": self.api_key,
                "query": query,
                "search_depth": "basic",
                "include_answer": True,
                "include_sources": True,
                "max_results": 5
            }
            
            response = requests.post(self.base_url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            results = []
            if "results" in data:
                for i, result in enumerate(data["results"][:5], 1):
                    title = result.get("title", "")
                    url = result.get("url", "")
                    content = result.get("content", "")
                    
                    results.append(f"**Source {i}: {title}**\nURL: {url}\nSummary: {content[:200]}...\n---")
            
            if results:
                return f"Web Search Results for '{query}':\n\n" + "\n".join(results)
            else:
                return f"No results found for '{query}'"
                
        except Exception as e:
            return f"Search error: {str(e)}"

class BraveSearchTool(BaseTool):
    """Real web search using Brave Search API."""
    
    def __init__(self, api_key: str):
        super().__init__()
        self.name = "brave_search"
        self.description = "Search the web using Brave Search API for unbiased results"
        self.api_key = api_key
        self.base_url = "https://api.search.brave.com/res/v1/web/search"
    
    def _run(self, query: str) -> str:
        """Execute web search using Brave."""
        try:
            headers = {
                "Accept": "application/json",
                "Accept-Encoding": "gzip",
                "X-Subscription-Token": self.api_key
            }
            
            params = {
                "q": query,
                "count": 5,
                "offset": 0,
                "mkt": "en-US",
                "safesearch": "moderate"
            }
            
            response = requests.get(self.base_url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            results = []
            if "web" in data and "results" in data["web"]:
                for i, result in enumerate(data["web"]["results"][:5], 1):
                    title = result.get("title", "")
                    url = result.get("url", "")
                    description = result.get("description", "")
                    
                    results.append(f"**Source {i}: {title}**\nURL: {url}\nSummary: {description}\n---")
            
            if results:
                return f"Web Search Results for '{query}':\n\n" + "\n".join(results)
            else:
                return f"No results found for '{query}'"
                
        except Exception as e:
            return f"Search error: {str(e)}"

class EnhancedMockSearchTool(BaseTool):
    """Enhanced mock search with realistic links and sources."""
    
    def __init__(self):
        super().__init__()
        self.name = "enhanced_mock_search"
        self.description = "Enhanced mock search with realistic sources and links"
    
    def _run(self, query: str) -> str:
        """Execute enhanced mock search with real-looking sources."""
        
        ai_sources = [
            {
                "title": "OpenAI Research - Latest AI Developments",
                "url": "https://openai.com/research/",
                "summary": "Cutting-edge research in large language models, safety, and alignment."
            },
            {
                "title": "Google AI Research - Machine Learning Advances", 
                "url": "https://research.google/research-areas/machine-intelligence/",
                "summary": "Breakthrough research in neural networks, computer vision, and NLP."
            },
            {
                "title": "MIT Technology Review - AI News",
                "url": "https://www.technologyreview.com/topic/artificial-intelligence/",
                "summary": "Latest developments and analysis in artificial intelligence."
            },
            {
                "title": "ArXiv AI Papers - Recent Research",
                "url": "https://arxiv.org/list/cs.AI/recent", 
                "summary": "Latest academic papers and research in artificial intelligence."
            }
        ]
        
        results = []
        for i, source in enumerate(ai_sources, 1):
            results.append(f"**Source {i}: {source['title']}**\nURL: {source['url']}\nSummary: {source['summary']}\n---")
        
        return f"Web Search Results for '{query}':\n\n" + "\n".join(results) + "\n\nNote: Using enhanced mock search with real research URLs."

class ToolsManager:
    """Enhanced tools manager with real web search capabilities."""
    
    def __init__(self, settings):
        self.settings = settings
        self._initialize_tools()
    
    def _initialize_tools(self):
        """Initialize all available tools."""
        self.search_tools = []
        
        # Add real search tools if API keys available
        if hasattr(self.settings, 'serper_api_key') and self.settings.serper_api_key:
            try:
                self.search_tools.append(SerperSearchTool(self.settings.serper_api_key))
                print("✅ Serper (Google) search tool initialized")
            except Exception as e:
                print(f"⚠️  Serper tool failed: {e}")
        
        if hasattr(self.settings, 'tavily_api_key') and self.settings.tavily_api_key:
            try:
                self.search_tools.append(TavilySearchTool(self.settings.tavily_api_key))
                print("✅ Tavily search tool initialized")
            except Exception as e:
                print(f"⚠️  Tavily tool failed: {e}")
        
        if hasattr(self.settings, 'brave_api_key') and self.settings.brave_api_key:
            try:
                self.search_tools.append(BraveSearchTool(self.settings.brave_api_key))
                print("✅ Brave search tool initialized")
            except Exception as e:
                print(f"⚠️  Brave tool failed: {e}")
        
        # Enhanced mock search as fallback
        if not self.search_tools:
            self.search_tools.append(EnhancedMockSearchTool())
            print("✅ Enhanced mock search tool initialized")
    
    def get_research_tools(self) -> List[BaseTool]:
        """Get tools for research agents."""
        return self.search_tools
    
    def get_writing_tools(self) -> List[BaseTool]:
        """Get tools for writing agents."""
        return []
    
    def get_verification_tools(self) -> List[BaseTool]:
        """Get tools for fact-checking agents."""
        return self.search_tools
    
    def get_document_tools(self) -> List[BaseTool]:
        """Get tools for document processing agents."""
        return []