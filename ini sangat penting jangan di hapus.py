from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot' , methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'hi' in incoming_msg:
        p = """
        Hallo, Selamat Datang Di Hallo Indihome. Kenalin Nama Aku Sobi!, Salam Kenal Ya. Ada yang Bisa Sobi Bantu Gak nih?.
        *lokasi* = Lokasi Plasa Bumiayu
        *promo* = Info Menarik Promo Dari Indihome
        """
        msg.body(p) 
    if 'promo' in incoming_msg:
        msg.media('https://subsystem.indihome.co.id/cms-ih/assets/uploads/promorec/Paket-Jitu-1_Page-Detail-2220x740.jpg')

    elif 'lokasi' in incoming_msg:
        msg.body('Lokasi Kami Bisa Anda Lihat Di sini, https://goo.gl/maps/YAxJnsrNjHVFkNd86')
    return str(resp)


if __name__ == '__main__':
        app.run(port=4000)