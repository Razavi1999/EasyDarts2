
a = [(1,0) ,(2 , 0.2) ,(3,0.1) ,(4,0.5) ,(5,0.5),(6,0.6),(7,0.7) ,(8,0.8) ,(9,0.9),(10,1)]

b = [(1,1) , (2,0.5) ,(3,0.4) ,(4,0.8) ,(7,0.3) ,(11,0.5)]

result = {}


for a_i in a:
  for b_i in b:
    tmp=a_i[0] * b_i[0]
    ozviat=min(a_i[1],b_i[1])
    if tmp not in result.keys():
      result[tmp]=ozviat
    else:
      if result[tmp]<ozviat:
        result[tmp]=ozviat

dictionary_items = result.items()
for item in dictionary_items:
    print(item)