#!/bin/bash

VENV_DIR="venv"

if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists. Activating..."
    source "$VENV_DIR/bin/activate"
else
    echo "Virtual environment does not exist. Creating..."
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
fi

if [ -f "requirements.txt" ]; then
    echo "Installing packages from requirements.txt..."
    source "$VENV_DIR/bin/activate"
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Exiting..."
    deactivate
    exit 1
fi

echo "Setup complete."
deactivate