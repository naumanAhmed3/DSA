#===================================
#===================================
# Name   :  Nouman Ahmed
# Roll no:  251--713559
# Section: B
# Date   : December 4th , 2022 . Sunday 
#===================================
#===================================


#------------------------------------
# Node class for a Doubly Linked List
#------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
#------------------------------------


class TextEditor:
    def __init__(self, row = -1 , col = -1 , material = [], lines = 0):
        '''
        Predefined member variables. 
        
        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        
        self.doc = None   # The root of everything. See page 2 for details
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        self.temp = self.doc
        self.row , self.col = row , col 
        self.cur = [self.row , self.col]
        self.material = []
        self.lines = lines


        
        
        #======================
        
#======================
    def goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        
         # self.temp is set to be equal to self.doc everytime the function is called 




       
        row_count  = 0 
        col_count = 0
        #self.cur[0] = 0
        #self.cur[-1] = 0
        

        if (row == 0)  :      # if row is 0 .i.e if the user wants to move cur somewhere in the first row 
              self.temp = Node(Node(None,self.temp))
              self.doc = self.temp
              self.cur[0] = self.cur[0] +1
              self.row = self.cur[0]
              row_count = self.row
              self.temp = self.temp.data 
              self.cur[-1] = self.cur[-1] +1 
              self.col = self.cur[-1] 
              col_count = self.col 
              self.lines += 1 

              while (col_count != col) :
                
                self.temp.next = Node(None, self.temp)
                self.temp = self.temp.next 
                self.cur[-1] = self.cur[-1] +1 
                self.col = self.cur[-1] 
                col_count = self.col
                
                return None  



        if (row == 0) and (col<self.cur[-1]):
            while (col_count != col):
                self.temp = self.temp.prev 
                self.cur[-1] = self.cur[-1]-1 
                self.col = self.cur[-1] 
                col_count = self.col
                
            return None 
        

        if (row < self.row) :
            while (row_count  != row) :
                self.doc2 = self.doc
                self.doc2 = self.doc.next 
                self.cur[0] = self.cur[0] -1
                self.row = self.cur[0]
                row_count = self.row 
            self.cur[-1] = -1 
            self.col = self.cur[-1]
            col_count = self.col       
            if (self.doc.data != None ) :
                self.doc2 = self.doc.data 
                self.cur[-1] =self.cur[-1] + 1 
                self.col = self.cur[-1]
                col_count = self.col

            while (col_count != col):
                if (self.doc2.next == None) :
                    self.doc2.next = Node(None,self.doc2)
                    self.doc2 = self.doc2.next 
                    self.cur[-1] =self.cur[-1] + 1 
                    self.col = self.cur[-1]
                    col_count = self.col

                else :
                    self.doc = self.doc.next 
                    self.cur[-1] =self.cur[-1] + 1 
                    self.col = self.cur[-1]
                    col_count = self.col
            return None 
















        if (col == 0):
          
              self.temp = Node(Node(None,self.temp)) 
              self.doc = self.temp
              self.cur[0] = self.cur[0] +1
              self.row = self.cur[0]
              row_count = self.row
              while (row_count != row) :
                self.temp.next = Node(Node(None,self.temp.next),self.temp)
                self.temp = self.temp.next
                self.cur[0] = self.cur[0] +1
                self.row = self.cur[0]
                row_count = self.row
                self.lines += 1 

              self.temp = self.temp.data 
              self.cur[-1] = self.cur[-1] +1 
              self.col = self.cur[-1] 
              col_count = self.col

              
              return None 



        


        if (row>0) :
              self.temp = Node(Node(None,self.temp))
              self.doc = self.temp
              self.cur[0] = self.cur[0] +1
              self.row = self.cur[0]
              row_count = self.row
              self.lines += 1 

              while (row_count != row) :
                self.temp.next = Node(Node(None,self.temp.next),self.temp)
                self.temp = self.temp.next
                self.cur[0] = self.cur[0] +1
                self.row = self.cur[0]
                row_count = self.row
                self.lines += 1 
              self.temp = self.temp.data 
              self.cur[-1] = self.cur[-1] +1 
              self.col = self.cur[-1] 
              col_count = self.col

              if (col > 0):
                while (col_count != col) :
                  
                  self.temp.next = Node(None, self.temp)
                  self.temp = self.temp.next 
                  self.cur[-1] = self.cur[-1] +1 
                  self.col = self.cur[-1] 
                  col_count = self.col
              
              
              return None 

       
        if (row<0) or (col<0):
          return 


        
        if (row > 0) and (col== None) :
              self.temp = Node(Node(None,self.temp))
              self.doc = self.temp
              self.cur[0] = self.cur[0] +1
              self.row = self.cur[0]
              row_count = self.row
              self.lines += 1 
              while (row_count != row) :
                self.temp.next = Node(Node(None,self.temp.next),self.temp)
                self.temp = self.temp.next
                self.cur[0] = self.cur[0] +1
                self.row = self.cur[0]
                row_count = self.row
                self.lines += 1 
                self.temp.data = None
        return None 

            
#======================

#======================
    def forward(self):
        '''
        Moves the cursor one step forward
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        t = TextEditor()
        if (self.temp.next == None):
            self.row += 1 
            t.goto(self.row , 0)
        else:
            self.temp = self.temp.next 
        return None 
        
        
