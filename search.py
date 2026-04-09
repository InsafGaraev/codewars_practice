def find_user(user_list, target_id):
    for item in user_list:
        if  item == target_id:
            return True
    return False
users = [101, 205, 308, 401, 502]
print(find_user(users, 308)) # Должно быть True
print(find_user(users, 999)) # Должно быть False