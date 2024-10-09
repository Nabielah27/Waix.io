from flask import Flask, request, jsonify
from qr_code_generator import verify_qr_code # type: ignore

app = Flask(__name__)

@app.route('/verify', methods=['POST'])
def verify_qr_code_api():
    qr_code_data = request.get_json()['qrCodeData']
    if verify_qr_code(qr_code_data):
        return jsonify({'message':'Result is authentic'})
    else:
        return jsonify({'message':'Result is not authentic'})
if __name__ == '__main__':
  app.run(debug=True)



