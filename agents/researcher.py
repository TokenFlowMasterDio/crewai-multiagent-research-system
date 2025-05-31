from crewai import Agent

def create_researcher_agent(llm):
    return Agent(
        role="Research Analyst",
        goal="Identify cutting-edge developments in AI",
        backstory="An AI agent specializing in deep research and summarization of technical findings.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )