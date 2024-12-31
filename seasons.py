def find_season(A):
    
    if A < 1 or A > 12:
        return "Invalid"
    
    # Determine the season if 3 <= A <= 5:
        return "Spring"
    elif 6 <= A <= 8:
        return "Summer"
    elif 9 <= A <= 11:
        return "Autumn"
    else:  # December, January, February
        return "Winter"


print(find_season(6))   # Output: "Summer"
print(find_season(13))  # Output: "Invalid"
