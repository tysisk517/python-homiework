# homework-1
def men_bmr(weight,height,age):
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

    return BMR

print(men_bmr(115, 185, 28))

def women_bmr(weight,height,age):
    BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return BMR

print(women_bmr(70, 154, 29))

# homework-2
def calculate_net_income(revenue, expenses):
    net_income = revenue - expenses

    return net_income

print(calculate_net_income(25000, 30000))

# homework-3
def calculate_cogs(binventory, purchases, einventory):
    cogs = binventory + purchases - einventory

    return cogs

print(calculate_cogs(2000, 3000, 1000))

# homework-4
def store_roi(gain, cost):
    roi = ((gain - cost) / cost) * 100

    return roi

print(store_roi(8000, 5000))

# homework-5
def rep_max(weight, reps):
    max = weight * (reps * 0.33 + 1)

    return max

print(rep_max(666, 6))
    