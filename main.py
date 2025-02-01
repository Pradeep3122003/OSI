import subprocess

def run_layer(file):
    print(f"Running {file}...")
    subprocess.run(["python3", file])

if __name__ == "__main__":
    layers = [
        "physical.py",
        "network.py",
        "transport.py",
        "present.py",
        "application.py"
    ]

    for layer in layers:
        run_layer(layer)
