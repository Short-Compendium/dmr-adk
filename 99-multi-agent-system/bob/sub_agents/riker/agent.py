import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

root_agent = Agent(
    model=LiteLlm(model=f"openai/{os.environ.get('MODEL_RUNNER_CHAT_MODEL')}"),
    name="riker_agent",
    description=(
        """
        Riker is a helpful assistant. 
        """
    ),
    instruction="""
    You are Riker, a helpful assistant who can answer questions.
    If you don't know the answer, you should say "I don't know" or "I'm not sure"

    Always start an answers with "🦁 Riker:"

    ### IMPORTANT:
    1. **No Parent Agent Routing:** Do not route back to the parent agent unless the user explicitly requests it.
    """,
)