import os
from datetime import date

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from .prompts import instructions_root
from .sub_agents import bill_agent, riker_agent


# INITIALIZE:
os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

date_today = date.today()


root_agent = Agent(
    model=LiteLlm(model=f"openai/{os.environ.get('MODEL_RUNNER_CHAT_MODEL')}"),
    name="bob_agent",
    description=(
        """
        Bob is a helpful assistant. 
        """
    ),
    global_instruction=( # instruction that applies to all agents in the Bobiverse
        f"""
        You are a Bobiverse Multi Agent System.
        Todays date: {date_today}
        """
    ),
    instruction= instructions_root(),
    sub_agents=[bill_agent, riker_agent],
    tools=[],

)