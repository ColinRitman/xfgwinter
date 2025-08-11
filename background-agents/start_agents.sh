#!/bin/bash
# Background AI Agents Startup Script for XFG STARK Project
# Elite Senior Developer Configuration

echo "🚀 Starting Background AI Agents for XFG STARK Project"
echo "🏆 Elite Senior Developer Mode: ENABLED"
echo "🔐 Cryptographic Grade Validation: ENABLED"
echo "🦀 Rust Excellence Standards: ENABLED"
echo "⚡ STARK Proof Expertise: ENABLED"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Validate elite standards
echo "🏆 Validating elite senior developer standards..."
python start_background_agents.py --validate-only

if [ $? -eq 0 ]; then
    echo "✅ Elite standards validation passed!"
    echo "🚀 Starting background agents..."
    python start_background_agents.py
else
    echo "❌ Elite standards validation failed!"
    echo "Please check configuration and try again."
    exit 1
fi
