import pyshortner

url=input("Enter the url for shtortnening: ")

print("The shortened url is: ",pyshortner.Shortener().tinyurl.short(url))
