class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort(key=lambda x: x[0])
        new_queries = queries.copy()
        new_queries.sort()
        result = [-1] * len(queries)
        result_map = {}
        q = 0

        def contains(interval, q):
            return interval[0] <= q <= interval[1]

        for interval in intervals:
            while q < len(new_queries) and new_queries[q] < interval[0]:
                q += 1

            if q >= len(new_queries):
                break

            if contains(interval, new_queries[q]):
                int_length = interval[1] - interval[0] + 1
                nq = q
                while nq < len(new_queries) and contains(interval, new_queries[nq]):
                    if new_queries[nq] not in result_map:
                        result_map[new_queries[nq]] = int_length
                    else:
                        result_map[new_queries[nq]] = min(result_map[new_queries[nq]], int_length)
                    nq += 1

        for i in range(len(queries)):
            if queries[i] in result_map:
                result[i] = result_map[queries[i]]

        return result
