## Implementation of Stack using linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def isempty(self):
        return (self.top==None)

    def push(self, data):
        if self.top == None:
            self.top = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.isempty():
            print('Stack is empty !!!')
        else:
            temp = self.top
            self.top = self.top.next
            print('{} has successfully poped.'.format(temp.data))

    def display(self):

        temp = self.top
        if self.isempty():
            print("Stack Underflow")

        else:

            while temp != None:
                print(temp.data, end="\n")
                temp = temp.next
            return


if __name__ == '__main__':
    if __name__ == '__main__':
        print('Welcome to Stack')
        game = True
        s = Stack()
        while game:
            print('1.Push \n2.Pop \n3.Traverse \n4.Exit ')
            operation = int(input('Enter Index which operation do you want to perform ?'))
            if operation == 1:
                ele = int(input('Enter an element: '))
                s.push(ele)
                print('{} is successfully pushed.'.format(ele))
            if operation == 2:
                s.pop()
            if operation == 3:
                s.display()
            if operation == 4:
                print('Session has Ended')
                game = False
