from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import (
    StdioServerParameters,
    stdio_client,
)

MODEL = "us.amazon.nova-pro-v1:0"

aws_docs_mcp = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="awslabs.aws-documentation-mcp-server"
        )
    )
)

with aws_docs_mcp:
    tools = aws_docs_mcp.list_tools_sync()

    agent = Agent(
        model=MODEL,
        tools=tools,
        system_prompt="""
You are an AWS Learning Assistant.
Explain AWS concepts simply.
"""
    )

    print("☁️ AWS Learning Assistant")
    print("Type quit to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        print("\nAssistant:\n")
        print(agent(user_input))
        print()
print("\n✅ Challenge 5 complete!")