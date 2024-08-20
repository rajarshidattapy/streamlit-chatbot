import openai

# Set up your OpenAI API key
openai.api_key ="api key"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

def main():
    print("Chatbot is running. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
