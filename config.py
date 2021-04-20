import os

# Change to suit your server/port, then create .env for the others

class Config:
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWD')
    MAIL_TO_USER = os.environ.get('EMAIL_TO_USER')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
