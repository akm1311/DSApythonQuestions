# Read number of songs
N = int(input())

# Read the singers for each song
singers = list(map(int, input().split()))

# Dictionary to store the occurrences of each singer
occ = {}

# Count occurrences of each singer
for singer in singers:
    if singer in occ:
        occ[singer] += 1
    else:
        occ[singer] = 1

# Determine the maximum count of songs for any singer
max_count = max(occ.values())

# Count how many singers have this maximum count
favourite_singer_count = sum(1 for count in occ.values() if count == max_count)

print(favourite_singer_count)
