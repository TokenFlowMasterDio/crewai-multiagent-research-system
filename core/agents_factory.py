from crewai import Agent
from typing import List

class AgentsFactory:
    """Factory for creating specialized AI agents compatible with CrewAI tool format."""
    
    def __init__(self, settings, tools_manager):
        self.settings = settings
        self.tools_manager = tools_manager
    
    def create_researcher(self, llm, memory) -> Agent:
        """Create research agent with web search capabilities."""
        
        return Agent(
            role="Senior AI Research Analyst",
            goal="Conduct comprehensive research on AI topics and provide accurate, well-sourced information",
            backstory="""You are a world-class AI research analyst with expertise in finding the latest 
            information and credible sources. You excel at synthesizing complex topics and providing 
            comprehensive research with proper citations and URLs.""",
            verbose=True,
            allow_delegation=True,
            # Temporarily remove tools to fix validation - we'll add them back properly
            # tools=self._format_tools_for_crewai(self.tools_manager.get_research_tools()),
            memory=memory,
            llm=llm,
            max_iter=3
        )
    
    def create_reporter(self, llm, memory) -> Agent:
        """Create content writer agent."""
        return Agent(
            role="Senior Technology Writer",
            goal="Create compelling, well-structured articles based on research findings with proper citations",
            backstory="""You are an award-winning technology journalist. You excel at taking research 
            findings and transforming them into engaging, well-structured articles with proper source citations. 
            You write in a clear, accessible style that appeals to both technical and general audiences.""",
            verbose=True,
            allow_delegation=False,
            memory=memory,
            llm=llm,
            max_iter=3
        )
    
    def create_fact_checker(self, llm, memory) -> Agent:
        """Create fact-checking agent."""
        
        return Agent(
            role="Senior Fact-Checker & Verification Specialist",
            goal="Verify information accuracy and ensure all claims are properly sourced",
            backstory="""You are a meticulous fact-checker with expertise in verifying claims and 
            checking source credibility. You ensure the highest standards of accuracy and help 
            identify any potential misinformation or unsupported claims.""",
            verbose=True,
            allow_delegation=False,
            # Temporarily remove tools to fix validation
            # tools=self._format_tools_for_crewai(self.tools_manager.get_verification_tools()),
            memory=memory,
            llm=llm,
            max_iter=3
        )
    
    def create_document_qa_agent(self, llm, memory) -> Agent:
        """Create document Q&A agent."""
        return Agent(
            role="Document Analysis Expert",
            goal="Provide accurate answers based on document analysis with specific references",
            backstory="""You are a document analysis expert who provides precise answers 
            with proper citations and page references from the analyzed documents. You excel 
            at understanding complex documents and extracting key information.""",
            verbose=True,
            allow_delegation=False,
            memory=memory,
            llm=llm,
            max_iter=3
        )
    
    def _format_tools_for_crewai(self, tools: List) -> List:
        """Format tools properly for CrewAI (for future use)."""
        # This will be used later when we properly integrate tools
        formatted_tools = []
        for tool in tools:
            if hasattr(tool, '_run'):
                # Convert our custom tools to CrewAI format
                formatted_tools.append({
                    'name': getattr(tool, 'name', 'search_tool'),
                    'description': getattr(tool, 'description', 'Web search tool'),
                    'func': tool._run
                })
        return formatted_tools