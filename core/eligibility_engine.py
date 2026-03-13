def check_eligibility(user, scheme):

    reasons = []

    if user["age"] < scheme["min_age"]:
        reasons.append("Age below minimum")

    if user["age"] > scheme["max_age"]:
        reasons.append("Age above maximum")

    if user["income"] > scheme["max_income"]:
        reasons.append("Income exceeds limit")

    if scheme["gender"] != "any" and scheme["gender"] != user["gender"]:
        reasons.append("Gender requirement not satisfied")

    if scheme["state"] != "india" and scheme["state"] != user["state"]:
        reasons.append("State requirement not satisfied")

    if reasons:
        return False, reasons

    return True, ["All eligibility criteria satisfied"]