import os
from datetime import datetime

from strands import Agent, tool
from strands_tools import calculator

os.environ["BYPASS_TOOL_CONSENT"] = "true"

MODEL = "us.amazon.nova-pro-v1:0"


@tool
def weather(city: str) -> str:
    """Get weather for a city."""
    return f"The weather in {city} is sunny, 32°C."


@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from YYYY-MM-DD."""
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()

    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1

    return f"Age: {age} years"


agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator],
    system_prompt="You are a helpful assistant."
)

print("🧮 Math Test")
print(agent("What is 42 * 17?"))

print("\n🌤️ Weather Test")
print(agent("What's the weather in Chennai?"))

print("\n🎂 Age Test")
print(agent("How old is someone born on 2000-05-15?"))

print("\n✅ Challenge 2 complete!")