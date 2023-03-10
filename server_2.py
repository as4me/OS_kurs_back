import asyncio

import websockets as websockets
import psutil
import json
all_clients = set()

count_clients = 0
all_users = {}

async def send_massage(message: str,id: int):
   
    total_memory = psutil.virtual_memory().total

   
    free_memory = psutil.virtual_memory().free


    used_memory = total_memory - free_memory

    memory_usage_percentage = (used_memory / total_memory) * 100
    
    client = all_users[id]
    if(message =='pm'):
        await client.send(json.dumps({"user_id":str(2),"pm":str(total_memory)}))
    elif(message == 'free'):
        await client.send(json.dumps({"user_id":str(2),"free":str(free_memory)}))
    else:
        pass
    

num_physical_cores = psutil.cpu_count(logical=False)
print(num_physical_cores)
        
async def new_client_connected(client_socket: websockets.WebSocketClientProtocol, path: str):
    print("New cliet connected")
    all_clients.add(client_socket)
    all_users[len(all_clients)] = client_socket
    count_clients = len(all_clients)
    try:
        while True:
            new_message = await client_socket.recv()
            print("New message from a client: ", new_message)
            await send_massage(message=new_message,id=count_clients)
    # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        all_clients.remove(client_socket)
        
async def start_server():
    await websockets.serve(new_client_connected,"0.0.0.0",7891)
    
    
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()