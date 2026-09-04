#Check whether the temperature is within the safe range 18–35.
# def temperature_safe(temperature):
#     return 18 <= temperature <= 35

# print("Safe =", temperature_safe(32))

# Compare a user-entered password with the stored password.
# def password_match(entered, stored):
#     return entered == stored

# print("Password Match =", password_match("Python@123", "Python@123"))

# def package_accepted(weight):
#     return weight <= 25
# print("Accepted =", package_accepted(28))

# def score_compare(student1, student2):
#     return student1 > student2
# print("Student 1 scored higher =", score_compare(82, 76))

# def valid_pin(pinLength):
#     return pinLength == 4
# print("Valid PIN =", valid_pin(4))

# def login(usernameCorrect, passwordCorrect):
#     return usernameCorrect and passwordCorrect
# print("Login =", login(True, False))

# def scholarship(marks, attendance):
#     return marks >= 85 and attendance >= 75
# print("Eligible =", scholarship(90, 80))

# def emergency(temperature, smokeDetected):
#     return temperature > 45 or smokeDetected
# print("Alert =", emergency(30, True))

# def account_access(accountLocked):
#     return not accountLocked
# print("Access Allowed =", account_access(False))

# def free_shipping(premium, specialOffer):
#     return premium or specialOffer
# print("Free Shipping =", free_shipping(False, True))

# def game_health(health, damage):
#     health -= damage
#     return health
# print("Health =", game_health(100, 35))

# def restock(stock, newItems):
#     stock += newItems
#     return stock
# print("Stock =", restock(80, 25))

# def battery_reduce(battery, usage):
#     battery -= usage
#     return battery
# print("Battery =", battery_reduce(90, 15))

# def double_score(score):
#     score *= 2
#     return score
# print("Score =", double_score(250))

# def quantity_adjust(quantity):
#     quantity -= 3
#     return quantity
# print("Quantity =", quantity_adjust(10))

# def allowed_country(countries, country):
#     return country in countries
# countries = ["India", "Japan", "Germany", "Canada"]
# print("Available =", allowed_country(countries, "Japan"))

# def blocked_user(blocked, username):
#     return username in blocked
# blocked = ["admin", "root", "system"]
# print("Blocked =", blocked_user(blocked, "root"))

# def supported_file(supported, extension):
#     return extension in supported
# supported = ["jpg", "png", "webp"]
# print("Supported =", supported_file(supported, "pdf"))

# def ingredient_check(ingredients, item):
#     return item in ingredients
# ingredients = ["rice", "onion", "tomato", "salt"]
# print("Ingredient Found =", ingredient_check(ingredients, "tomato"))

# def forbidden_character(forbidden, password):
#     return any(ch in password for ch in forbidden)
# print("Forbidden Character Found =", forbidden_character("@#$", "hello#123"))

# def same_cart(cart1, cart2):
#     return cart1 is cart2
# cart1 = ["phone", "case"]
# cart2 = cart1
# print("Same Object =", same_cart(cart1, cart2))

# def same_object(list1, list2):
#     return list1 is list2
# list1 = [10, 20, 30]
# list2 = [10, 20, 30]
# print("Same Object =", same_object(list1, list2))


# def empty_check(result):
#     return result is None
# print("No Result =", empty_check(None))

# def has_permission(userPermission, requiredPermission):
#     return (userPermission & requiredPermission) == requiredPermission
# print("Has Permission =", has_permission(7, 4))

# def feature_toggle(settings, feature):
#     return settings ^ feature
# print("Updated Settings =", feature_toggle(5, 1))

# def common_permissions(user1, user2):
#     return user1 & user2
# print("Common Permissions =", common_permissions(13, 11))

# def enable_permissions(current, newPermission):
#     return current | newPermission
# print("Updated Permissions =", enable_permissions(5, 2))


# def binary_toggle(status, toggle):
#     return status ^ toggle
# print("Status =", binary_toggle(1, 1))

# def access_control(employee, intern, suspended, locations):
#     return (employee or intern) and not suspended and "office" in locations
# print("Access =", access_control(
# False, True, False, ["home", "office"]))


# def operation_allowed(role, locked, permissions, userBits, requiredBit):
#     return (
#         (role == "admin" or role == "manager")
#         and not locked
#         and "edit" in permissions
#         and (userBits & requiredBit) == requiredBit
#     )
# print("Operation Allowed =", operation_allowed(
#     "manager", False, ["view", "edit", "delete"], 7, 2))

# def notes_required(amount,notesrequired):
#     notes = [2000, 500, 200, 100, 50, 20, 10]
#     count = 0

#     for note in notes:
#         count += amount // note
#         amount %= note

#     return count

# amount = int(input("Enter amount: "))
# print("Number of notes:", notes required(amount))