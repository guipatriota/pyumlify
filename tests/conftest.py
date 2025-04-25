# tests/conftest.py
import subprocess
import sys
# from pytest import Session

def pytest_sessionstart(session):
    """
    Run once before all tests to ensure the package is installed.
    """
    print("🔧 Installing package in editable mode...")
    
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-e", ".", "--no-build-isolation"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)
        raise RuntimeError("❌ Editable install failed")

    print("✅ Editable install completed.")
