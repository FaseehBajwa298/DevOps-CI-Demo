import sys
import subprocess
from pathlib import Path

# Ensure repository root is on sys.path for importing app.py
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app


def test_build_message_custom():
    assert app.build_message("CI") == "Hello from DevOps-CI-Demo, CI!"


def test_cli_default_output():
    result = subprocess.run([sys.executable, "app.py"], capture_output=True, text=True)
    assert "Hello from DevOps-CI-Demo, friend!" in result.stdout