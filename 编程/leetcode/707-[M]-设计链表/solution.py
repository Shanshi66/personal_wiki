from platform import node


class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.node_num = 0
        self.link = None

    def get(self, index: int) -> int:
        if self.node_num <= index:
            return -1
        i = 0
        p = self.link
        while i != index:
            p = p.next
            i += 1
        return p.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, next = self.link)
        self.link = node
        self.node_num += 1

    def addAtTail(self, val: int) -> None:
        if self.node_num == 0:
            self.addAtHead(val)
            return
        p = self.link
        node = Node(val)
        while p.next:
            p = p.next
        p.next = node
        self.node_num += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.node_num:
            return
        elif index <= 0:
            self.addAtHead(val)
        else:
            i = 0
            p = self.link
            while i != index-1:
                p = p.next
                i += 1
            node = Node(val, p.next)
            p.next = node
        self.node_num += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.node_num:
            return   
        elif index == 0:
            self.link = self.link.next
        else:
            i = 0
            p = self.link
            while i != index-1:
                p = p.next
                i += 1
            p.next = p.next.next
        self.node_num -= 1


if __name__ == '__main__':
    link_list = MyLinkedList()
    # link_list.addAtIndex(0, 10)
    link_list.addAtTail(1)
    link_list.get(0)