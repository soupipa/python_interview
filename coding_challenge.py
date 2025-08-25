log_data = """2023-11-21 08:30:15 [INFO] - User 'alice' logged in successfully.
2023-11-21 08:35:22 [WARNING] - Disk space is almost full.
2023-11-21 08:45:10 [ERROR] - Failed to connect to database server 'db-main'.
2023-11-21 09:05:00 [INFO] - New data processed from source 'source-A'.
2023-11-21 09:10:15 [ERROR] - Null pointer exception in module 'payment-processor'.
2023-11-21 09:15:30 [INFO] - User 'bob' logged in successfully.
2023-11-21 09:25:45 [DEBUG] - Cache cleared for user 'alice'.
2023-11-21 10:00:05 [ERROR] - Transaction failed for user 'charlie'.
2023-11-21 10:02:18 [WARNING] - High memory usage detected."""

def analyze_logs(x):
    
    log_level_counts = {}
    error_messages = []
    hourly_activity = {}

    lines = x.split("\n")
    for line in lines:
        parts = line.split(" ")

        
        time_part = parts[1]                
        hour = int(time_part.split(":")[0]) 

        
        log_level = parts[2][1:-1]        

       
        if log_level not in log_level_counts:
            log_level_counts[log_level] = 0
        log_level_counts[log_level] += 1

        
        if hour not in hourly_activity:
            hourly_activity[hour] = 0
        hourly_activity[hour] += 1

        
        if log_level == "ERROR":
            message = " ".join(parts[4:])   
            error_messages.append(message)

    
    busiest_hour = None
    max_count = 0
    for h in hourly_activity:
        if hourly_activity[h] > max_count:
            max_count = hourly_activity[h]
            busiest_hour = h

    return log_level_counts, error_messages, busiest_hour



counts, errors, busiest = analyze_logs(log_data)

print("Log Level Counts:")
print(counts)

print("\nError Messages:")
for msg in errors:
    print("-", msg)

print("\nHour with Most Activity:", busiest)