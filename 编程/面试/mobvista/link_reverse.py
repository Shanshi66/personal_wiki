class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse_link(link):
    if not link:
        return link
    p1 = link
    p2 = link.next
    p1.next = None # 注意顺序
    while p2:
        tmp = p2.next
        p2.next = p1
        p1 = p2
        p2 = tmp
    return p1


def create_link(nums):
    nodes = [Node(num) for num in nums]
    for i in range(len(nodes)):
        if i < len(nodes)-1:
            nodes[i].next = nodes[i+1]
    return nodes[0]

def print_link(link):
    p = link
    while p:
        print(p.val, end = '\t')
        p = p.next
    print()

if __name__ == '__main__':
    link = create_link([1,2,3,4,5])
    print_link(link)
    new_link = reverse_link(link)
    print_link(new_link)