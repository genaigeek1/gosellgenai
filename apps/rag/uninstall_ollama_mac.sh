#!/bin/bash

echo "🔧 Uninstalling Ollama CLI and GUI..."

# Remove Homebrew CLI install
brew uninstall --formula ollama 2>/dev/null

# Remove GUI App
rm -rf /Applications/Ollama.app

# Remove user data (models, config)
rm -rf ~/.ollama

echo "✅ Ollama completely removed from this system."