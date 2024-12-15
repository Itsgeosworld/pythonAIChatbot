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


def conversation():
    context = ""
   # chats = []  chats of all conversations are initialized to an empty list
    print("Welcome to the AI Chatbot, Type 'exit' to quit. Enter 1 to view conversation history.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if user_input.lower() == "1":
            with open('logs.json', 'r') as file:
                print(file.read())
                continue
        result = chain.invoke({"context": context, "question": user_input})
        print("ChatBot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

        # idea:when the user enters previous session, the user's previous conversation with the model is shown

        # The user's and chatbot's responses are appended to the list
       # chats.append(context)


        with open('logs.json','a') as file:
            file.write(context)

      #  with open("logs.json",'r') as file:
      #      print(file.read())


        # testing purposes which prints the user and AI's chat
       # print(context)


if __name__ == "__main__":
    conversation()
