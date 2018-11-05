

def largest_hour_glass_sum(arr):
    """
    Arr is 6 x 6
    Each value [-9,9]
    """
    hour_glass_indices = [(0,0), (0,1), (0,2), (1,1), (2,0), (2,1), (2,2)]

    largest = -9*7 # lowest value of hour glass

    for i, value in enumerate(arr):
        if i + 2 == len(arr):
            break
        for j, value in enumerate(arr[i]):
            if j + 2 == len(arr[i]):
                break

            hour_glass = 0
            for index in hour_glass_indices:
                x,y = index[0]+i, index[1]+j
                hour_glass += arr[x][y]
            if hour_glass > largest:
                largest = hour_glass

    return largest
