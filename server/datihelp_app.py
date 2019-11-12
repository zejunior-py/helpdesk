from flask import Flask, jsonify, request
from server.service.helpdesk import DatiHelpDesk

SAP_REQUESTS_AUTHENTICATION = '12345678900'
app = Flask(__name__)


def check_auth(auth):
    if auth['Authorization'] == SAP_REQUESTS_AUTHENTICATION:
        return True
    return False


@app.route("/dati_help", methods=['GET', 'POST'])
def sap_decathlon():
    if check_auth(request.headers):
        return jsonify(DatiHelpDesk(request).run(), 200)
    return jsonify(username='Usuario nao Autorizado'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
