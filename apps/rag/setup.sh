#!/bin/bash

echo "🔧 Creating virtual environment with Python 3.11..."
/opt/homebrew/Cellar/python@3.11/3.11.12_1/bin/python3.11 -m venv rag-env

echo "✅ Activating virtual environment..."
source rag-env/bin/activate

echo "🧪 Ensuring pip..."
python -m ensurepip --upgrade

echo "⬆️ Upgrading pip..."
python -m pip install --upgrade pip

echo "📦 Installing dependencies..."
pip install --force-reinstall --no-cache-dir -r requirements.txt

echo "✅ Setup complete. To activate: source rag-env/bin/activate"