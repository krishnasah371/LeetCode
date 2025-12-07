class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        return_arr = []
        
        for i in range(len(intervals)):
            if not return_arr:
                return_arr.append(intervals[i])
            elif intervals[i][0] <= return_arr[-1][1]:
                return_arr[-1] = [return_arr[-1][0], max(intervals[i][1],return_arr[-1][1])]
            else:
                return_arr.append(intervals[i])

        return return_arr
            


        
        