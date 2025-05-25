#!/bin/bash

set -e

# --- Original docker setup ---
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

# --- Ollama check ---
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

# --- Start docker containers ---
echo "🐳 Starting Docker containers for Ollama and Streamlit..."
docker-compose up -d --build

sleep 5

# --- Check Ollama ---
echo "🔍 Checking if Ollama container is responding..."
if curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "✅ Ollama container is up and reachable at http://localhost:11434"
else
    echo "❌ Failed to connect to Ollama on port 11434. Check Docker logs or retry."
    docker ps
    exit 1
fi

# --- Healthcheck for local iframe services ---
echo "🛠 Checking ttyd, Flask editor, and Streamlit..."
function check_port {
  local port=$1
  local label=$2
  if lsof -i :$port &>/dev/null; then
    echo "$label already running on $port"
  else
    echo "$label not running — launching..."
    case $port in
      7681)
        ttyd bash &
        ;;
      5050)
        export FLASK_APP=editor.py
        flask run --port=5050 &
        ;;
      8501)
        (cd apps/rag && streamlit run app.py &)
        ;;
    esac
  fi
}

check_port 7681 "Local terminal (ttyd)"
check_port 5050 "sample.txt editor (Flask)"
check_port 8501 "Streamlit UI"

# --- Start local web server for HTML testing ---
echo "🧪 Starting local web server at http://localhost:8080"
python3 -m http.server 8080 &

# --- Auto-open demo page in default browser ---
sleep 2
URL="http://localhost:8080/docs/html/ragdemo.html"
echo "🌐 Opening RAG demo in browser: $URL"
open "$URL"

wait