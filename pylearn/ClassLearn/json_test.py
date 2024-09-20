
import json

info = {
    'name': ['alex','game','张三'],
    'age':[22,23,24],
    'id':[1,2,3]
}
with open('test.json','w') as f:
    f.write(json.dumps(info))