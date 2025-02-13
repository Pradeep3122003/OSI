from network import NetworkInterfaceLayer
from internet import InternetLayer
from transport import TransportLayer
from application import ApplicationLayer

def client():
    network_interface = NetworkInterfaceLayer('127.0.0.1', 12345)
    network_interface.connect()
    app_layer = ApplicationLayer(TransportLayer())

    app_layer.send_message("Hello, Server!", network_interface, 
    network_interface.sock)
    
    network_interface.close()

if __name__ == "__main__":
    client()
