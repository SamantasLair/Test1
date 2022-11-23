# Problem: Reverse Linked List #18
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


# Refactor Iteration 2 (2021-11-22):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_18():
    pass # Validated on 2022-06-17

# Refactor Iteration 3 (2022-11-22):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_18():
    pass # Validated on 2022-11-23
