import requests

domain = "https://www.google.com"

# extract header information

headers=requests.get(domain).headers

if 'X-Frame-Options' in headers:
	print("website is not vulnerable")
	
else:
	print("website is vulnerable to attack")
	
# Check x frame options in the header information
