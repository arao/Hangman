import os
import random

VOCABULARY = None


class Flash:
    message = ""

    def clear(self):
        self.message = None

    def print(self):
        if self.message:
            console_output(self.message)
            self.clear()

    def setmessage(self, message):
        self.message = message

    def getmessage(self):
        return self.message


def init():
    with open('./words.txt', 'r') as ip:
        global VOCABULARY
        VOCABULARY = ip.read().split('\n')


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def word():
    return VOCABULARY[random.randint(0, len(VOCABULARY))]


def console_input(data=">>>") -> str:
    data = list(input(data))
    return data[0].lower()


def console_output(output_word):
    if isinstance(output_word, list):
        print("".join(output_word))
    else:
        print(output_word)


def hangman(index=0):
    man = (
        '''
                       _____
                      /     \\
                     |       |
                      \_____/
        ''',
        '''
                       _____
                      /     \\
                     |       |
                      \_____/
                       |   |
                       |   |
        ''',
        '''
                       _____
                      /     \\
                     |       |
                      \_____/
                       |   |
                       |   |
                    ___|___|___
                   |           |
                   |           |
                   |           | 
                   |           |
                   |___________|
        ''',
        '''
                       _____
                      /     \\
                     |       |
                      \_____/
                       |   |
                       |   |
                    ___|___|___
                  /|           |
                 / |           |
                /  |           | 
               /   |           |
             /|\   |___________|
        ''',
        '''
                       _____
                      /     \\
                     |       |
                      \_____/
                       |   |
                       |   |
                    ___|___|___
                  /|           |\\
                 / |           | \\
                /  |           |  \\
               /   |           |   \\
              /|\  |___________|  /|\\
        ''',
        '''
                       _____
                      /     \\
                     |       |
                      \_____/
                       |   |
                       |   |
                    ___|___|___
                  /|           |\\
                 / |           | \\
                /  |           |  \\
               /   |           |   \\
              /|\  |___________|  /|\\
                      |
                      |
                      |
                      |
                     /|\  
        ''',
        '''
                       _____
                      /     \
                     |       |
                      \_____/
                       |   |
                       |   |
                    ___|___|___
                  /|           |\\
                 / |           | \\
                /  |           |  \\
               /   |           |   \\
              /|\  |___________|  /|\\
                      |    |
                      |    |
                      |    |
                      |    |
                     /|\  /|\\
        ''',
        '''
        ________________________________
                |      _____
                 \    /     \\
                  \  |       |
                   \  \_____/
                    \  |   |
                     \_|   |_
                    ___|___|___
                  /|           |\\
                 / |           | \\
                /  |           |  \\
               /   |           |   \\
              /|\  |___________|  /|\\
                      |    |
                      |    |
                      |    |
                      |    |
                     /|\  /|\\
        ''',
    )
    if index < 0:
        return True
    elif index < 7:
        print(man[index])
        return True
    else:
        print(man[7])
        return False


def controller():
    hangman_counter = -1
    hidden_word = list(word())
    revealed_word = ['_'] * len(hidden_word)
    revealed_word_counter = 0
    garbage = []
    clear()
    flash_message = Flash()
    console_output('>>>>>>>>>>>>>>> Game starts <<<<<<<<<<<<<')
    while hangman(hangman_counter) and revealed_word_counter < len(hidden_word):
        # console_output(hidden_word)
        console_output(revealed_word)
        flash_message.print()
        new_alphabate = console_input()
        inc = True
        if new_alphabate not in revealed_word and new_alphabate not in garbage:
            for index, item in enumerate(hidden_word):
                if item == new_alphabate:
                    revealed_word[index] = new_alphabate
                    revealed_word_counter += 1
                    inc = False
            if inc:
                garbage.append(new_alphabate)
                hangman_counter += 1
            clear()
        else:
            flash_message.setmessage('word already used')
        clear()
    if hangman_counter >= 7:
        console_output('You Are Dead Man')
        return False
    else:
        console_output('Winner Winner Chicken Dinner')
        return True


def main():
    last_match = controller()
    while True:
        if last_match:
            choice = console_input('You are a winner, give it another shot (y/n)>>> ')
        else:
            choice = console_input('You loose last match , give it another shot (y/n)>>> ')
        if choice == 'n':
            exit(0)
        elif choice == 'y':
            clear()
            last_match = controller()
        else:
            console_output('choose right option')


if __name__ == '__main__':
    code = None
    try:
        init()
        main()
        code = 0
    except Exception as e:
        print(str(e))
        code = -1
    finally:
        print('program terminates')
        exit(code)
else:
    print('There is nothing for you')
    exit(-1)
