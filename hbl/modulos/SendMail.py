from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "RPI 4"

sender = {"name":"John Doe","email":"espjph@gmail.com"}

to = [{"email":"dss@jphlions.com","name":"Jane Doe"}]
cc = [{"email":"example2@example2.com","name":"Janice Doe"}]
bcc = [{"name":"John Doe","email":"example@example.com"}]
reply_to = {"email":"replyto@domain.com","name":"John Doe"}
headers = {"Some-Custom-Name":"unique-id-1234"}
params = {"parameter":"My param value","subject":"New Subject"}



def send(date):
    try:
        html_content = "<html><body><h1>" + date + "</h1></body></html>"
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)