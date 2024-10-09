import os
import hashlib
import qrcode
from PIL import Image

SECRET_KEY = "my_secret_key"
QR_CODE_BOX_SIZE = 10
QR_CODE_BORDER = 4

def create_digital_signature(exam_result):
    
    hash_object = hashlib.sha256()
    hash_object.update(exam_result.encode('utf-8') + SECRET_KEY.encode('utf-8'))
    digital_signature = hash_object.hexdigest()
    return digital_signature

def generate_qr_code(exam_result, digital_signature):

    qr = qrcode.QRcode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=QR_CODE_BOX_SIZE,
        border=QR_CODE_BORDER,
    )
    qr.add_data(f"Exam Result: {exam_result}\nDigital Signature: {digital_signature}")
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')

def verify_qr_code(qr_code_image):

    qr = qrcode.QRCode()
    qr.add_data(qr_code_image)
    qr.make(fit=True)
    data = qr.data.decode('utf-8')
    exam_result, exam_result = data.split('\n')
    exam_result = exam_result.split(': ')[1]
    if digital_signature == digital_signature_expected: # type: ignore
        return True
    else:
        return False
    
qr_code_image = Image.open(os.path.join(os.getcwd(), 'qr_code.png'))
if verify_qr_code(qr_code_image):
    print("Result is authentic.")
else:
    print("Result is not authentic.")
