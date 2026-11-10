---
tags:
  - programming
  - machine_learning
---
```python
from dotenv import load_dotenv
import os
import asyncio
from backboard import BackboardClient
from pydantic import BaseModel, Field

load_dotenv()
secret_key = os.getenv('BACKBOARD_APIKEY')

questions = {
    # noul: yes/no proposition -> probability from 0 to 1
    "refund_requested": {
        "type": "noul",
        "instructions": "Does the customer request a refund?",
    },
    # choice: pick one named option
    "department": {
        "type": "choice",
        "instructions": "Which team should handle this request?",
        "criteria": {
            "billing": "Payments, charges, and refunds",
            "technical": "Software errors and troubleshooting",
            "general": "Other enquiries",
        },
    },
    # score: ordered rubric, low to high (at least 2 levels)
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this request?",
        "criteria": ["Low", "Medium", "High"],
    },
}
async def main():
    client = BackboardClient(api_key=secret_key)
    
    # Send a message — thread and assistant are auto-created
    response = await client.send_message(
        "I was charged twice. Please refund me urgently.",
        memory="Auto",
        llm_provider="typesafe",
        model_name="jev-latest",
        stream=False,
        system_one= { "questions" : questions }
    )
    print(response.content)

asyncio.run(main())
```