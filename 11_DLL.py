class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def create_node(self):
        data = int(input("Enter data: "))
        return Node(data)

    def insert_begin(self):
        new_node=self.create_node()
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        print("Inserted at beginning")    
        
    def insert_end(self):
        new_node = self.create_node()
        if self.head is None:
            self.head=new_node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        print("Inserted at end")

    def insert_location(self):
        new_node = self.create_node()
        if self.head is None:
            self.head = new_node
            return
        loc=int(input("enter location:"))
        if loc==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            temp=self.head
            for i in range(1,loc-1):
                if temp.next is None:
                    print("Invalid location")
                    return
                temp=temp.next

            new_node.next=temp.next
            if temp.next:
                temp.next.prev=new_node
            new_node.prev=temp
            temp.next=new_node
        print(f"Inserted at location {loc}")
    def begin_Delete(self):
        if self.head is None:
            print("List is empty!!")
        else:
            print("Deleted node:", self.head.data)
            self.head=self.head.next
            if self.head:
                self.head.prev=None

    def end_Delete(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            print("Deleted node:",self.head.data)
            self.head=None
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            print("Deleted node:",temp.data)
            temp.prev.next=None

    def location_Delete(self):
        if self.head is None:
            print("List is empty!!")
            return  
        
        loc=int(input("Enter location:"))

        if loc==1:
            print("Deleted node:",self.head.data)
            self.head=self.head.next
            if self.head:
                self.head.prev = None
        else:
            temp=self.head
            for i in range(1,loc):
                if temp is None:
                    print("Invalid location!!")
                    return
                temp=temp.next
            if temp is None:
                print("Invalid location")
                return
            print("Deleted node:",temp.data)
            temp.prev.next=temp.next
            if temp.next:
                temp.next.prev=temp.prev
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("NULL")
mylist=DoublyLinkedList()
while True:
    print("\n1.beginInsert.\n2.endInsert.\n3.locationInsert.\n4.beginDelete.\n5.endDelete.\n6.locationDelete.\n7.display.\n8.Exit")
    try:
        choice=int(input("enter your choice number:"))
    except ValueError:
        print("Please enter a valid integer choice")
        continue
    match choice:
        case 1:
            mylist.insert_begin()
        case 2:
            mylist.insert_end()
        case 3:
            mylist.insert_location()
        case 4:
            mylist.begin_Delete()
        case 5:
            mylist.end_Delete()
        case 6:
            mylist.location_Delete()
        case 7:
            mylist.display()
        case 8:
            print("Exit!!")
            break
        case _:
            print("Invalid choice!")


