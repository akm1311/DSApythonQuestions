def count_overlaps(time):
    hours, minutes = map(int, time.split(':'))
    total_minutes = hours * 60 + minutes
    overlap_interval = 720 / 11
    overlaps = 0
    current_overlap_time = 0
    
    while current_overlap_time <= total_minutes:
        overlaps += 1
        current_overlap_time += overlap_interval
    
    return overlaps - 1

time_input = input()
print(count_overlaps(time_input))
