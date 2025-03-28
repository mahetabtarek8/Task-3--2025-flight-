#Mahetab Tarek Eid        section:6
# بيانات الرحلات الجوية
flights = [
    {"Flight ID": "A320", "Time": "10:30", "Altitude": 35000, "Speed": 500},
    {"Flight ID": "B737", "Time": "09:45", "Altitude": 30000, "Speed": 480},
    {"Flight ID": "C900", "Time": "11:15", "Altitude": 36000, "Speed": 510},
    {"Flight ID": "D450", "Time": "08:50", "Altitude": 28000, "Speed": 470},
]

# تحويل الوقت إلى دقائق ليسهل الفرز
def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

# تطبيق Quick Sort
def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if time_to_minutes(x[key]) < time_to_minutes(pivot[key])]
    middle = [x for x in arr if time_to_minutes(x[key]) == time_to_minutes(pivot[key])]
    right = [x for x in arr if time_to_minutes(x[key]) > time_to_minutes(pivot[key])]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# فرز الرحلات حسب وقت الوصول
sorted_flights = quick_sort(flights, "Time")

# طباعة النتيجة
for flight in sorted_flights:
    print(f"Flight {flight['Flight ID']} - Time: {flight['Time']} - Altitude: {flight['Altitude']} ft - Speed: {flight['Speed']} mph")