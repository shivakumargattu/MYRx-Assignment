""" 4. We are given two arrays that represent the arrival and departure times of trains, the task is to find the minimum number of platforms required so that no train waits. 
Examples: 
Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}, dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
Output: 3 """


def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()

    platform_needed = 0
    max_platforms = 0
    i, j = 0, 0

    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platform_needed += 1
            i += 1
        else:
            platform_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platform_needed)

    return max_platforms

arr = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
arr_times = [int(t.replace(":", "")) for t in arr]
dep_times = [int(t.replace(":", "")) for t in dep]
print(min_platforms(arr_times, dep_times))  # Output: 3
