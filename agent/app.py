import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Alex. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()


# reflectio  lab 1
#1)the internet history it holds every single person that used it and it goes over his nfo and details , count how much you have to pay each month and track the payment details so every time it want to use this info it go back to the history 
#a)history.append({'role': 'assistant', 'content': reply}) It still remembers what I asked because the user messages are saved but it forgets what it replied before
#b) load_dotenv()  when using it the code doesent work because API key isn't loaded from the .env file without the key the API call doesnt work
#c)the chatbot still runs normally but its kinda change the personality so it less creative
#d) if you remove the break the code continue working if you press exit it doesnt 
#3)the api code didnt work at the beggining and i solve it by reciving another api code and capitalaise the vairble 

