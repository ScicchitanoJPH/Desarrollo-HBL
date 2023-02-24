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
"""

WS_HOST = 'wss://172.16.23.25:443'
BIOSTAR2_WS_URL = WS_HOST + '/wsapi'
API_HOST = 'https://172.16.23.25'
BIOSTAR2_LOGIN_API_URL = API_HOST + '/api/login'
BIOSTAR2_WS_EVENT_START_URL = API_HOST + '/api/events/start'

EVENT_TYPE_WANTED  = "IDENTIFY_SUCCESS_FINGERPRINT"
DEVICE_ID_WANTED  = "538849673"


def Get_bs_session_id():
    url = BIOSTAR2_LOGIN_API_URL
    payload = "{\r\n    \"User\": {\r\n        \"login_id\": \"admin\",\r\n        \"password\": \"Jphlions135\"\r\n    }\r\n}"
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    bs_session_id = response.headers['bs-session-id']
    print(bs_session_id)
    return bs_session_id






def Inicializar_Eventos(bs_session_id):
    url = BIOSTAR2_WS_EVENT_START_URL
    payload = "{\r\n    \"User\": {\r\n        \"login_id\": \"admin\",\r\n        \"password\": \"Jphlions135\"\r\n    }\r\n}"
    headers = {"bs-session-id" : bs_session_id}
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    print(response.text)
    time.sleep(4)






def on_message(ws, message):
    message_json = json.loads(message)

    #print("\n")
    #print("**************************************************************************")
    
    event_type_name = message_json["Event"]["event_type_id"]["name"]
    device_id = message_json["Event"]["device_id"]["id"]
    #print("Tipo de evento : " + event_type_name)
    #print("Device ID : " + device_id)
    if event_type_name == EVENT_TYPE_WANTED and device_id == DEVICE_ID_WANTED:
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
        ws = websocket.WebSocketApp(BIOSTAR2_WS_URL,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
        
        

        ws.run_forever(dispatcher=rel, reconnect=5,sslopt={"cert_reqs": ssl.CERT_NONE})  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()