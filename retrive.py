import json
#print( json.load(open("Indian_Number_plates.json","r")) )

#with open ('Indian_Number_plates.json') as plate:
#    data=json.load(plate)
import urllib.request as ur    
tweets = []
cnt=0
for line in open('Indian_Number_plates.json', 'r'):
    data=json.loads(line)
    #print(data['content'])
    ur.urlretrieve(data['content'],"C:\\Users\\maste\\Desktop\\dataset\\img"+str(cnt)+".jpg")
    cnt+=1
    

