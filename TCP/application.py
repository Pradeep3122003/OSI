class ApplicationLayer:
    def __init__(self, transport_layer):
        self.transport_layer = transport_layer

    def send_message(self, message, network_interface, connection):
        segment = self.transport_layer.create_segment(message)
        packet = internet().encapsulate(segment)
        network_interface.send(connection, packet)

    def receive_message(self, network_interface, connection):
        packet = network_interface.receive(connection)
        segment = internet().decapsulate(packet)
        _, data = self.transport_layer.extract_data(segment)
        return data
