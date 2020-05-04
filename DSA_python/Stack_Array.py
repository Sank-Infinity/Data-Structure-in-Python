class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def insert(self, index, element):
        if index <= len(self.stack):
            self.stack.insert(index, element)
        else:
            print('Invalid index.')
    def pop(self):
        if len(self.stack) == 0:
            print('Stack is empty')
        return self.stack.pop()

    def pop_specific(self,index):
        if index<= len(self.stack):
            if len(self.stack) == 0:
                print('Stack is empty')
            return self.stack.pop(index)
        else:
            print('Invalid Index')


    def top(self):
        if len(self.stack)==0:
            print('Stack is empty')
        return self.stack[-1]

if __name__ == '__main__':
    print('Welcome to Stack')
    game = True
    s = Stack()
    while game:
        print('1.Push \n2.Pop \n3.Traverse \n4.Insert at specific position \n5.Delete from specific position \n6.Exit ')
        operation = int(input('Enter Index which operation do you want to perform ?'))
        if operation==1:
            ele = int(input('Enter an element: '))
            s.push(ele)
            print('Element is successfully pushed.')
        if operation==2:
            s.pop()
            print('Element is successfully popped.')
        if operation==3:
            print(s.stack)
        if operation==4:
            ele = int(input('Enter an element :'))
            position = int(input('Enter Index :'))
            s.insert(position,ele)
        if operation==5:
            position = int(input('Enter index:'))
            s.pop_specific(position)
        if operation==6:
            print('Session has Ended')
            game = False
