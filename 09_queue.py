class Queue:
    def __init__(self):
        self.queue=[]
        self.front=-1
        self.rear=-1
        self.size=int(input("Enter size of the queue::"))
    def enqueue(self):
        if self.rear==self.size-1:
            print("\n queue is full,overflow!! ")
        else:
            value=int(input("Enter the value to be inserted::"))
            self.queue.append(value)
            self.rear+=1
            print("\nInserted")
            if self.front==-1:
                self.front=0
    def dequeue(self):
        if self.front==-1:
            print("\nqueue is empty,underflow")
        else:
            print(f"deleted element:{self.queue[self.front]}")
            self.front+=1
            if self.front>self.rear:
                self.front=self.rear=-1
                self.queue.clear()
    def display(self):
        if self.front==-1:
            print("\nqueue is empty!!")
        else:
            print("\n element of queue::")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()

if __name__=="__main__":
    obj=Queue()

    while True:
        print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                obj.enqueue()
            case 2:
                obj.dequeue()
            case 3:
                obj.display()
            case 4:
                print("Exit")
                break
            case _:
                print("Invalid choice")