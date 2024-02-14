from Parser import interpret_query
import query

def main():
    print('Software Engineering Warm-Up Project')
    print("Enter queries below. Enter 'help' for a list of commands")
    # This loop will run until the user enters 'exit'
    user_input = ''
    while user_input.find("exit") == -1:
        user_input = input('?: ')
        send_to_parser = []
        send_to_parser = user_input.split(',')
        send_to_query = interpret_query(send_to_parser)
        if send_to_query != None:
            # use send_to_query in query.py
            pass
        # print(send_to_query)