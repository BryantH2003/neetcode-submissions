class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []

        # Need to sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]
        
        # Loop through intervals to find if any start times overlap another start time
        for start2,end2 in intervals:
            
            # If end >= start2 --> overlap
            if end >= start2:
                end = max(end,end2)
            
            # start2 > end --> no overlap
                # Append prev interval to res 
                # Override new start and end values
            if start2 > end:
                res.append([start,end])
                start = start2
                end = end2
    
        res.append([start,end])

        return res
            
