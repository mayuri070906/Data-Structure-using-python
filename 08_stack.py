class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.size=int(input("Enter size of array:"))
    def push(self):
        if self.top==self.size-1:
            print("\n stack is full,overflow!!")
        else:
            value=int(input("\n enter value to be inserted::"))
            self.stack.append(value)
            self.top+=1
            print("Inserted!!!")
    def pop(self):
        if self.top==-1:
            print("stack is empty,overflow!!")
        else:
            print(f"\nDeleted element:{self.stack[self.top]}")
            self.stack.pop()
            self.top-=1

    def display(self):
        if self.top==-1:
            print("\n list is empty!!")
        else:
            print("stack element are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i],end=" ")
            print()

if __name__=="__main__":
    obj=Stack()
while True:
    print("\n1.push.\n2.pop.\n3.display.\n4.Exit.")
    choice=int(input("Enter your choice::"))
    match choice:
        case 1:
            obj.push()
        case 2:
            obj.pop()
        case 3:
            obj.display()
        case 4:
            print("Exit")
            break
        case _:
            print("Invalid choice!!")