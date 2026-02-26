def quick_sort(arr):
    # Base case: Agar list khali hai ya 1 element hai, toh wo sorted hi hai
    if len(arr) <= 1:
        return arr
    
    # Ek 'pivot' element choose karte hain (beech ka element)
    pivot = arr[len(arr) // 2]
    
    # Teeno hisson mein divide karte hain:
    left = [x for x in arr if x < pivot]    # Pivot se chhote
    middle = [x for x in arr if x == pivot] # Pivot ke barabar
    right = [x for x in arr if x > pivot]   # Pivot se bade
    
    # Recursively sort karke sabko jod dete hain
    return quick_sort(left) + middle + quick_sort(right)

# Test karne ke liye
data = [38, 27, 43, 3, 9, 82, 10]
sorted_data = quick_sort(data)

print(f"Original: {data}")
print(f"Sorted:   {sorted_data}")
