# Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleOfLinkedList(self, head):
        temp = head
        lenLL = 0
        while temp:
            lenLL += 1
            temp = temp.next
        
        lenLL = lenLL // 2
        # if lenLL % 2 == 0:
        #     lenLL = lenLL//2 + 1
        # else:
        #     lenLL = lenLL//2
        
        temp = head
        while lenLL:
            lenLL -= 1
            temp = temp.next
        
        return temp

# Definition for Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    mid = sol.middleOfLinkedList(head)

    print("Linked List:")
    printList(head)

    print("\nMiddle Node Value:", mid.val)
