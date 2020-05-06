class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        return self.queue.append(element)

    def dequeue(self):
        if len(self.queue)==0:
            return ('Queue is empty')
        return self.queue.pop(0)

    def specific_position(self,index,element):
        return (self.queue.insert(index, element))

    def remove_specific_position(self, index):
        if len(self.queue)==0:
            return ('Queue is empty')
        return (self.queue.pop(index))


if __name__ == '__main__':
    print('Welcome to Stack')
    game = True
    s = queue()
    while game:
        print('1.Enqueue \n2.Dequeue \n3.Traverse \n4.Insert at specific position \n5.Delete from specific position \n6.Exit')

        operation = int(input('Enter Index which operation do you want to perform ?'))

        if operation==1:
            element = int(input('Enter an element: '))
            s.enqueue(element)

        if operation==2:
            if len(s.queue)==0:
                print(s.dequeue())
            else:
                print('{} is dequeued successfully.'.format(s.dequeue()))

        if operation==3:
            print(s.queue)

        if operation==4:
            element = int(input('Enter an element: '))
            position = int(input('Enter an index: '))
            s.specific_position(position, element)

        if operation==5:
            position = int(input('Enter an index: '))
            if len(s.queue)==0:
                print('Queue is empty.')
            else:
                print('{} successfully deleted.'.format(s.remove_specific_position(position)))

        if operation==6:
            print('Session has ended successfully.')
            game = False
