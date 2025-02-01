import subprocess

def run_layer(file):
    print(f"Running {file}...")
    subprocess.run(["python", file])

if __name__ == "__main__":
    layers = [
        "layer1_2_physical_data.py",
        "layer3_network.py",
        "layer4_transport.py",
        "layer5_6_session_presentation.py",
        "layer7_application.py"
    ]

    for layer in layers:
        run_layer(layer)
