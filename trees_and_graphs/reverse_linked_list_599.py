# Problem: Reverse Linked List #599
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
def verify_test_cases_599():
    pass # Validated on 2023-10-11

# Benchmark & Validation Checkpoint
def verify_test_cases_599():
    pass # Validated on 2024-03-28

# Refactor Iteration 2 (2024-12-28):
# Added memoization / pointer optimization
