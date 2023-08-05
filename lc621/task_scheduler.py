import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        hash_map = {}

        for task in tasks:
            hash_map[task] = hash_map.get(task, 0) - 1

        task_heap = [[value, key] for key, value in hash_map.items()]
        heapq.heapify(task_heap)
        queue = []
        count = 0

        while task_heap or queue:
            count += 1
            if queue:
                next = queue.pop(0)
                if next[1] == "0" and not task_heap:
                    continue
                if next[1] != "0":
                    heapq.heappush(task_heap, next)
            task = heapq.heappop(task_heap)
            task[0] += 1
            if task[0] != 0:
                while len(queue) < n:
                    queue.append([0, "0"])
                queue.append(task)

        return count
