import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

# DATA:
# Import the externalized pizza data
from .pizza_data import pizza_ingredients

# TOOL:
# Function to search ingredients by name
def search_ingredient_by_name(name: str):
    """
    Search for ingredients that start with the given name
    Args:
        name (str): The name or prefix of the ingredient
    Returns:
        dict: A dictionary of matching ingredients and their prices, or an empty dictionary if no matches are found
    """
    name = name.lower().strip()
    matches = {ingredient: price for ingredient, price in pizza_ingredients.items() if ingredient.startswith(name)}
    
    if not matches:
        print(f"No ingredients found starting with '{name}'")
        return {}
    
    return matches

# TOOL:
def say_hello(name: str):
    """
    A tool that says hello to someone.
    """
    return f"Hello, {name}! 👋"


root_agent = Agent(
    model=LiteLlm(model=f"openai/{os.environ.get('MODEL_RUNNER_CHAT_MODEL')}"),
    name="michelangelo_agent",
    description=(
        """
        Michelangelo is a helpful assistant who can answer questions about Pizza.
        """
    ),
    instruction="""
    You are Michelangelo, a helpful assistant who can answer questions about Pizza.
    You will be asked questions about Pizza, and you should provide accurate and helpful answers.
    If you don't know the answer, you should say "I don't know" or "I'm not sure
    """,
    tools=[
        say_hello,
        search_ingredient_by_name,
        MCPToolset(
            connection_params=StdioServerParameters(
                command='socat',
                args=[
                    "STDIO",
                    "TCP:host.docker.internal:8811",
                ],
            ),
            # Optional: Filter which tools from the MCP server are exposed
            tool_filter=['brave_web_search']
        )
    ],
)


