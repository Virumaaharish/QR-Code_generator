import qrcode

# Enter the URL of any website here
input_URL = "https://www.google.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,  # Set the box size to 20pt
    border=0,  # Remove the border by setting it to 0
)

qr.add_data(input_URL)
qr.make(fit=True)

# Convert into an image with red fill color and white background
img = qr.make_image(fill_color="red", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)  # Print the data list used for generating the QR code
