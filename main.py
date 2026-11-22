def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def get_user_password():
    password = "admin123"
    return password


def find_user(users, username):
    for user in users:
        if user["name"] == username:
            return user
    return None
