# fast slow pointer / tortoise and hare pointer
# floyd's cycle detection algorithm
# tortoise pointer moves once , hare pointer moves twice per iteration, hare would lap tortoise

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_slow_p = head
        current_fast_p = head

        while current_fast_p and current_fast_p.next:
            current_slow_p = current_slow_p.next
            current_fast_p = current_fast_p.next.next

            if current_slow_p == current_fast_p:
                return True
        
        return False
#first attempt, window of 2 actually unnecessary, could always lap again etc
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_slow_p = head
        current_fast_p = head
        # while hare moving twice at a time the window of current tortoise & next of tortoise sufficient
        while current_fast_p and current_fast_p.next:
            next_next_fast_p = current_fast_p.next.next
            next_slow_p = current_slow_p.next

            if next_next_fast_p == current_slow_p:
                return True

            if next_next_fast_p == next_slow_p:
                return True
                
            current_fast_p = next_next_fast_p
            current_slow_p = next_slow_p
        return False