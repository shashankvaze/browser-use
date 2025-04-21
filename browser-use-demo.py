from langchain_openai import AzureChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    try:
        agent = Agent(
            task="Compare the price of gpt-4o and DeepSeek-V3",
            llm=AzureChatOpenAI(model="gpt-4o",api_version="2023-05-15"),
        )
        await agent.run()
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(main())