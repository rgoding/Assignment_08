#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# Rgoding, 2020-Sept-01, created file
# Rgoding, 2020-Sept-01, created class CD()
# Rgoding, 2020-Sept-02, Brought over load and save functions
# Rgoding, 2020-Sept-02, Modified Main Body from Previous Assignment
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:
    properties:
        intId: (int) with CD ID
        strTitle: (string) with the title of the CD
        strArtist: (string) with the artist of the CD
        
    methods:
        __str__: returns formatting of properties
    """
    #Constructor
    def __init__(self, ID, Title , Artist):
        self.__intID = ID
        self.__strTitle = Title
        self.__strArtist = Artist
    
    
    #Properties
    @property
    def intID(self):
        return self.__intID
    
    @intID.setter
    def intID(self, value):
        self.intID = value
    
    @property
    def strTitle(self):
        return self.__strTitle
    
    @strTitle.setter
    def strTitle(self, value):
        self.strTitle = value
    
    @property
    def strArtist(self):
        return self.__strArtist
    
    @strArtist.setter
    def strArtist(self, value):
        self.strArtist = value
    
   

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:
    properties:
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """
    @staticmethod
    def load_inventory(file_name, table):
        """Function to manage data ingestion from file to a list of objects
        
        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one dictionary row in table.
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
            
        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        with open(file_name, 'r') as objFile:
                for row in objFile:
                    data = row.strip().split(',')
                    CDobj = CD(data[0],data[1],data[2])
                    table.append(CDobj)
                print('Data from ' + strFileName +' loaded')
        
        
    
    @staticmethod
    def save_inventory(file_name, table):
        """Function to write data from the table to a file
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns: 
            None
        """
              
        with open(file_name, 'w') as objFile:
                for obj in table:
                    data = (str(obj.intID) + ',' + str(obj.strTitle) + ',' + str(obj.strArtist) + '\n')
                    objFile.write(data)
                print('Inventory Data Saved to ' + strFileName)
       
        
        
        
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """

        print('Menu\n\n[l] Show inventory from file\n[a] Add CD to inventory')
        print('[i] Display Current Inventory\n[s] Save Inventory to file\n[x] exit\n')
        
    
    @staticmethod
    def menu_choice():  
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

        
    @staticmethod
    def show_inventory(table):  
        """Displays current inventory table
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for obj in table:
            print('{}\t{} (by:{})'.format(obj.intID,obj.strTitle,obj.strArtist))
        print('======================================\n')

    @staticmethod
    def new_cd():
        """Function to prompt user for new CD attributes
        
        Args:
            strID: user input for CD ID
            strTitle: CD title
            strArtist: artist name
            
        Returns:
            intID, strTitle, strArtist
        
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        intID = int(strID)
        return intID, strTitle, strArtist
    

# -- Main Body of Script -- #
# 1. When program starts, read in the currently saved Inventory
# Add Error exceptions to display error instead of closing program
try:
    FileIO.load_inventory(strFileName, lstOfCDObjects)
except:
    print("No text file found in local folder, please create CDInventory.txt")
while True:
    #Display Menu to user and get choice
    IO.print_menu() 
    strChoice = IO.menu_choice()

    if strChoice == 'x': # process exit request
        break
    
    if strChoice == 'l': # process load inventory from file
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Do you want to continue? [y/n] ')
        #Error Handling if file is not created
        try:
            if strYesNo.lower() == 'y':
                print('reloading...')
                FileIO.load_inventory(strFileName, lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
        except:
            print("CDInventory.txt does not exist in local directory")
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
    
    elif strChoice == 'a': # process add a CD
        #IO.add_cd() will request user for input
        intID, strTitle, strArtist = IO.new_cd()
        # Instantiate CD Class object
        objCD = CD(intID, strTitle, strArtist) 
        lstOfCDObjects.append(objCD)
        #Display Inventory
        IO.show_inventory(lstOfCDObjects) 
        continue  
    
    elif strChoice == 'i': # process display current inventory
        IO.show_inventory(lstOfCDObjects)
        continue  
    
    elif strChoice == 's': # process save inventory to txt file
        IO.show_inventory(lstOfCDObjects) # Display current inventory and ask user for confirmation to save
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        #Process choice
        if strYesNo == 'y':
            #write data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')