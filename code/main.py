from Parser import interpret_query
from query import query_db

def main():
    print('Software Engineering Warm-Up Project')
    print("Enter queries below. Enter 'help' for a list of commands")
    # This loop will run until the user enters 'exit'
    user_input = ''
    results = []

    while user_input.find("exit") == -1:
        results.clear()
        user_input = input('?: ')
        print("\n")
        send_to_parser = []
        send_to_parser = user_input.split(',')
        send_to_query = interpret_query(send_to_parser)
        if send_to_query != None:
            results = query_db(send_to_query)
            pass
        for dict in results:
            print(dict,"\n")
        if len(results) == 0:
            print("No songs found\n")
    return

main()