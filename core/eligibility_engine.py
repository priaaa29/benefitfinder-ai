def check_eligibility(user, scheme):

    if user["age"] < scheme["min_age"]:
        return False

    if user["age"] > scheme["max_age"]:
        return False

    if user["income"] > scheme["max_income"]:
        return False

    if scheme["gender"] != "any" and scheme["gender"] != user["gender"]:
        return False

    if scheme["state"] != "india" and scheme["state"] != user["state"]:
        return False

    return True