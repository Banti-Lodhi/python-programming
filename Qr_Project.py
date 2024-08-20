import qrcode as qr

img = qr.make("https://www.google.com/search?q=world+cup&rlz=1C1YTUH_enIN1001IN1001&oq=world&gs_lcrp=EgZjaHJvbWUqDQgAEAAY4wIYsQMYgAQyDQgAEAAY4wIYsQMYgAQyCggBEC4YsQMYgAQyBggCEEUYOTIKCAMQLhixAxiABDIHCAQQABiABDIKCAUQABixAxiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTE1NjQ3ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#ip=1")

img.save("ws_cubetech.png")
print(img)