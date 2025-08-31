time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = time_str.split(",")

sum_minutes = 0

for time_value in time_list:
    chunk_all = time_value.split()
    for chunk in chunk_all:
        if 'h' in chunk:
            sum_minutes += int(chunk.replace('h','')) * 60
        elif 'm' in chunk:
            sum_minutes += int(chunk.replace('m',''))
        elif 's' in chunk:
            sum_minutes += int(chunk.replace('s','')) // 60
        else:
            print("An error occured during time value conversion!")
            

print('Minutes sum:', int(sum_minutes))