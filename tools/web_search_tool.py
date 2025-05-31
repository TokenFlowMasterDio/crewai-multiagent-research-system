from pydantic import Field
from crewai.tools import BaseTool  # ✅ Corrected import

class WebSearchTool(BaseTool):
    name: str = Field(default="web_search", description="Tool that searches the web.")
    description: str = Field(
        default="Useful for when you need to find information on the web."
    )

    def _run(self, query: str) -> str:
        # Simulated logic
        return f"Simulated web search result for query: {query}"
