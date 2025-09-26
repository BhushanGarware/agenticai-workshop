# agenticai-workshop
A starter kit for building basic AI agents with the Gemini API. Covers examples using LangChain, LangGraph, the Google ADK, and an MCP server.

## Getting Started 
### 1. Get your Gemini API KEY
You can get a free Gemini API key for learning and development purposes directly from [Google AI Studio](https://aistudio.google.com/).
This key provides access to a generous free tier, which is perfect for learning, prototyping, and personal projects.

#### Here are the simple steps to get your key:

1. ##### Go to Google AI Studio:
Navigate to the official [Google AI Studio website](https://aistudio.google.com/).

2. ##### Sign In:
Sign in using your personal Google account.

3. ##### Agree to Terms:
If it's your first time, you will likely need to read and agree to the Terms of Service.

4. ##### Get API Key:
Once in the studio, look for a button or link on the left-hand side labeled "Get API key".

5. ##### Create API Key:
On the API key page, click the button that says "Create API key". You may be prompted to create a new Google Cloud project for your key. This is a standard step and is still part of the free process.

6. ##### Copy Your Key:
Your new API key will be generated and displayed. This is the only time you will see the full key, so copy it immediately.

### Important: Keep Your Key Secure
1. Treat your API key like a password. Never share it publicly.
2. Do not paste it into your code if you are sharing that code (e.g., on GitHub).

###### For projects, use environment variables to store your key securely.

### 2. Installing Google ADK
1. ##### Create & activate virtual environment:
We recommend creating a virtual Python environment using venv:

             python -m venv adk_workshop

Now, you can activate the virtual environment using the appropriate command for your operating system and environment:

              # Mac / Linux 
              source adk_workshop/bin/activate
              # Windows CMD:
              adk_workshop\Scripts\activate.bat
              # Windows PowerShell:
              adk_workshop\Scripts\Activate.ps1

Install ADK

             pip install google-adk


### 3. Running MCP Demo
1. #### Install required packages
             pip install "mcp[cli]" httpx
2. #### Get API Key
    Get a free API key from https://www.financialdatasets.ai/ and update .env file in MCP_Server
3. #### Run the MCP Server
            python server.py
   Once the server is running, you should see a message like:

financial-datasets-mcp - INFO - Starting Financial Datasets MCP Server...
This means the server is ready to accept JSON-RPC requests from any MCP-compatible client, including your ADK agent.

4. #### Run the MCP Client
   Update the .env with GOOGLE_API_KEY and execute from parent directory 
   
            adk web 
   
   
   
  


             



