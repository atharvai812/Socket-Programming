import asyncio

async def main():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    while True:
        message=input('enter message..')
        print ('send : {}'.format(message))
        writer.write(message.encode())

        data = await reader.read(100)
        print('Received:{}'.format(data.decode()))

    print('Close the connection')
    writer.close()

asyncio.run(main())
