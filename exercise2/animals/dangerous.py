class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member fish
        self.members = ['Shark']
    def printMembers(self):
        print('Printing members of the dangerous Fish class')
        for member in self.members:
            print('\t%s ' % member)
            
class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = []
    def printMembers(self):
        print('Printing members of the dangerous Birds class')
        for member in self.members:
            print('\t%s ' % member)
            
class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Wild Cat']
    def printMembers(self):
        print('Printing members of the dangerous Mammals class')
        for member in self.members:
            print('\t%s ' % member)