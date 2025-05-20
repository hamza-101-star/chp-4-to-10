def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)  # Remove the first message from the list
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = [
    "Hey, how are you?",
    "Don't forget the meeting at 3 PM.",
    "Happy Birthday!",
    "Call me when you're free.",
    "Let's catch up soon!"
]

sent_messages = []

send_messages(text_messages, sent_messages)

print("\nOriginal messages list (should be empty now):")
print(text_messages)

print("\nSent messages list:")
print(sent_messages)
