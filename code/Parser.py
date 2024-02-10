class Parser:

    def __init__(self):
        self.query = ''
        self.asc = 'desc'
        self.parsed_query = []

    #Simple parsing method, only has error handling for type input
    #at the moment.
    def parse(self, query):
        try:
            self.parsed_query = query.split(',')
            for term in self.parsed_query:
                term.strip()
        except:
            print("INPUT QUERY CANNOT BE PARSED")
            return
        
# I created this class to act as an object holding info on what we're searching in the DB for
class Query:
    def __init__(self, Lower_Rank, Upper_Rank, Artist, Title, Features):
        self.Lower_Rank = Lower_Rank
        self.Upper_Rank = Upper_Rank
        self.Artist = Artist
        self.Title = Title
        self.Features = Features

# takes a list of commands and arguments after they have been split from each other
    # I designed this to seperate commands and arguments, thought it might be easer than having them combined
# returns a query object containing info on fields and given values
def interpret_query(query_cmds, query_args):
    # sets the query object
    query_contents = Query(None, 1, 40, None, None)
    for arg in query_args:
        for cmd in query_cmds:
            if arg.find(cmd) != -1:
                match cmd:
                    # print help section
                    case 'help':
                        print("Here is a list of commands:\n")
                        print("'help': Displays this list\n")

                        print("'?:': Every user query has to start with this argument\n")

                        print("'{ }': Used to specify which parts of the query are arguments. \n" + 
                            "Example: {Taylor Swift} is used to refer to the artist value Taylor Swift\n")
                        
                        print("'is': Used to query if a provided field is equal to some value. \n" + 
                            "Returns a list of data that the equality holds true for. \n" + 
                            "Example: '?: artist is \{Kanye\}' will return all songs with the Artist 'Kayne'\n")
                        
                        print("'<': Used to query a numeric field, and returns all data where the field value is less than the provided value. \n" + 
                            "Example: '?: rank < \{6\}' will return the first five songs in the dataset\n")

                        print("'>': Used to query a numeric field, and returns all data where the field value is greater than the provided value. \n" +
                            "'Example: '?: rank > \{5\}' will return all songs with rank greater than five\n")

                        print("'of': Used to get another field of a value. \n" + 
                            "Example: '?: rank of {Good Morning}' returns the rank of the song with the Title 'Good Morning'\n")

                        print("'asc': Optional command, used to reverse order of data to pick from the bottom first. Default order is top down. \n" + 
                            "Example: '?: rank > \{15\}, asc' will return songs of ranks 40 through 26\n")
                        
                        print("'exit': Used to exit out of the query program")

                    # TODO:
                    case 'asc':
                        print('asc')

                    case 'is':
                        field = (arg.split(' '))[0].lower() #separates out what "is"; rank, artist, etc.
                        searched = (arg.split(' '))[2]
                        match field:

                            case 'rank':
                                query_contents.Rank = searched

                            case 'artist':
                                query_contents.Artist = searched
                            
                            case 'title':
                                query_contents.Title = searched

                            case 'feature':
                                query_contents.Features = searched
                    # TODO:
                    case '<':
                        # gets the value to test for the field
                        arg1 = query_args[1]

                        # sets the upper rank to search up to
                        query_contents.Upper_Rank = arg1

                    # with the < and > tests, the field being tested will always be rank since that is the only numeric field
                    case '>':
                        # gets the value to test for the field
                        arg1 = query_args[1]

                        # sets the lower rank to start search from
                        query_contents.Lower_Rank = arg1

                    # TODO:
                    case 'of':
                        print('of')

                    # TODO
                    case 'exit':
                        print('exit')
    
    # return the query object
    return query_contents