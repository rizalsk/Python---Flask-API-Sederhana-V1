from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi object flask
app = Flask(__name__)

# inisiasi object flask_restful
api = Api(app)

# inisiasi object flask cors
CORS(app)

# init variable kosong tipe dictionary
identitas = {} #Variable Global

# membuat class resource
class ContohResource(Resource):
    # method get dan post
    def get(self):
        response = {'response':'Hello dunia!, ini app restful pertamaku'}
        return identitas
    
    def post(self):
        nama = request.form['nama']
        umur = request.form['umur']
        identitas['nama'] = nama
        identitas['umur'] = umur
        response = {'msg' : 'data berhasil disimpan'}
        return response

# Setup Resource
api.add_resource(ContohResource, '/api', methods=['GET', 'POST'])

# 
if __name__ == '__main__':
    app.run(debug=True, port=5005)