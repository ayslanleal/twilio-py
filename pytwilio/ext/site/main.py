from flask import Flask, request, Blueprint
from twilio.twiml.messaging_response import MessagingResponse

bp = Blueprint('site', __name__)


@bp.route('/sms', methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message("retorno: {}".format(msg))

    return str(resp)
