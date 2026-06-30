import json
import os

from strands import Agent

MODEL = "us.amazon.nova-pro-v1:0"
MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"name": "", "food": ""}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


memory = load_memory()

agent = Agent(
    model=MODEL,
    system_prompt="You are a helpful assistant."
)

print("🧠 Memory Agent Ready!")
print("Type quit to exit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        break

    if "my name is" in user_input.lower():
        memory["name"] = user_input.split("is")[-1].strip()
        save_memory(memory)
        print("Name remembered.")
        continue

    if "i love" in user_input.lower():
        memory["food"] = user_input.split("love")[-1].strip()
        save_memory(memory)
        print("Preference remembered.")
        continue

    if "what do you know about me" in user_input.lower():
        print(memory)
        continue

    print(agent(user_input))

print("\n✅ Challenge 3 complete!")