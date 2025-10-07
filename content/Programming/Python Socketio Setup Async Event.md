---
tags:
  - python
---
```python
@sio.event
async def connect(sid, environ):
    # Create background task when server starts accepting connections
    if not hasattr(sio, '_background_task_started'):
        sio.start_background_task(send_to_client)
        sio._background_task_started = True

```