import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "p5zs2s6hoayrlm3b@ethereal.email"
    login = "p5zs2s6hoayrlm3b@ethereal.email"
    password = "bchwV8vmEeCWdQPSNM"

    msg = MIMEMultipart()
    msg['From'] = "viagens_confirmar@email.com"
    msg['to'] = ', '.join(to_addrs)

    msg['Subject'] = "Confirmação de viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.ethereal.email', 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    server.quit()
