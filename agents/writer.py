from crewai import Agent

def create_writer_agent(llm):
    return Agent(
        role="Content Writer",
        goal="Communicate technical ideas clearly to the general public",
        backstory="An AI agent trained to write compelling articles and explain technical concepts to non-experts.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )