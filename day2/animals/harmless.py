class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member fish
        self.members = ['Tuna', 'Sardine']
    def printMembers(self):
        print('Printing members of the harmless Fish class')
        for member in self.members:
            print('\t%s ' % member)
            
class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
    def printMembers(self):
        print('Printing members of the harmless Birds class')
        for member in self.members:
            print('\t%s ' % member)
            
class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Elephant']
    def printMembers(self):
        print('Printing members of the harmless Mammals class')
        for member in self.members:
            print('\t%s ' % member)