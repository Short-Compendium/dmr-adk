import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset,StdioServerParameters, SseServerParams, StreamableHTTPServerParams


#print(f"🤖 MESSAGE: {MESSAGE}")

root_agent = Agent(
    model=LiteLlm(model=f"openai/{os.environ.get('MODEL_RUNNER_CHAT_MODEL')}"),
    name="bob_agent",
    description=(
        """
        Bob is a helpful assistant who can answer questions about Hawaiian Pizza.
        """
    ),
    instruction="""
    You are Bob, a helpful assistant who can answer questions about Hawaiian Pizza.
    You will be asked questions about Pizza, and you should provide accurate and helpful answers.
    If you don't know the answer, you should say "I don't know" or "I'm not sure
    """,
     tools=[
         MCPToolset(
             connection_params=SseServerParams(
                 url="http://0.0.0.0:8080/mcp",
             ),
            tool_filter=[
                'say_hello', 
            ]
         ),
         MCPToolset(
             connection_params=StreamableHTTPServerParams(
                 url="http://0.0.0.0:9090/mcp",
             ),
            tool_filter=[
                'say_hey', 
            ]
         ),         
     ]
)


