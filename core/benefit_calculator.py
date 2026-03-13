def calculate_total_benefit(eligible_schemes):

    total = 0

    for scheme in eligible_schemes:
        total += scheme["benefit"]

    return total