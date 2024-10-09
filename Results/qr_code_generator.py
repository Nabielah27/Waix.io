import qrcode
import hashlib

def generate_exam_result_id(exam_result):
    exam_result_id = hashlib.sha256(exam_result.encode()).hexdigest()
    return exam_result_id

exam_result = "John Doe, 90%, Math"

exam_result_id = generate_exam_result_id(exam_result)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(exam_result_id)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("exam_result_qr_code.png")