#======================

#======================
    def back(self):
        '''
        Moves the cursor one step backwards
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        t=TextEditor()
        if (self.col == 0 ):
            self.row = self.row - 1
            while self.temp.next != None:
                t.goto(self.row , 0)
                self.col+= 1 
        else :
            self.temp = self.temp.prev 
        print (self.temp.data)

#======================

#======================
    def home(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        t=TextEditor()
        self.col = 0
        t.goto(self.row , self.col)
        return None 
#======================

#======================
    def end(self):
        '''
        Moves the cursor to the end of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        while(self.temp.next != None ):
            self.temp = self.temp.next 
        return None 

#======================

#======================
    def insert(self, string):
        '''
        Inserts the given string immediately after the cursor
 
        Parameters:
            a string
        
        Return value:
            None
        '''
        
        for char in string :
          if (self.temp.next == None):
            self.temp.next = Node(char , self.temp)
            self.temp = self.temp.next 
            self.material.append(char)
     
        

        return None 
#======================

#======================
    def delete(self, num):
        '''
        Deletes specified number of characters from the cursor position
 
        Parameters:
            integer number of characters to delete
        
        Return value:
            None
        '''
        
        for i in range(num) :
            self.temp.data = None 
            if self.temp.data in self.material:
                self.mateial.pop(self.temp.data)
            self.temp = self.temp.next 
        
        return None 


#======================

#======================
    def countCharacters(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            total number of characters in the document, basically
               the total number of pink nodes in the document.
        '''
        print (len(self.material))
        return (len(self.material))
#======================

#======================
    def countLines(self):
        '''
        Count total of non-empty lines in the document.
 
        Parameters:
            None
        
        Return value:
            integer number of non-empty lines in the document
        '''
        print (self.lines)
        return (self.lines)
#======================


#======================
    def printDoc(self):
        '''
        Prints the entire document on the screen.
        '''
        
        
        while (self.doc != None) :
            self.temp = self.doc 
            if self.doc.data != None :
                self.temp = self.doc.data
            while (self.temp != None ):
                print(self.temp.data)
                self.temp = self.temp.next 
            self.doc = self.doc.next 
        return None 
                

#======================

            
#======================
#======================
#    BONUS
#======================
    def undo(self):
        '''
        Undos the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def redo(self):
        '''
        Redos the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        with open(fileName , 'w') as f:
            for data in self.material :
                f.write(data)
                f.write('------->')
        return None 

            
        

#----------------------

    def load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError
            
#----------------------

    def find(self, substr):
        '''
        Finds a given substring within the entire document. If no such substring
          is found then return None.
 
        Parameters:
            substring to look for
        
        Return value:
            - reference to the first node of the substring found
            - None if substring is not found
        '''
#======================

#======================

    def quit (self):
        exit()
                


def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    editor = TextEditor()
    print("Welcome to DS Text Editor\n Enter commands at the prompt\n")
    while True:
        
        i=input()
        if i=="forward":
            editor.forward()
        if i=="back":
            editor.back()
        if i=="home":
            editor.home()
        if i=="end":
            editor.end()
        if i=="countCharacters":
            print(editor.countCharacters())
        if i=="countLines":
            print(editor.countLines())
        if i =="printDoc":
            editor.printDoc()
        if i=="quit":
            exit()
        else:
            try:
                l=i.split()
            except:
                print("Enter Valid Integer")
                next
            if l[0]=="goto":
                editor.goto(int(l[1]),int(l[2]))
            if l[0]=="insert":
                p=l[1:]
                editor.insert(p)
            if l[0]=="delete":
                editor.delete(int(l[1]))
                
    # while True:
    #     editor.Goto(0,0)
    #     editor.insert("Hello comp200")
    #     editor.printDoc()
    

if __name__ == '__main__':
    main()





