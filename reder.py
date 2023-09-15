import json
with open("test.json","r",encoding="UTF-8") as f:
    d=json.load(f)
    
print(d)