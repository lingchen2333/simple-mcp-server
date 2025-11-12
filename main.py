import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    print("Hello from simple-mcp-server!")


if __name__ == "__main__":
    asyncio.run(main())
