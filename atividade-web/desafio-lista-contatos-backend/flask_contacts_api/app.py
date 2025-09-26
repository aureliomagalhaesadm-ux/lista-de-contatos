from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, methods=["GET", "POST", "DELETE", "OPTIONS"])

contacts = [
    { "name": "John Doe", "email": "johne@email.com", "photo": "http://randomuser.me/api/portraits/men/1.jpg"},
    { "name": "Jane Doe", "email": "janedoe@email.com", "photo": "http://randmuser.me/api/portraits/women/1.jpg"}
] # lista para armazenar os contatos temporariamente
# Método para retornar todos os contatos
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify({'contacts': contacts}), 200

@app.route('/contacts/<email>', methods=['GET'])
def get_contact(email):
   contact = next((contact for contact in contacts if contact['email'] == email), None)
    if not contact:
        return jsonify({'error': 'Contact not found'}), 404
return jsonify({'contact': contact}), 200


if __name__ == '__main__':
   app.run(debug='true')
