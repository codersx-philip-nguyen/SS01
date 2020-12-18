class Node:
    def __init__(self, data_value = None):
        self.data_value = data_value
        self.next_value = None
class SLinkedList:
    def __init__(self):
        self.head_value = None

    #Insert new node at the beginning
    def atBeginninng(self, new_data):
        NewNode = Node(new_data)
        NewNode.next_value = self.head_value
        self.head_value = NewNode
    #Insert new node at the end
    def atEnd(self, new_data):
        NewNode = Node(new_data)

        if(self.head_value is None):
            self.head_value = NewNode
            return
        last = self.head_value
        while(last.next_value):
            last = last.next_value
        last.next_value = NewNode

    #Insert at the middle
    def inBetween(self, middle_node, new_data):
        if(middle_node is None):
            return
        NewNode = Node(new_data)
        NewNode.next_value = middle_node.next_value
        middle_node.next_value = NewNode

    #print all the node in the linkedlist
    def printNode(self):
        print_value = self.head_value
        while print_value is not None:
            print(print_value.data_value)
            print_value = print_value.next_value

list = SLinkedList()
list.head_value = Node([1, 2, 3])
node_2 = Node([4, 5, 6])
node_3 = Node([7, 8, 9])

#link the nodes above
list.head_value.next_value = node_2
node_2.next_value = node_3

list.printNode()
