import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


# responsible for saving chat history into json file
def save_conversation(data, filename="logs.json"):
    try:
        with open(filename, "r") as f:  # firstly reads data if file exists
            current_data = json.load(f)
    except FileNotFoundError:
        current_data = []

    current_data.append(data)

    # updated chat history is written to file
    with open(filename, "w") as f:
        json.dump(current_data, f)


def conversation():
    context = ""
    chats = []  # chats of all conversations are intialized to an empty list
    print("Welcome to the AI Chatbot, Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("ChatBot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

# The user's and chatbot's responses are appended to the list 
        chats.append({"User:": user_input, "ChatBot:": result})


if __name__ == "__main__":
    conversation()
