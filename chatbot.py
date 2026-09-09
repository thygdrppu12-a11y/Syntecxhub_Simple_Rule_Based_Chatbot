import datetime
import re

# Simple Rule-Based Chatbot for Syntecxhub Internship

def log_conversation(user_input, bot_response):
    """Logs conversation history to a text file."""
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] User: {user_input}\n")
        file.write(f"[{timestamp}] Bot: {bot_response}\n\n")

def get_bot_response(user_input):
    """Processes input and returns rule-based response."""
    text = user_input.lower().strip()

    # Rule 1: Greetings
    if re.search(r'\b(hi|hello|hey|greetings|good morning|good evening)\b', text):
        return "Hello! Welcome to Syntecxhub AI Support. How can I help you today?"

    # Rule 2: Help / Capabilities
    elif re.search(r'\b(help|support|what can you do|features)\b', text):
        return "I can answer questions about Syntecxhub internships, AI concepts, and basic navigation. Type 'exit' to end our chat."

    # Rule 3: Knowledge Base - Internships
    elif re.search(r'\b(internship|program|domain|tasks)\b', text):
        return "Syntecxhub offers internships across AI, Web Development, Data Science, and UI/UX with weekly practical tasks."

    # Rule 4: Knowledge Base - AI & Python
    elif re.search(r'\b(ai|artificial intelligence|python)\b', text):
        return "Artificial Intelligence leverages algorithms like rule-based bots, search algorithms, and machine learning models to solve complex problems."

    # Rule 5: Small Talk
    elif re.search(r'\b(how are you|how do you do)\b', text):
        return "I'm doing great! Ready to assist you with your queries."

    elif re.search(r'\b(thank you|thanks)\b', text):
        return "You're very welcome! Let me know if you need anything else."

    # Rule 6: Exit
    elif text in ['exit', 'quit', 'bye', 'goodbye']:
        return "Goodbye! Have a great day ahead."

    # Default Response
    else:
        return "I'm sorry, I didn't quite understand that. You can ask me about 'internships', 'AI', or type 'help'."

def run_chatbot():
    print("=" * 50)
    print("      Syntecxhub Rule-Based Chatbot Active      ")
    print("       (Type 'exit' or 'bye' to end chat)        ")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")
        if not user_input.strip():
            continue

        response = get_bot_response(user_input)
        print(f"Bot: {response}")

        log_conversation(user_input, response)

        if user_input.lower().strip() in ['exit', 'quit', 'bye', 'goodbye']:
            break

if __name__ == "__main__":
    run_chatbot()
