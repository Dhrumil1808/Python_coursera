import json

input = '''
{
  "note":"bla h blaha bhlajh",
  "comments":
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]
}'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Name', item['note']
    print 'Id', item['id']
    print 'Attribute', item['x']

