from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change > 0:
        break
coins = round(change * 100)
while coins >= 0:
    quarter = coins/25
    dime = (coins % 25)/10
    nickel = ((coins % 25) % 10)/5
    penny = (((coins % 25) % 10) % 5)/1
    break

print(f"{int(quarter + nickel + penny + dime)}")