# LIFO for popping out when it ends
# saving the data - 
    # {id: time} o(1) lookup
    # (id, time) less memory
# only one function can be running at a time
# Function calls are nested, not concurrent - If a function starts while another is running, the first function is paused until the second function completes.
# ie ["0:start:0", "1:start:2", "0:end:5", "1:end:6"] impossible
# ["0:start:0", "1:start:2", "1:end:5", "0:end:6"] possible 


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def process_log(log):
            function_id, status, timestamp = log.split(":")
            return int(function_id), status, int(timestamp)

        stack = []
        function_time = [0] * n  # id associated with index for storage
        last_time = 0  # Last processed timestamp

        for log in logs:
            function_id, status, timestamp = process_log(log)

            if status == 'start':
                if stack:
                    # the last function was paused with this start, the time is added for up until the new function call
                    function_time[stack[-1]] += timestamp - last_time
                    print('added to function time' , stack[-1], function_time)
                stack.append(function_id)
                print('added to stck', stack, timestamp)
                last_time = timestamp
                

            elif status == 'end':
                # finished function will always be at the top of stack due ot nature of cpu architecture
                finished_function = stack.pop()
                print('finished function', finished_function)
                # Update its time (inclusive of the current timestamp)
                function_time[finished_function] += timestamp - last_time + 1
                print('timestamp', timestamp, 'last_time', last_time )
                # Update the last processed timestamp
                last_time = timestamp + 1
                print('new_last_time', timestamp + 1 )


        return function_time