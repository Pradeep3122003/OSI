from network import NetworkInterfaceLayer
from application import ApplicationLayer
from transport import TransportLayer
from internet import InternetLayer

def server():
    network_interface = NetworkInterfaceLayer('0.0.0.0', 12345)
    conn = network_interface.accept()
    app_layer = ApplicationLayer(TransportLayer())

    message = app_layer.receive_message(network_interface, conn)
    print(f"Received Message: {message}")

    network_interface.close()

if __name__ == "__main__":
    server()
