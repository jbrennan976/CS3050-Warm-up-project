from Parser import interpret_query
from query import query_db

def main():
    # Welcome prompt
    print('Software Engineering Warm-Up Project')
    print("Enter queries below. Enter 'help' for a list of commands")
    # This loop will run until the user enters 'exit'
    user_input = ''
    results = []

    # while the user hasn't chosen to end the program
    while user_input.find("exit") == -1:
        # reset user input and (re)prompt
        results.clear()
        user_input = input('?: ')
        print("\n")

        # create the list of queries to send to the parser
        send_to_parser = []
        send_to_parser = user_input.split(',')

        # send the queries to check
        send_to_query = interpret_query(send_to_parser)
        
        # if there is a valid query to check
        if send_to_query != None:
            # query the database
            results = query_db(send_to_query)

            # print the results returned from the database
            for dict in results:
                result = ""
                for elt in dict:
                    # print everything except for 'has_feature'
                    if elt != 'has_feature':
                        # if a field is empty, don't print it
                        if str(dict[elt]) != "":
                            result += elt + ': ' + str(dict[elt]) + ' '
                print(result,"\n")
            # if nothing is found
            if len(results) == 0:
                print("No songs found\n")
    return

main()