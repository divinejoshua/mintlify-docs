api_key = "wtc-sk-ad74a24c0976d994b382a85c48b31f6d79288983"

import asyncio
from wetro import AsyncWetrocloud

async def main():
    client = AsyncWetrocloud(api_key=api_key)
    response = await client.rag.collection.query(collection_id="my_unique_collection_id", request_query="What is this article about?")
    return response

result = asyncio.run(main())