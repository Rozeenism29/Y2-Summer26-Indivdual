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
        print('History:', history)
        print('History so far:', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        print(response)
        reply = response.content[0].text
        print(response)
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


#lab2 (not finished)
#step1 the input token is how much it tkes to process your question and the output is how much it takes for the code to print the reply 
#step2 
#it crached because i wrote a messege more than 50 letters 
#the temprusyre baisclly controll how much uniqu the answers are so whne changinging it to 0 it gave same resposees but when rechange it to 1 it start giving more varied answers
# history prints double of what you enter so remember what has already been said and give responses that continue the conversation so because we enterd 3 messeges that means were gonna have 6 messeges in the history  
# a)The ai only receives the previous conversation history so it doesn't know what I just typed. The input_tokens count is also lower because the new user message isn't included.
#b)The ai forgets what it said before and the token count grows more slowly because assistant messages are no longer added to the history
#c) My Anthropic API credits had run out, so I no longer had access to make requests I thought there was something wrong with my code and for the gap it was a coding bug,