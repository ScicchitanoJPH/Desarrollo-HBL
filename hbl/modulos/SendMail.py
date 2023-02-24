from email.message import EmailMessage
import smtplib
remitente = "espjph@gmail.com"
destinatario = "dss@jphlions.com"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Intruso detectado"




def send(date):
    try:
        mensaje = "<html><body><h1> Se ha detectado un intruso a las : " + date + "</h1></body></html>"
        email.set_content(mensaje)
        smtp = smtplib.SMTP_SSL("smtp-relay.sendinblue.com")
        smtp.login(remitente, "cE3TXIL9BO0Fy7nb")
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()
        
    except Exception as e:
        print("No se pudo enviar el mail : %s\n" % e)