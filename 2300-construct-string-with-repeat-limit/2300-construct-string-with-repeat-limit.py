from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        counts = Counter(s)
        heap = [(-ord(ch), ch, freq) for ch, freq in counts.items()]
        heapq.heapify(heap)
        #print(counts)
        #print(heap)

        result = []

        while heap:
            _, ch, freq = heapq.heappop(heap)
            use = min(freq, repeatLimit)
            result.append(ch*use)
            freq -= use
            if freq >0:
                if not heap:
                    break
                _, ch2, freq2 = heapq.heappop(heap)
                result.append(ch2)
                freq2 -= 1

                heapq.heappush(heap, (-ord(ch), ch, freq))
                if freq2 > 0:
                    
                    heapq.heappush(heap, (-ord(ch2), ch2, freq2))

        return "".join(result)
