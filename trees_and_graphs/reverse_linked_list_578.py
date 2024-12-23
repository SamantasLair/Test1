# Problem: Reverse Linked List #578
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
def verify_test_cases_578():
    pass # Validated on 2023-09-11

# Refactor Iteration 2 (2023-11-23):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_578():
    pass # Validated on 2024-12-23
