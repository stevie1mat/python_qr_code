# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" width="35"> Python QR Code Scanner and Reader
 
Python QR Code Scanner and Reader using webcam. It can also be used to scan Barcodes.
 
 Star⭐ the repo if you like what you see😉.

# <img src="https://cdn.freebiesupply.com/logos/large/2x/visual-studio-code-logo-png-transparent.png" width="25"> Requirements
Any Operating System (ie. MacOS X, Linux, Windows)

VSCode or Pycharm. Any text editor will also do the job.

Latest Version of Python. Get it from <a href="https://www.python.org/downloads/">here.</a>
Latest Version of PIP

# Libraries Requirement

Install these using pip command.
(Eg. pip install qrcode)

<li>qrcode<br/>
<li>image<br/>
<li>opencv-python<br/>
<li>Pillow<br/>
<li>pyzbar<br/>
<li>image<br/>

# QR Code Create
<img src="https://github.com/stevie1mat/python_qr_code/blob/main/ss_reader.png">

Code Explanation:

```
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5,
)
```
version : This tells us how complicated qr code can be, larger the no, more complex will be the QR code generated.<br/>
box_size : Size of the QR Code box<br/>
border : Outer white space

```
data = 'https://www.youtube.com/channel/UCLYAvOLIC0vYV9mnIaqXLXQ'
```
Data takes in the value that the QR code will embed in itself.

```
img.save("qr.png")
```
The final image will be saved in png format. You can change according your requirement.

# QR Code Scanner
<img src="https://github.com/stevie1mat/python_qr_code/blob/main/ss_qrcode.png">

Code Explanation

```
barcode_info = barcode.data.decode('utf-8')
cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
```
Firt we have to draw a rectangle/square around the QR Code and decode the code.

```
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
```
Next we will put a text that is recognized, on top of the rectangle

```
with open("barcode_result.txt", mode ='w') as file:
file.write("Recognized Barcode:" + barcode_info)
```
Save the generated details into the text file.

```
camera = cv2.VideoCapture(0)
ret, frame = camera.read()
```
Use the device camera for scanning the QR Code

```
while ret:
ret, frame = camera.read()
frame = read_barcodes(frame)
cv2.imshow('Barcode/QR code reader', frame)
if cv2.waitKey(1) & 0xFF == 27:
break
```
To avoid issues, keep the loop running till ESC is pressed

```
camera.release()
cv2.destroyAllWindows()
```
Close the opened camera and windows.

That's it. Hopefully you will be able to run this project without any issues.

Author : <b>Steven Mathew</b>
<br/>
Programmer @ <a href="https://phinstudio.com">phinstudio.com</a>
