class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        return_arr = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= return_arr[-1][1] and return_arr[-1][1] <= intervals[i][1]:
                return_arr[-1] = [return_arr[-1][0], intervals[i][1]]
            elif intervals[i][0] <= return_arr[-1][1] and return_arr[-1][1] > intervals[i][1]:
                continue
            else:
                return_arr.append(intervals[i])

        return return_arr
            


        
        