import wikipedia as wp

topic=input("Enter the topic: ")

result=wp.summary(topic,sentences=2)# sentences=2 means it will print only 2 sentences
print(result)