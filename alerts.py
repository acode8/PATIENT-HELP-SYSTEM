import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
from config import EMAIL_SENDER, EMAIL_PASS, EMAIL_RECEIVER, TWILIO_SID, TWILIO_AUTH, TWILIO_FROM, TWILIO_TO

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(EMAIL_SENDER, EMAIL_PASS)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"[Email Error] {e}")

def send_sms(body):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        client.messages.create(body=body, from_=TWILIO_FROM, to=TWILIO_TO)
    except Exception as e:
        print(f"[SMS Error] {e}")
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import os

def make_call(message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        
        # Use TwiML to speak the message
        twiml = VoiceResponse()
        twiml.say(message, voice='alice')

        # Save TwiML to a URL-accessible location or use Twilio's TwiMLBin (or paste as string below)
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=TWILIO_TO,
            from_=TWILIO_FROM
        )
        print(f"[Voice Call] Sent: {call.sid}")
    except Exception as e:
        print(f"[Voice Call Error] {e}")
