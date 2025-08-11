#!/bin/bash
# Background AI Agents Status Check Script
# XFG STARK Project Monitoring

echo "📊 Background AI Agents Status Check"
echo "🔍 XFG STARK Project Integration"
echo "🏆 Elite Senior Developer Standards"
echo ""

# Check if agents are running
if pgrep -f "start_background_agents.py" > /dev/null; then
    echo "✅ Background agents are running"
    
    # Show recent logs
    echo ""
    echo "📋 Recent activity:"
    if [ -f "logs/background_agent_manager.log" ]; then
        tail -n 10 logs/background_agent_manager.log
    fi
    
    # Show agent status
    echo ""
    echo "🤖 Agent Status:"
    for log_file in logs/*.log; do
        if [ -f "$log_file" ]; then
            agent_name=$(basename "$log_file" .log)
            echo "  $agent_name: $(tail -n 1 "$log_file" | grep -o 'status.*' || echo 'active')"
        fi
    done
else
    echo "❌ Background agents are not running"
    echo "💡 To start agents, run: ./start_agents.sh"
fi

echo ""
echo "🔗 XFG STARK Project Integration:"
echo "  Project Root: /Users/aejt/fuegowalletproof/xfg-stark-agent-coordination"
echo "  Agents Directory: /Users/aejt/fuegowalletproof/xfg-stark-agent-coordination/agents"
echo "  Coordination Directory: /Users/aejt/fuegowalletproof/xfg-stark-agent-coordination/coordination"
