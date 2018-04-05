# File-Transfer-via-QR-code

# Use-case : Transfer a file from your local computer to your phone

1. Select a file on your local computer.

2. Create a simple http server from your local computer.
    Run on command line : python -m SimpleHTTPServer <port>  //port eg.8000
    
    This will create a localhost on port 8000 (http://localhost:8000)
    
3. Convert localhost to local ip :
    Run on command line : <ifconfig>
    Copy the ip address for eth0
    
4. Attach the full path to the ip you got from ifconfig i.e. http://<ip>:<port>/path/to/the/file

5. Convert IP to QR code
    Install pyqrcode library,
    Run on command line : sudo pip install pyqrcode
    Edit the file convert_ip_to_qr.py with the ip you generated and run it.
   
   It will output a QR code.
   
6. Scan that QR code in your phone and the file will be downloaded automatically.
