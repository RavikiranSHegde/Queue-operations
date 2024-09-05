class Queue:
    def __init__(self):
        self.q1 = []
        self.size = int(input("Enter the size of the queue: "))
        while True:
            print("\n1. Enqueue\t2. Dequeue\t3. Display\t4. Exit")
            choice = int(input("Enter a choice: "))
            if choice == 1:
                self.enqueue()
            elif choice == 2:
                self.dequeue()
            elif choice == 3:
                self.display()
            elif choice == 4:
                break
            else:
                print("Invalid choice")

    def enqueue(self):
        if len(self.q1) < self.size:
            data = eval(input("Enter data: "))
            self.q1.append(data)
            print("Data enqueued:", data)
        else:
            print("Queue is full")

    def dequeue(self):
        if len(self.q1) == 0:
            print("Queue is empty")
        else:
            data = self.q1.pop(0)
            print("Data dequeued:", data)

    def display(self):
        if len(self.q1) == 0:
            print("Queue is empty")
        else:
            print("Queue contents:", self.q1)


# Instantiate the queue
q = Queue()
