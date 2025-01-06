# move a ball from i -> j that's abs(i - j ) == 1
# want minimum i -> j movements
# calculating for every index

# brute force o n ^ 2
# [ i = sum( [ | afilledbox - i | for afilledbox in boxes]), ... ]

# dynamic programming

# prefix sum array o n = o n + o n + o n
# o n create a left ball move count
# o n create a right ball move count
# o n combine counts into single array


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        print('boxes', boxes)
        operations = [0] * len(boxes)
        left_moves , left_ball_count = [0] * len(boxes) , 0
        right_moves , right_ball_count = [0] * len(boxes) , 0


# have to save distances for each
        for b in range(1, len(boxes) ) :
            left_moves[b] += left_moves[b-1] + left_ball_count
            # print(left_moves[b-1], 'moves counted to the left', left_ball_count, 'balls counted to the left' )
            if boxes[b - 1] == '1':
                left_moves[b] += 1
                left_ball_count += 1
                # print('1 move , ball counted to the left')


        # start : last index : len(boxes) -1
        # stop : one index before first : - 1
        # step : -1 backwards
        # (start , stop , step )
        for b in range( len(boxes) -2, -1, -1 ):
            right_moves[b] += right_moves[b+1] + right_ball_count
            # print(right_moves[b+1], 'moves counted to the right', right_ball_count, 'balls counted to the left' )
            if boxes[b + 1] == '1':
                right_moves[b] += 1
                right_ball_count += 1
                # print('1 move , ball counted to the right')

        # remember not to do - 1 with range
        for b in range( len(operations) ) :
            operations[b] = left_moves[b] + right_moves[b] 
            # print(left_moves[b] + right_moves[b] , left_moves[b], right_moves[b])

        # print('left' , left_moves)
        # print('right', right_moves)

        return operations

        # move a ball from i -> j that's abs(i - j ) == 1
# want minimum i -> j movements
# calculating for every index

# brute force o n ^ 2
# [ i = sum( [ | afilledbox - i | for afilledbox in boxes]), ... ]

# dynamic programming

# prefix sum array o n = o n + o n + o n
# o n create a left ball move count
# o n create a right ball move count
# o n combine counts into single array


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        print('boxes', boxes)
        operations = [0] * len(boxes)
        left_moves , left_ball_count = [0] * len(boxes) , 0
        right_moves , right_ball_count = [0] * len(boxes) , 0


# have to save distances for each
        for b in range(1, len(boxes) ) :
            left_moves[b] += left_moves[b-1] + left_ball_count
            # print(left_moves[b-1], 'moves counted to the left', left_ball_count, 'balls counted to the left' )
            if boxes[b - 1] == '1':
                left_moves[b] += 1
                left_ball_count += 1
                # print('1 move , ball counted to the left')


        # start : last index : len(boxes) -1
        # stop : one index before first : - 1
        # step : -1 backwards
        # (start , stop , step )
        for b in range( len(boxes) -2, -1, -1 ):
            right_moves[b] += right_moves[b+1] + right_ball_count
            # print(right_moves[b+1], 'moves counted to the right', right_ball_count, 'balls counted to the left' )
            if boxes[b + 1] == '1':
                right_moves[b] += 1
                right_ball_count += 1
                # print('1 move , ball counted to the right')

        # remember not to do - 1 with range
        for b in range( len(operations) ) :
            operations[b] = left_moves[b] + right_moves[b] 
            # print(left_moves[b] + right_moves[b] , left_moves[b], right_moves[b])

        # print('left' , left_moves)
        # print('right', right_moves)

        return operations

        