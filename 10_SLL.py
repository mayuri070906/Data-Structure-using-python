class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def create_node(self):
        data=int(input("Enter data::"))
        return Node(data)

    def insert_begin(self):
        newNode=self.create_node()
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        print("Inserted at begin!!")

    def insert_end(self):
        newNode=self.create_node()
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
        print("Inserted at end!!")
        
    def insert_location(self):
        newNode=self.create_node()
        if self.head is None:
            self.head=newNode
        loc=int(input("Enter location:"))
        if loc==1:
            newNode.next=self.head
            self.head=newNode
        else:
            temp=self.head
            for i in range(1,loc-1):
                if temp.next is None:
                    print("Invalid locaion")
                    return 
            temp=temp.next
        newNode.next=temp.next
        temp.next=newNode

    def Delete_begin(self):
        if self.head is None:
            print("list is empty!!!!")
        else:
            print("Deleted node:", self.head.data)
            self.head=self.head.next
            print("deleted from begining!!!!!")
    def Delete_end(self):
        if self.head is None:
            print("list is empty!!!!")
        elif self.head.next is None:
            print("Deleted node:",self.head.data)
            self.head=None
            print("deleted from end!!!")
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            print("Deleted node:",temp.next.data)
            temp.next=None
            print("Deleted from end!!!!")
    def Delete_location(self):
        if self.head is None:
            print("list is empty!!!!")
            return

        loc=int(input("Enter location:"))

        if loc==1:
            deleted = self.head.data
            self.head=self.head.next
            print("Deleted node:",deleted)
            return
        else:
            temp = self.head
            for i in range(1,loc-1):
                if temp is None:
                    print("invalid location")
                    return
                temp = temp.next
            if temp.next is None:
                print("invalid location")
                return
            print("Deleted node:",temp.next.data)
            temp.next=temp.next.next
    def display(self):
        temp=self.head
        if temp is None:
            print("list is Empty!!")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="->")
                temp=temp.next
            print("NULL")
if __name__=="__main__":
    obj=SinglyLinkedList()

    while True:
        print("\n1.beginInsert.\n2.endInsert.\n3.locationInsert.\n4.beginDelete.\n5.endDelete.\n6.locationDelete.\n7.display.\n8.Exit")
        choice=int(input("Enter your choice::"))
        match choice:
            case 1:
                obj.insert_begin()
            case 2:
                obj.insert_end()
            case 3:
                obj.insert_location()
            case 4:
                obj.Delete_begin()
            case 5:
                obj.Delete_end()
            case 6:
                obj.Delete_location()
            case 7:
                obj.display()
            case 8:
                print("Exit!!")
                break
            case _:
                print("Invalid choice!")
