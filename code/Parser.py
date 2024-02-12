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
def interpret_query(query_args):
    # sets the query object
    query_contents = Query(None, None, None, None, None)
    for arg in query_args:
        field = (arg.split(' '))[0].lower() # which field is to be found
        searched = (arg.split('{')) 
        searched = searched[1].split('}')
        searched = searched[0] # which field is given

        command = (arg.split(' '))[1].lower()
        match command:
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
                match field:
                    # Finding specific rank
                    case 'rank':
                        # If the ranks have not been set yet
                        if query_contents.Lower_Rank == None:
                            if query_contents.Upper_Rank == None:
                                # Set them as int values
                                try:
                                    query_contents.Lower_Rank = int(searched)
                                    query_contents.Upper_Rank = int(searched)

                                except:
                                    print("MUST USE AN INTEGER FOR THIS VALUE")
                                    break
                            else:
                                print("CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                                return None
                        else:
                            print("CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                            return None

                    # Finding specific artist
                    case 'artist':
                        if query_contents.Artist == None:
                            query_contents.Artist = searched
                        else:
                            print("CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                            return None
                    
                    # Finding specific title
                    case 'title':
                        if query_contents.Title == None:
                            query_contents.Title = searched
                        else:
                            print("CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                            return None

                    # Finding specific feature
                    case 'feature':
                        if query_contents.Features == None:
                            query_contents.Features = searched
                        else:
                            print("CANNOT GIVE TWO 'IS' VALUES FOR THE SAME FIELD")
                            return None
            # with the < and > tests, the field being tested will always be rank since that is the only numeric field
            case '<':
                # Check if the upper rank has been set yet
                if query_contents.Upper_Rank == None:
                    try:
                        searched = int(searched[0])
                    except:
                        print("MUST USE AN INTEGER FOR THIS VALUE")
                        break

                    # sets the upper rank to search up to
                    query_contents.Upper_Rank = int(searched)
                
                else:
                    print("CANNOT GIVE TWO '<' VALUES FOR THE SAME FIELD")

            # with the < and > tests, the field being tested will always be rank since that is the only numeric field
            case '>':
                # Check if the lower rank has been set yet
                if query_contents.Lower_Rank == None:
                    try:
                        searched = int(searched[0])
                    except:
                        print("MUST USE AN INTEGER FOR THIS VALUE")
                        break

                    # sets the lower rank to start search from
                    query_contents.Lower_Rank = int(searched)
                
                else:
                    print("CANNOT GIVE TWO '>' VALUES FOR THE SAME FIELD")

            # TODO:
            case 'of':
                match field:
                    case 'rank':
                        pass

                    case 'artist':
                        pass

                    case 'title':
                        pass

                    case 'feature':
                        pass

            # TODO
            case 'exit':
                print('exit')
    
    # if lower and upper ranks were set, set them to default values
    if query_contents.Lower_Rank == None:
        query_contents.Lower_Rank = 1
    
    if query_contents.Upper_Rank == None:
        query_contents.Upper_Rank = 40

    # return the query object
    return query_contents

# Using this for testing output -- Feel free to change
contents = interpret_query(['rank is {Taylor Swift}'])

print(contents)