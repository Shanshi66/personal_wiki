# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_link(head, left, right):
    if not head or left < 0 or left == right:
        return head
    p = head
    p_left = None
    i = 0
    while i < left-1 and p:
        p = p.next
        i += 1
    p_left = p

    p_pre = p_left.next if left > 0 else p_left
    if p_pre:
        p_post = p_pre.next
    else:
        return head

    i = 0
    while i < right-left and p_post: # 一定要双指针，单指针不行，因为指针内容一定会变
        tmp = p_post.next
        p_post.next = p_pre
        p_pre = p_post
        p_post = tmp
        i += 1
    
    if left == 0:
        p_left.next = p_post
        head = p_pre
    else:
        p_left.next.next = p_post
        p_left.next = p_pre
    return head

def create_link(nums):
    nodes = [ListNode(num) for num in nums]
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
    new_link = reverse_link(link, 1, 3)
    print_link(new_link)
