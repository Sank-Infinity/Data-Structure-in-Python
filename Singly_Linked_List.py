# Fist of all create NODE class where we wind data and address of next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_Linked_List :
    try:
        def __init__(self):
            self.head = None

        def deleteNode(self):
            if self.head == None:
                print('Singly linked List is empty')
            else:
                ## here dynamic deletion takes place therefore we don,t need to do manually
                # temp = self.head
                self.head = self.head.next

        def insert_node(self,element):
            newNode = Node(element)
            if self.head==None:
                self.head = newNode
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = newNode

        def traverse(self):
            if self.head==None:
                print('Singly linked list is empty.')
            else:
                temp = self.head
                while temp != None:
                    print(temp.data, end=' ')
                    temp = temp.next
                print('\n')

        def insert_at_specific_position(self,data,index):
            newNode = Node(data)
            temp = self.head
            cnt = 0
            while temp!=None:
                temp=temp.next
                cnt+=1
            ## If linked list is empty then we insert an element at first position by default

            if self.head==None:
                self.head= newNode
            elif cnt>=index:
                cnt = 0
                temp = self.head
                prev = self.head
                while cnt!=index:
                    prev = temp
                    temp= temp.next
                    cnt+=1
                prev.next = newNode
                newNode.next = temp
            else:
                print('Index is out of range !!!')

        def delete_from_specific_position(self,index):
            temp = self.head
            cnt = 0
            while temp != None:
                temp = temp.next
                cnt += 1

            if self.head==None:
                print('Singly Linked List is empty !!!')

            elif self.head.next==None:
                ## linked list contains only one Node
                self.head == None

            elif cnt>=index:
                cnt = 0
                temp = self.head
                prev = self.head
                while cnt != index:
                    prev = temp
                    temp = temp.next
                    cnt += 1
                prev.next = temp.next
            else:
                print('Index is out of range !!!')

    except Exception as e:
        print('Something went wrong !!!')

if __name__ == '__main__':

    print('Welcome to Singly_linked_list !!!')
    game = True
    s = Singly_Linked_List()
    while game:
        print('1.Push \n2.Pop \n3.Traverse \n4.Insert at specific position \n5.Delete from specific position \n6.Exit ')
        try:
            operation = int(input('Enter Index which operation do you want to perform ?'))
        except Exception as e:
            print('Something went wrong !!!')

        if operation == 1:
            value = int(input('Enter an element: '))
            s.insert_node(value)

        if operation == 2:
            s.deleteNode()

        if operation == 3:
            s.traverse()

        if operation == 4:
            element = int(input('Enter an element: '))
            index = int(input('Enter an index: '))
            s.insert_at_specific_position(element, index)

        if operation == 5:
            index = int(input('Enter an index: '))
            s.delete_from_specific_position(index)

        if operation == 6:
            print('Session has successfully ended !!!')
            game = False
