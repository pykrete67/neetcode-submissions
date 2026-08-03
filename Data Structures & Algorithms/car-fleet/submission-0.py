class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair = sorted(pair)

        result = []

        for p, s in pair[::-1]:
            time_to_destination = (target-p)/s
            result.append(time_to_destination)
            if result and len(result) >= 2:
                if result[-2] > result[-1]:
                    result.pop()

        return len(result) - 1


