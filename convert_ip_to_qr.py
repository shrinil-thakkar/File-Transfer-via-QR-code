"""
  These commands convert your public ip address to QR code and outputs it on the screen.
"""

import pyqrcode

# url = <enter the public you created>
url = pyqrcode.create(public_url)
print(url.terminal(quiet_zone=1)) 
