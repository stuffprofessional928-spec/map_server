import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent,Runner, set_tracing_disabled, function_tool, OpenAIChatCompletionsModel
from agents.mcp import MCPServerStdio



load_dotenv(override=True)
set_tracing_disabled(True)


openrouter_key = os.getenv("OPENROUTER_API_KEY")
openrouter_url = os.getenv("OPENROUTER_URL")

client = AsyncOpenAI(base_url=openrouter_url, api_key=openrouter_key)
MODEL = "gpt-5.4-mini"
model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)