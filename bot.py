import smtplib
import webbrowser
from datetime import datetime

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Chatbot:Hello %1, How are you today ?", ]
    ],

    [
        r"who made you",
        ["Chatbot:i was made by Akshat Nayak on 18th December", ]
    ],

    [
        r"using which module were you created",
        ["Chatbot:i was made using nltk module of python", ]
    ],

    [
        r"what is python",
        [
            "Chatbot:Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. It was made in 1992 by Guido Van Rossum in CWI(central wiskhunde and informatica in the netherlands"]
    ],

    [
        r"what is your name",
        ["Chatbot:my name is chatbot 17878."],
    ],

    [
        r"ok bye",
        ["bye, type quit to leave.  Have a good day :)"]
    ],

    [
        r"do you know the generations of computers",
        ["Yes, First Generation The period of first generation: 1946-1959\n."
         " Vacuum tube based. Second Generation The period of second generation: 1959-1965. Transistor based\n. "
         "	Third Generation The period of third generation: 1965-1971. Integrated Circuit based\n."
         "	Fourth Generation The period of fourth generation: 1971-1980. VLSI microprocessor based\n."
         "Fifth Generation The period of fifth generation: 1980-onwards. ULSI microprocessor based\n."]
    ],

    [
        r"do you know anything about chatbots?",
        [
            'Chatbot:Yes a computer program designed to simulate conversation with human users, especially over the internet is a chatbot.']
    ],

    [
        r"what is html?",
        [
            "Chatbot:Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript"]
    ],

    [
        r"I am angry!",
        [
            "Chatbot:What I remember most about my dad’s jokes is my mother’s reaction. While everyone else was howling at one of his punch lines, my mom would always respond, “Bernard, no one thinks you’re funny.”"]
    ],

    [
        r"How many countries are there in the world",
        ["Chatbot:There are 197 countries in the world"]
    ],

    [
        r"What is the time",
        ["Chatbot:Plz rerun the program, it will ask you if u want to know the time:)"]
    ]

]


def current_time():
    from datetime import datetime

    now = datetime.now()

    current_time1 = now.strftime("%H:%M:%S")
    print("Current Time =", current_time1)


def rock_paper_scissors_game():
    from random import randint

    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]

    # assign a random play to the computer
    computer = t[randint(0, 2)]

    # set player to False
    player = False

    while player == False:
        # set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        elif player == "quit":
            break
        else:
            print("That's not a valid play. Check your spelling!")
        # player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0, 2)]


def random_password_generator():
    import string
    import random

    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    PUNCTUATION = string.punctuation

    def get_password_length():
        length = input("How long do you want your password: ")
        return int(length)

    def password_generator(cbl, length=8):

        # create alphanumerical by fetching string constant
        printable = fetch_string_constant(cbl)

        # convert printable from string to list and shuffle
        printable = list(printable)
        random.shuffle(printable)

        # generate random password
        random_password = random.choices(printable, k=length)

        # convert generated password to string
        random_password = ''.join(random_password)
        return random_password

    def password_combination_choice():

        # retrieve a user's password character combination choice
        want_digits = input("Want digits ? (True or False) : ")
        want_letters = input("Want letters ? (True or False): ")
        want_puncts = input("Want punctuation ? (True or False): ")

        # convert those choices from string to it's right boolean type
        try:
            want_digits = eval(want_digits.title())
            want_puncts = eval(want_puncts.title())
            want_letters = eval(want_letters.title())
            return [want_digits, want_letters, want_puncts]

        except NameError as e:
            print("Invalid value. Use either True or False")
            print("Invalidity returns a default, try again to regenerate")

        return [True, True, True]

    def fetch_string_constant(choice_list):

        string_constant = ''

        string_constant += NUMBERS if choice_list[0] else ''
        string_constant += LETTERS if choice_list[1] else ''
        string_constant += PUNCTUATION if choice_list[2] else ''

        return string_constant

    if __name__ == '__main__':
        length = get_password_length()
        choice_list = password_combination_choice()
        password = password_generator(choice_list, length)

        print(password)


def onlineclass():
    webbrowser.open('https://cornerstonepublicschool.codetantra.com/secure/tla/m.jsp')


def chatty():
    print(
        "Chatbot:Hi, I'm a chatbot and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ")  # default message at the start
    inputclass = input("Chatbot:Are you getting late for your class, type y for yes and n for no:")
    if inputclass == "y":
        onlineclass()
        print("Chatbot:NO MORE CHATTING, GO TO YOUR CLASS --_--")
    else:
        do_you_Want_to_open_any_website = input("Chatbot:Do you want to open any website, y for yes, n for no:")
        if do_you_Want_to_open_any_website == "y":
            i11 = input("Chatbot:Which website do you want to open:")
            webbrowser.open(i11)

            chat = Chat(pairs, reflections)
            chat.converse()
        else:
            do_u_want_to_Send_mail = input("Chatbot :DO you want to send a mail, y for yes and n for no:")
            if do_u_want_to_Send_mail == "y":
                email_id = input("Chatbot:TO WHOM U WANT TO SEND MAIL:")

                def send_email(subject, msg):
                    try:
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.ehlo()
                        server.starttls()
                        server.login('akshat.nayak027@gmail.com', 'Akshat200927')
                        message = 'Subject: {}\n\n{}'.format(subject, msg)
                        server.sendmail('akshat.nayak027@gmail.com', email_id, message)
                        server.quit()
                        print("Success: Email sent!")
                    except:
                        print("Email failed to send.")

                subject = input("ChatbotWhat is the subject of your mail:")
                msg = input("Chatbot:What is the message of ur mail:")
                send_email(subject, msg)

                chat = Chat(pairs, reflections)
                chat.converse()

            else:
                random_password = input("Chatbot:Do you want a random password generator, y for yes, n for no:")
                if random_password == "y":
                    random_password_generator()

                    game = input("Chatbot: Do you want to play Rock Paper scissors with the computer:")
                    if game == "y":
                        rock_paper_scissors_game()
                        chat = Chat(pairs, reflections)
                        chat.converse()
                    else:
                        chat = Chat(pairs, reflections)
                        chat.converse()

                else:
                    game = input("Chatbot: Do you want to play Rock Paper scissors with the computer:")
                    if game == "y":
                        rock_paper_scissors_game()
                        chat = Chat(pairs, reflections)
                        chat.converse()
                    else:
                        time = input("Chatbot:Do you want to know the time, y for yes, n for no:")
                        if time == "y":
                            current_time()
                            chat = Chat(pairs, reflections)
                            chat.converse()
                        else:
                            chat = Chat(pairs, reflections)
                            chat.converse()


chatty()
