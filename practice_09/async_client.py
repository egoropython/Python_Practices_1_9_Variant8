"""Дополнительный asyncio-клиент для JSON-over-TCP."""
import asyncio, json
HOST="127.0.0.1"; PORT=50508
async def request(command,data=None):
    reader,writer=await asyncio.open_connection(HOST,PORT)
    message=json.dumps({"command":command,"data":data or {}},ensure_ascii=False)+"\n"
    writer.write(message.encode("utf-8")); await writer.drain()
    line=await reader.readline(); writer.close(); await writer.wait_closed()
    return json.loads(line.decode("utf-8"))
async def main():
    print(json.dumps(await request("list"),ensure_ascii=False,indent=2))
if __name__=="__main__": asyncio.run(main())
