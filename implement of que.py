queue=[]
def enqueue():
    element=int(input("Enter the element:"))
    queue.append(element)
    print(element,"is added to queue")

def dequeue():
    if not queue:
        print("the queue is empty")
    else:
        e=queue.pop(0)
        print("Poped element is",e)

def display():
    print(queue)


while True:
    print("Select the operation 1.Append 2.Pop 3.Display 4.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Select the correct choice")