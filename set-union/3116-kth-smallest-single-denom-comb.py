# k can be as large as 2 * 10 ** 9 -- needs constant or logarithmic
# steps
    # union set lists of combinations
    # binary search on the list
class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)

        def count(num: int) -> int:
            ''' 
            :param num: value testing number of combinations ==
            inclusion exclusion principle
            '''
            valid_combinations, include = 0, True
            for i in range(1, n + 1): # combination sizes
                multiples_count = 0
                for comb in itertools.combinations(coins, r=i):
                    # print(comb)
                    # print(math.lcm(*comb))
                    multiples_count += num // math.lcm(*comb) # how many numbers up to num are divisible by the LCM of each combination of coins
                # inclusion exclusion principle
                # avoid overcounting number of valid combinations
                valid_combinations = valid_combinations + multiples_count if include else valid_combinations - multiples_count
                include = not include

            return valid_combinations

        # only need to do this count() o log (low * k) times
        low = min(coins)
        high = low * k # worst case is minimum k times
        while low <= high:
            mid = (low + high) // 2
            mid_combinations = count(mid)
            if mid_combinations < k:
                low = mid + 1
            else:
                high = mid - 1

        return low
    
# use a min heap to track smallest
# misunderstood the problem not doing cross coin combinations!!
# also complexity issue
import heapq
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        sorted_coins = sorted(coins)
        coin_p = [1] * n
        min_heap = list()
        seen = set(coins)

        for i in coins:
            heapq.heappush(min_heap, i)
        # want to do every combination of coins
        # starting with smallest for incrementing
        # keep doing until get k in the heap
        multiples = 1
        while len(min_heap) < 3 * k :
            for i, coin in enumerate(sorted_coins):
                to_pair = sorted_coins[i:]
                for new_coin in to_pair:
                    val = coin + new_coin * multiples
                    if val not in seen:
                        heapq.heappush(min_heap, val)
                    seen.add(val)
            multiples += 1
        for i in range(k):
            result = heapq.heappop(min_heap)
        return result
