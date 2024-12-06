MAX_MESSAGE_SIZE = 256
HEADER_SIZE = 64

# Application, presentation, session -> not always adds a header
# what they add is also not exactly a header. They add additional info like
#                   data transformation and session management, etc

# Headers are added in the Transport, Network, Datalink layers (always)
# Physical layer -> only transmits bits (doesn't add a header)

def application_layer(message):
    header = "APPLICATION_LAYER_HEADER:"
    padded_header = f"{header:<28}"
    layer = "Application Layer: "
    padded_layer = f"{layer:<20}"
    new_message = f"{padded_header}{message}"
    print(f"{padded_layer} {new_message}")
    presentation_layer(new_message)


def presentation_layer(message):
    header = "PRESENTATION_LAYER_HEADER:"
    padded_header = f"{header:<28}"
    layer = "Presentation Layer: "
    padded_layer = f"{layer:<20}"
    new_message = f"{padded_header}{message}"
    print(f"{padded_layer} {new_message}")
    session_layer(new_message)


def session_layer(message):
    header = "SESSION_LAYER_HEADER:"
    padded_header = f"{header:<28}"
    layer = "Session Layer: "
    padded_layer = f"{layer:<20}"
    new_message = f"{padded_header}{message}"
    print(f"{padded_layer} {new_message}")
    transport_layer(new_message)


def transport_layer(message):
    header = "TRANSPORT_LAYER_HEADER:"
    padded_header = f"{header:<28}"
    layer = "Transport Layer: "
    padded_layer = f"{layer:<20}"
    new_message = f"{padded_header}{message}"
    print(f"{padded_layer} {new_message}")
    network_layer(new_message)


def network_layer(message):
    header = "NETWORK_LAYER_HEADER:"
    padded_header = f"{header:<28}"
    layer = "Network Layer: "
    padded_layer = f"{layer:<20}"
    new_message = f"{padded_header}{message}"
    print(f"{padded_layer} {new_message}")
    data_link_layer(new_message)


def data_link_layer(message):
    header = "DATA_LINK_LAYER_HEADER:"
    padded_header = f"{header:<28}"
    layer = "Data Link Layer: "
    padded_layer = f"{layer:<20}"
    new_message = f"{padded_header}{message}"
    print(f"{padded_layer} {new_message}")
    physical_layer(new_message)


def physical_layer(message):
    header = "PHYSICAL_LAYER_HEADER:"
    padded_header = f"{header:<28}"
    layer = "Physical Layer: "
    padded_layer = f"{layer:<20}"
    new_message = f"{padded_header}{message}"
    print(f"{padded_layer} {new_message}")


if __name__ == "__main__":
    application_message = "The DATA"
    application_layer(application_message)
