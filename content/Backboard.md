---
tags:
  - machine_learning
  - programming
---
A routing tool that exposes multiple AI models for use
# Boilerplate
```python
# pip install backboard-sdk
import asyncio
from backboard import BackboardClient

async def main():
    client = BackboardClient(api_key="YOUR_API_KEY")

    # Send a message — thread and assistant are auto-created
    response = await client.send_message(
        "Hello! I'm excited to get started.",
        memory="Auto",
    )
    print(response.content)

    # Continue the conversation using the returned thread_id
    response = await client.send_message(
        "What can you help me with?",
        thread_id=response.thread_id,
    )
    print(response.content)

asyncio.run(main())
```