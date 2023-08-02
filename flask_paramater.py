from flask import Flask,make_response, request, jsonify
from flask_cors import cross_origin, CORS
import cgi
import io
from PIL import Image
import numpy as np

app = Flask(__name__)
# @cross_origin()
CORS(app, resources=r'/*')


@app.route('/tabcco_ocr/', methods=['POST',"OPTIONS","HEAD","GET"])
@cross_origin()
def test(**kwgs):
    age = request.args.get('type')
    print("age------",age)

    data = request.get_data()
    content_type = request.content_type
    print('content_type', content_type)

    if content_type:
        boundary = content_type.split("=")[1].encode()  # 获取boundary字符串，并转换为bytes类型
        #       print(boundary)
        fields = cgi.parse_multipart(io.BytesIO(data), {'boundary': boundary})

        # *********************************
        img_io = io.BytesIO(fields['file'][0])
        #         print(type(img_io))
        #         tttt = img_io.read()
        #         print( tttt)
        img_PIL = Image.open(img_io).convert('RGB')
        #         img_PIL_to_detect = img_PIL.copy()
        #         img_PIL = Image.open(io.BytesIO(fields['file'][0]))

        #         print(img_PIL.size)
        # #         img_PIL.save('./chuanguolaidetupian_img_PIL.jpg')
        img_np = np.asarray(img_PIL)
        print(img_np.shape)



    respose = {
        "code": 'ok了',
        "image shape":img_np.shape
    }
    return jsonify(respose)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2228)