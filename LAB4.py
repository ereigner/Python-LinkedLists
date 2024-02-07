# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> sub1, sub2 = x.split()
        >>> sub1
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
        >>> sub2
        Head:Node(5)
        Tail:Node(9.78)
        List:5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        newNode = Node(value)
        if self.isEmpty() == True:                      
            self.head = newNode
            self.tail = newNode
        elif newNode.value <= self.head.value:           # Checks if the value of newNode is less then or equal to the head value
            newNode.next = self.head                    
            self.head = newNode                         
        elif newNode.value >= self.tail.value:
            self.tail.next = newNode                    # points the tail value to newNode
            self.tail = newNode                         # Sets the tail as newNode
        else:
            current = self.head
            while current.next is not None and current.next.value <= newNode.value:
                current = current.next
            newNode.next = current.next                 # newNode points to current.next                     
            current.next = newNode                      # current points to newNode

            


    def split(self):
        subList1 = SortedLinkedList()
        subList2 = SortedLinkedList()
        if self.isEmpty() == True:
            return None
        if self.__len__() % 2 == 1:
            midpoint = self.__len__() // 2 + 1                          # If the length is odd you add the middle value to subList1
        if self.__len__() % 2 == 0:
            midpoint = self.__len__() // 2                              # If the length is even just split in half
        count = 0
        current = self.head
        while count < midpoint:                                        
            subList1.add(current.value)                                 # Runs the add function and adds it to subList1
            current = current.next
            count += 1
        while current is not None:                                      # Don't care about the midpoint anymore just run until the end
            subList2.add(current.value)  
            current = current.next
        return subList1, subList2

                
                
            

    def removeDuplicates(self):
        current = self.head
        while current.next is not None:
            if current.value != current.next.value:
                current = current.next                      # Moves to the next node
            else:
                current = current                           
                current.next = current.next.next            # Current will point to the node over the node next to current
                



if __name__ == '__main__':
        import doctest
        doctest.run_docstring_examples(SortedLinkedList, globals(), name='LAB4',verbose=True)