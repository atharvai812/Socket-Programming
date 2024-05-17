import asyncio
async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print ("Received {} from {}".format(message, addr))
        msg = input("enter message...")
        print ("sent : {}".format(msg))
        writer.write(msg.encode())
        await writer.drain()
    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print('Serving on {}'.format(addrs,))
    async with server:
        await server.serve_forever()
asyncio.run(main())
