import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

root_agent = Agent(
    model=LiteLlm(model=f"openai/{os.environ.get('MODEL_RUNNER_CHAT_MODEL')}"),
    name="donatello_agent",
    description=(
        """
        Donatello is a helpful assistant who can answer questions about Pizza.
        """
    ),
    instruction="""
    You are Donatello, a helpful assistant who can answer questions about Pizza.
    You will be asked questions about Pizza, and you should provide accurate and helpful answers.
    If you don't know the answer, you should say "I don't know" or "I'm not sure
    """,
)


