import json
MAX_LINE=1024*1024

def encode_message(message): return (json.dumps(message,ensure_ascii=False)+"\n").encode("utf-8")
def decode_message(line):
    if len(line)>MAX_LINE: raise ValueError("Сообщение слишком большое")
    data=json.loads(line.decode("utf-8"))
    if not isinstance(data,dict) or "command" not in data or not isinstance(data.get("data",{}),dict):
        raise ValueError("Ожидается JSON-объект с command и data")
    return data
