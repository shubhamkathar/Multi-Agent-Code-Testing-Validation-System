import subprocess

def run_tests():
    result = subprocess.run(
        ["pytest", "-q"],
        capture_output=True,
        text=True
    )

    return {
        "output": result.stdout,
        "errors": result.stderr
    }
