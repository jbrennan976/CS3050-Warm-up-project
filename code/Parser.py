class Parser:

    def __init__(self):
        self.query = ''
        self.parsed_query = []
        
# I created this class to act as an object holding info on what we're searching in the DB for
class Query:
    def __init__(self, Lower_Rank, Upper_Rank, Artist, Title, Features, Desc):
        self.Lower_Rank = Lower_Rank # int
        self.Upper_Rank = Upper_Rank # int
        self.Artist = Artist         # string
        self.Title = Title           # string
        self.Features = Features     # bool - false default
        self.Desc = Desc             # bool - false default

# takes a list arguments that contains the user inputs, separated by command
# returns a query object containing info on fields and given values
def interpret_query(query_args):
    # sets the query object
    query_contents = Query(None, None, None, None, False, True)
    for arg in query_args:
        arg = arg.strip()
        field = (arg.split(' '))[0].lower() # which field is to be found

        # special case commands
        if field == "help" or field == "exit" or field == "asc" or field == "all":
            match field:
                # print help list
                case 'help':
                    print("Here is a list of commands:\n")
                    print("'help': Displays this list\n")

                    print("Queriable fields of the data are: 'rank', 'title', 'artist', 'features'")

                    print("Use ',' to input multiple commands\n")

                    print("'all': Command to print all of the items in the dataset\n")

                    print("'{ }': Used to specify which parts of the query are arguments. \n" + 
                        "Example: {Taylor Swift} is used to refer to the artist value Taylor Swift\n")
                    
                    print("'is': Used to query if a provided field is equal to some value. \n" + 
                        "Returns a list of data that the equality holds true for. \n" + 
                        "Example: '?: artist is {Kanye}' will return all songs with the Artist 'Kayne'\n")
                    
                    print("'<': Used to query a numeric field, and returns all data where the field value is less than or equal to the provided value. \n" + 
                        "Example: '?: rank < {6}' will return the first five songs in the dataset\n")

                    print("'>': Used to query a numeric field, and returns all data where the field value is greater than the provided value. \n" +
                        "'Example: '?: rank > {5}' will return all songs with rank greater than or eqaul to five\n")

                    print("'asc': Optional command, used to reverse order of data to pick from the bottom first. Default order is top down. \n" + 
                        "Example: '?: rank > {26}, rank < {40}, asc' will return songs of ranks 40 through 26 starting with 40\n")

                    print("Query examples: \n" +
                          "'?: rank > {15}, rank < {35}, title is {Teenage Dream}, artist is {Katy Perry}' will return songs of ranks 15 through 35 with the title of Teenage Dream and the artist Katy Perry\n" +
                          "'?: rank > {1}, rank < {40}' will return all songs 1-40\n" +
                          "'?: rank > {34}, features is {True}' will return all songs ranked 34 and above with features\n")

                    
                    print("'exit': Used to exit out of the query program\n")
                    return None
                
                # exit program
                case 'exit':
                    print("Ending program")
                    exit()

                # Used to reverse the order of the database
                # This will let us get the bottom 5 by input like: "rank < 5 asc"
                case 'asc':
                    query_contents.Desc = False

                # Prints all of the songs
                case 'all':
                    print("Printing all songs:\n")
                    query_contents.Lower_Rank = 1
                    query_contents.Upper_Rank = 40
                    return query_contents
        
        # specific queried fields
        elif field in ['rank', 'title', 'artist', 'features']:
            try:
                # get the user field
                searched = (arg.split('{')) 
                searched = searched[1].split('}')
                searched = searched[0] # which field is given
                searched = searched.strip()

                # what command is being used
                command = (arg.split(' '))[1].lower()
            except:
                print("Invalid syntax. Did you remember your {}?")
                return
            
            match command:
                case 'is':
                    match field:
                        # Finding specific rank -- Set lower and upper to same val
                        case 'rank':
                            # If the ranks have not been set yet
                            if query_contents.Lower_Rank == None:
                                if query_contents.Upper_Rank == None:
                                    # Set them as int values
                                    try:
                                        query_contents.Lower_Rank = int(searched)
                                        query_contents.Upper_Rank = int(searched)

                                    except:
                                        print("ERROR: MUST USE AN INTEGER FOR THIS VALUE")
                                        return None
                                else:
                                    print("ERROR: CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                                    return None
                            else:
                                print("ERROR: CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                                return None

                        # Finding specific artist
                        case 'artist':
                            if query_contents.Artist == None:
                                query_contents.Artist = searched
                            else:
                                print("ERROR: CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                                return None
                        
                        # Finding specific title
                        case 'title':
                            if query_contents.Title == None:
                                query_contents.Title = searched
                            else:
                                print("ERROR: CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                                return None

                        # Finding songs that have features
                        case 'features':
                            if searched == 'True':
                                query_contents.Features = True
                            elif searched == 'False':
                                query_contents.Features = False
                            else:
                                print("Invalid input. Features can only be {True} or {False}")
                                return None
                
                # with the < and > tests, the field being tested will always be rank since that is the only numeric field
                case '<':
                    # Check if the upper rank has been set yet
                    if query_contents.Upper_Rank == None:
                        try:
                            searched = int(searched)
                        except:
                            print("ERROR: MUST USE AN INTEGER FOR THIS VALUE")
                            return None

                        # sets the upper rank to search up to
                        query_contents.Upper_Rank = int(searched)
                    
                    else:
                        print("ERROR: CANNOT GIVE TWO '<' VALUES FOR THE SAME FIELD")
                        return None

                # with the < and > tests, the field being tested will always be rank since that is the only numeric field
                case '>':
                    # Check if the lower rank has been set yet
                    if query_contents.Lower_Rank == None:
                        try:
                            searched = int(searched)
                        except:
                            print("ERROR: MUST USE AN INTEGER FOR THIS VALUE")
                            return None

                        # sets the lower rank to start search from
                        query_contents.Lower_Rank = int(searched)
                    
                    else:
                        print("ERROR: CANNOT GIVE TWO '>' VALUES FOR THE SAME FIELD")
                        return None
                        
                # We didn't get this to work in time
                        
                # To simplify the 'of' case, we'll say that the second term/arg will always be "title"
                # case 'of':
                #     query_contents.Title = searched
                #     match field:
                #         case 'rank':
                #             query_contents.Lower_Rank = "RANK OF SONG"
                #             query_contents.Upper_Rank = "RANK OF SONG"

                #         case 'artist':
                #             query_contents.Artist = "ARTIST OF SONG"

                #         case 'title':
                #             print("ERROR: CANNOT SEARCH FOR TITLE OF TITLE")
                #             return None

                #         case 'feature':
                #             query_contents.Features = "FEATURES OF SONG"

                case _:
                    print('ERROR: UNKNOWN COMMMAND. Please type \'help\' for a list of commands')
                    return None
        else:
            print("Invalid input")
            return

    # if lower and upper ranks were not set, set them to default values
    if query_contents.Lower_Rank == None:
        query_contents.Lower_Rank = 1
    
    if query_contents.Upper_Rank == None:
        query_contents.Upper_Rank = 40

    # if the user chooses to read ranks in reverse order, adjust rank search values
    if query_contents.Desc == False:
        low_temp = 40 - (query_contents.Upper_Rank - 1)
        high_temp = 40 - (query_contents.Lower_Rank - 1)
        query_contents.Lower_Rank = low_temp
        query_contents.Upper_Rank = high_temp
        pass

    # return the query object
    return query_contents

# Using this for testing output -- Feel free to change
# contents = interpret_query(['rank > {20}'])

# print(contents)