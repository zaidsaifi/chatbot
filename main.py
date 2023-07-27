import tkinter as tk
from tkinter import ttk
import random

def get_random_response(responses):
    return random.choice(responses)

def get_bot_response(user_input):
    user_input = user_input.lower()
    bot_responses = {
        "hello": ["Hello! What's your emergency?", "Hi there! What's your emergency?", "Hey! Whats your emergency?", "Greetings! Whats your emergency?"],
        "how are you": ["I'm just a medical emergency chatbot, but thank you for asking.", "I'm here to assist with medical emergencies."],
        "what's your name": ["I'm a medical emergency chatbot. You can call me medcare.", "You can call me medcare."],
        "bye": ["Stay safe and take care!", "Wishing you good health! Goodbye!"],
        "i am having chestpain": ["Chest pain could be a symptom of a heart attack. Please call emergency services (112 or 102) immediately for immediate assistance.", "If you are experiencing severe chest pain, do not hesitate to call for emergency help."],
        "difficulty breathing": ["If you are having difficulty breathing, it could be a sign of a serious medical condition. Seek immediate medical attention.", "Breathing difficulsties can be serious. It is best to seek medical help right away."],
        "what should I do if I am bleeding": ["If you are experiencing uncontrolled bleeding, apply pressure to the wound and seek immediate medical assistance.", "For uncontrolled bleeding, apply pressure and get medical help as soon as possible."],
        "I have got  little burns": ["For minor burns, run cool water over the affected area. Seek medical attention for severe burns or if the burn covers a large area.", "Treat minor burns with cool water and consider medical help for severe burns."],
        "what should i do if someone is choking": ["If someone is choking and cannot breathe or talk, perform the Heimlich maneuver or call emergency services.", "For a choking person, use the Heimlich maneuver or seek immediate help."],
        "what should i do if someone is having seizure": ["During a seizure, ensure the person's safety by removing hazards. Do not restrain them. After the seizure, stay with them and offer support.", "For a person having a seizure, ensure safety and offer support afterwards."],
        "i have got allergic reaction": ["For severe allergic reactions (anaphylaxis), use an epinephrine auto-injector if available and seek immediate medical help.", "Anaphylaxis requires an epinephrine auto-injector and urgent medical assistance."],
        "what should i do if someone got poisoning": ["If someone is poisoned, call emergency services(112 or 102)  or the poison control center immediately. Do not induce vomiting without professional advice.", "In case of poisoning, call emergency services or the poison control center for immediate guidance."],
        "default": ["I'm sorry, I don't understand.", "Please seek professional medical advice for any emergency situation."]
    }
    return bot_responses.get(user_input, bot_responses["default"])

def on_send_message():
    user_input = user_entry.get()
    if user_input.lower() == "bye":
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        chat_log.insert(tk.END, "MedCare: " + get_random_response(get_bot_response("bye")) + "\n\n")
        user_entry.delete(0, tk.END)
    else:
        response = get_bot_response(user_input)
        bot_response = "MedCare: " + get_random_response(response) + "\n\n"
        chat_log.insert(tk.END, "You: " + user_input + "\n\n")
        chat_log.insert(tk.END, bot_response)
        user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Medical Emergency Chatbot")

chat_frame = ttk.Frame(root)
chat_frame.pack(expand=True, fill="both")

chat_log = tk.Text(chat_frame, wrap="word", bg="white", font=("Arial", 14))
chat_log.pack(expand=True, fill="both")

input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

user_entry = ttk.Entry(input_frame, width=50, font=("Arial", 14))
user_entry.pack(side="left", padx=5)

send_button = ttk.Button(input_frame, text="Send", command=on_send_message)
send_button.pack(side="left", padx=5)

user_entry.bind("<Return>", on_send_message)

root.mainloop()
