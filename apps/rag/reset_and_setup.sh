#!/bin/bash

echo "🧹 Cleaning up existing Docker containers..."
docker-compose down -v

echo "🔧 Removing old virtual environments..."
rm -rf rag-env
find . -type d -name '__pycache__' -exec rm -r {} +
find . -name "*.pyc" -delete

echo "🐳 Checking if Docker is running..."
if ! docker info > /dev/null 2>&1; then
    echo "⚠️ Docker is not running. Attempting to launch Docker Desktop..."
    open -a Docker
    echo "⏳ Waiting for Docker to start..."

    retries=0
    max_retries=10
    while ! docker info > /dev/null 2>&1; do
        sleep 3
        retries=$((retries+1))
        if [ $retries -eq $max_retries ]; then
            echo "❌ Docker did not start. Please launch Docker Desktop manually and retry."
            exit 1
        fi
    done
    echo "✅ Docker is now running."
else
    echo "✅ Docker is already running."
fi

echo "🧠 Checking for local Ollama CLI..."
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama CLI is not installed on your Mac."
    echo "👉 Install it with: brew install --cask ollama"
else
    echo "✅ Ollama CLI is installed."

    echo "🔍 Checking if 'mistral' model is pulled locally..."
    if ! ollama list | grep -q 'mistral'; then
        echo "⚠️ 'mistral' model is not pulled locally."
        echo "👉 Run this before continuing: ollama pull mistral"
        exit 1
    else
        echo "✅ 'mistral' model is available locally."
    fi

    echo "🧼 Checking for duplicate Ollama installations (GUI + CLI)..."
    if [ -d "/Applications/Ollama.app" ]; then
        echo "⚠️ Ollama GUI is installed. If CLI conflicts occur, consider removing it:"
        echo "👉 Run: sudo rm -rf /Applications/Ollama.app"
    fi
fi

echo "🐳 Starting Docker containers for Ollama and Streamlit..."
docker-compose up -d --build

echo "⏳ Waiting for containers to become ready..."
sleep 5

echo "🔍 Checking if Ollama container is responding..."
if curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "✅ Ollama container is up and reachable at http://localhost:11434"
else
    echo "❌ Failed to connect to Ollama on port 11434. Check Docker logs or retry."
    docker ps
    exit 1
fi

echo "✅ ✅ ✅ All components are up and running!"
echo "-------------------------------------------------"
echo "Next Steps:"
echo "👉 Open your browser: http://localhost:8501"
echo "👉 Log in: admin / adminpass"
echo "👉 Upload a document: data/sample.txt"
echo "👉 Ask a question about the document"
echo "-------------------------------------------------"