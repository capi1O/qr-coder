import gzip
import base64
import qrcode
from io import BytesIO

file_path = 'input.txt'

def compress_file_and_encode_to_base64(file_path):
    # Read the contents of the file
    with open(file_path, 'rt', encoding='utf-8') as file:
        input_str = file.read()
    
    # Compress the input string using gzip
    out = BytesIO()
    with gzip.GzipFile(fileobj=out, mode='w') as f:
        f.write(input_str.encode('utf-8'))
    compressed_data = out.getvalue()
    
    # Encode the compressed data to Base64
    base64_encoded_data = base64.b64encode(compressed_data).decode('utf-8')
    return base64_encoded_data

def generate_qr_code(data):
    # Generate a QR code from the given data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Display the QR code
    img.show()
    # Optionally, save the QR code to a file
    # img.save("output_qr.png")

base64_encoded_data = compress_file_and_encode_to_base64(file_path)
generate_qr_code(base64_encoded_data)
