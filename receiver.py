import asyncio

async def handle_data(
    reader: asyncio.StreamReader, 
    writer: asyncio.StreamWriter
) -> None:
    print('handle_data: status="in_progress"')
    data: bytes = await reader.read()
    print(data)
    print('handle_data: status="done"')
    

async def main():
    print("receiver: starting")
    server = await asyncio.start_server(handle_data, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())