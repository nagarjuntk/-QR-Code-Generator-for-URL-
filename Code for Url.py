import qrcode

# Correct the URL format by adding "https://"
data = "https://www.linkedin.com/in/nagarjun-tk-7044322b5"

# Generate QR code for the data
qr = qrcode.make(data)

# Correct the file path by using raw string or escaping backslashes
qr.save("C:/Users/Admin/Desktop/qrcode.png")
