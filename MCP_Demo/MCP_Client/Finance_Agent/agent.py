import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

FINANCIAL_SERVER_SCRIPT_PATH = os.path.abspath("/Users/bgarware/adk_workshop/MCP_Demo/MCP_Server/mcp-server/server.py")
print(f"Financial Advisory Agent connecting to: {FINANCIAL_SERVER_SCRIPT_PATH}")

MCP_COMMAND = 'python3'  # Assumes the server is a Python script
MCP_ARGS = [
    FINANCIAL_SERVER_SCRIPT_PATH
]

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='financial_advisor_agent',
    instruction=(
        'You are an automated financial advisor. '
        'You can retrieve real-time stock prices, historical financial statements, and company news. '
        'Use the available tools to answer questions about financial markets and companies.'
    ),
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command=MCP_COMMAND,
                args=MCP_ARGS,
            ),
            tool_filter=['get_current_stock_price', 'get_company_news']  # Expose only specific tools
        )
    ]
)