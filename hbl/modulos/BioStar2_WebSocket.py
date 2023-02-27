import websocket
import time
import rel
import requests
import ssl
import json
from modulos import hbl as hbl
from modulos import log as log


"""
    *Para usar la libreria de websocket, hay que instalar:
        pip install websocket-client
    Si se comete el error de instalar el paquete de websocket, hacer lo siguiente:
        pip uninstall websocket
        pip uninstall websocket-client
        pip install websocket-client

    *Hay dos tipos de eventos:
        # IDENTIFY_SUCCESS_FINGERPRINT
        # VERIFY_SUCCESS_CARD
"""


def Get_bs_session_id():
    url = hbl.BioStar2_WebSocket_Api_Host + '/api/login'
    payload = "{\r\n    \"User\": {\r\n        \"login_id\": \"" + hbl.BioStar2_WebSocket_BioStar2_User + "\",\r\n        \"password\": \"" + hbl.BioStar2_WebSocket_BioStar2_Password + "\"\r\n    }\r\n}"
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    bs_session_id = response.headers['bs-session-id']
    print(bs_session_id)
    return bs_session_id






def Inicializar_Eventos(bs_session_id):
    url = hbl.BioStar2_WebSocket_Api_Host + '/api/events/start'
    payload = "{\r\n    \"User\": {\r\n        \"login_id\": \"" + hbl.BioStar2_WebSocket_BioStar2_User + "\",\r\n        \"password\": \"" + hbl.BioStar2_WebSocket_BioStar2_Password + "\"\r\n    }\r\n}"
    headers = {"bs-session-id" : bs_session_id}
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    print(response.text)
    time.sleep(4)






def on_message(ws, message):
    message_json = json.loads(message)

    print(message_json)
    print("\n")
    print("**************************************************************************")
    
    event_type_name = message_json["Event"]["event_type_id"]["name"]
    device_id = message_json["Event"]["device_id"]["id"]
    #print("Tipo de evento : " + event_type_name)
    #print("Device ID : " + device_id)
    if event_type_name == hbl.BioStar2_WebSocket_Tipo_Evento and device_id == hbl.BioStar2_WebSocket_Device_ID:
        log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
        log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"Tipo de evento : " + event_type_name)
        log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"Device ID : " + device_id)
        id = message_json["Event"]["user_id"]["user_id"]
        #print("ID : " + id)
        log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"ID : " + id)
    #print("**************************************************************************")
    #print("\n")





def on_error(ws, error):
    print(error)





def on_close(ws, close_status_code, close_msg):
    print("### closed ###")





def on_data(arg1,arg2,arg3):
    print("### New Data ###")





def on_open(ws):
    bs_session_id = Get_bs_session_id()
    ws.send('bs-session-id' + "=" + bs_session_id)
    Inicializar_Eventos(bs_session_id)
    print("Opened connection")







def inicializacion():
    if hbl.BioStar2_WebSocket_activado:
        #websocket.enableTrace(True)
        ws = websocket.WebSocketApp(hbl.BioStar2_WebSocket_WebSocket_Host + '/wsapi',
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
        
        

        ws.run_forever(dispatcher=rel, reconnect=5,sslopt={"cert_reqs": ssl.CERT_NONE})  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()