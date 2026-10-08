password = input("Enter a password: ")
score = 0

if len(password) >= 8:
    score += 1
if len(password) >= 12:
    score += 1

has_lower = False
has_upper = False
has_digit = False
has_symbol = False

for char in password:
    if char.islower():
        has_lower = True
        elif char.isupper():
        has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True
if has_lower:
    score += 1
if has_upper:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

if score <= 2:
    rating = "Weak"
elif score <= 4:
    rating = "Medium"
else:
    rating = "Strong"

print(f"score: {score} out of 6")
print(f"Rating: {rating}")