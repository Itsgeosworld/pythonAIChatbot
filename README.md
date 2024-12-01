# pythonAIChatbot
A simple AI chatbot ran locally using Ollama, where the user can interact with AI using its language model. This project was inspired by TechwithTim. 

**Instructions**
1. Visit [Ollama](https://ollama.com/) to download the large language model (LLM) which would be responsible for running the chatbot on a local machine.
2. To ensure the installation was successful, open the command prompt/terminal to verify the installation
   
   Enter the command, ***ollama***, which shows that Ollama is running and lists the available commands.
   
3. There are different models that can be downloaded, but this is based on the user's PC requirements. For the sake of instructions, the Llama 3 model will be downloaded.
   Enter the command, ***ollama pull llama3***
4. To run the model, enter the command, ***ollama run llama3***. The user can interact with the LLM through the command prompt/terminal.
   
6. To integrate the LLM into Python, firstly, create a virtual environment in Python that will install dependencies needed for the program.
   Enter the following command in Python's terminal: ***python3 -m venv chatbot*** Chatbot is the name of the environment, but it can be changed based on the user's preference.
   
7. Activate the virtual environment.
   The following are different ways to activate the virtual environment depending on what's being used.
   
   If you're using command prompt, enter the command: ***.\chatbot\Scripts\activate.bat***
   If you're using powershell, enter the command: ***.\chatbot\Scripts\Activate.ps1***
   
8. Install the required packages.
   In the terminal, enter the command: ***pip install langchain langchain-ollama ollama***
