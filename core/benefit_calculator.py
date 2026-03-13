def calculate_total_benefit(schemes):

    total = 0

    for scheme in schemes:
        total += scheme["benefit"]

    return total