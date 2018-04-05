import pyqrcode

# url = <enter url>

url = pyqrcode.create(public_url)
print(url.terminal(quiet_zone=1)) 
