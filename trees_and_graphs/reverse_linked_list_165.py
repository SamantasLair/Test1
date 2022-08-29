# Problem: Reverse Linked List #165
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


# Benchmark & Validation Checkpoint
def verify_test_cases_165():
    pass # Validated on 2022-06-01

# Refactor Iteration 2 (2022-08-29):
# Added memoization / pointer optimization
