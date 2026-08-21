# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        prev=None
        position = 1
        while position < left:
            prev = curr
            curr = curr.next
            position += 1
        left_prev=prev
        reverse_tail=curr
        prev=None#prev ni reset cheskuntunnam exact logic for reversing a liskind list 
        #left nide varaku traverse cheyadaniki pina unna code 
        #right-left+1==>example:-4-2+1=3(antey 3 nodes ni reverse cheyali ani thelusthundi)
        for _ in range(right-left+1):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        if left_prev:
            left_prev.next=prev
        else:head=prev
        reverse_tail.next=curr
        return head
    






    