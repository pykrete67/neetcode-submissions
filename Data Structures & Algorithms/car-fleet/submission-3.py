class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # for easy traversal, we zip the list together
        pair = list(zip(position, speed))
        # we will go across the list in reverse order from the car with the furthest position first, from right to left, so we need to sort
        pair = sorted(pair)

        result = []

        for p, s in pair[::-1]:
            # the car will reach the car ahead only if time to destination is lesser than that car
            time_to_destination = (target-p)/s
            result.append(time_to_destination)
            if result and len(result) >= 2:
                # if time to destination is less than the car ahead, pop because it will join the car ahead at same speed
                if result[-2] >= result[-1]:
                    result.pop()
        
        return len(result)

# note: for example car 1,2,3. we might be wondering why dont we check whether car 1 and 2 collided first before car 3 because if car 1 collided with car 2, it will take the same speed as car 2 and go together. it car 1 will never collide with car 3


