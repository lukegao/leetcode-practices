
class Node(object):
    """docstring for Node"""

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self.next is not None:
            return f"{id(self)}: value={self.val}, next={id(self.next)}"
        else:
            return f"{id(self)}: value={self.val}, next=NULL"


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.head
        counter = 0

        while cur is not None:
            if index == counter:
                return cur.val
            cur = cur.next
            counter += 1

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        prev = None
        current = self.head
        node = Node(val)

        if current is None:
            return self.addAtHead(val)

        while current is not None:
            if current.next is None:
                current.next = node
                return
            current = current.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        if index == 0:
            return self.addAtHead(val)

        current = self.head
        prev = current
        counter = 0

        while current is not None:
            if counter == index:
                node.next = current
                prev.next = node
                return

            counter += 1
            prev = current
            current = current.next

        if index == counter:
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return
        if index == 0 and self.head is not None:
            self.head = self.head.next
            return

        counter = 0
        current = self.head
        prev = current
        while current is not None:
            if counter == index:
                prev.next = current.next
                return
            counter += 1
            prev = current
            current = current.next
        return

    def __repr__(self):
        current = self.head
        string = 'head'
        while current is not None:
            string += f"--> {current.val}"
            current = current.next
        string += '--> NULL'
        return string


if __name__ == '__main__':
    llist = MyLinkedList()
    llist.addAtIndex(0, 10)
    llist.addAtIndex(0, 20)
    llist.addAtIndex(1, 30)
    print(llist)
    print(llist.get(0))

    # llist.addAtHead(7)
    # llist.addAtHead(2)
    # llist.addAtHead(1)
    # llist.addAtIndex(3, 0)
    # llist.deleteAtIndex(2)
    # llist.addAtHead(6)
    # llist.addAtTail(4)
    # print(llist)
    # print(llist.get(4))
    # llist.addAtHead(4)
    # llist.addAtIndex(5, 0)
    # llist.addAtHead(6)
    # print(llist)
