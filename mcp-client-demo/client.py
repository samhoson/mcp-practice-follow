from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv", # Executable
    args=[
        "run",
        "--with",
        "mcp[cli]",
        "--with-editable",
        "D:\\workspace\\python\\mcp-test\\achievement",
        "mcp",
        "run",
        "D:\\workspace\\python\\mcp-test\\achievement\\server.py"
    ],# Optional command line arguments
    env=None # Optional environment variables
)
