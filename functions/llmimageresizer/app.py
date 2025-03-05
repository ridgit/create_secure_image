from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/resize', methods=['POST'])
def resize():
    img = Image.open(request.files['image'])
    size = request.form.get('size', '100x100').split('x')
    img = img.resize((int(size[0]), int(size[1])), Image.ANTIALIAS)
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
