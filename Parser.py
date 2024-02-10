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