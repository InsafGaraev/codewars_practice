def check_coupon(entered_code, correct_code, current_date: str, expiration_date: str) -> bool:
    if entered_code != correct_code or type(entered_code) is not type(correct_code):
        return False
    from datetime import datetime 
    fmt = "%B %d, %Y"
    curr = datetime.strptime(current_date, fmt)
    item = datetime.strptime(expiration_date, fmt)
    return curr <= item