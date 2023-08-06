```python
from lotusdb import Database
db = Database('mydb.file')
db.put({ 'a': 'b' })
print(db.find(lambda x: x['a'] == 'b'))
db.remove(lambda x: x['a'] == 'b')
```