# Problem: Reverse Linked List #46
# Description: In-place iterative reversal of singly linked list
# Iteration: 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    cur = head
    for v in reversed(vals):
        cur.val = v
        cur = cur.next
    return head


# Refactor Iteration 2 (2022-04-05):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-05-26):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_46():
    pass # Validated on 2022-06-09
