from core.scheme_loader import load_schemes
from core.eligibility_engine import check_eligibility
from core.benefit_calculator import calculate_total_benefit

def get_user_profile():
    return {
        "age": int(input("Enter your age: ")),
        "income": int(input("Enter your family income: ")),
        "gender": input("Enter gender (male/female): ").lower(),
        "state": input("Enter state: ").lower()
    }


def find_eligible_schemes(user, schemes):

    eligible = []

    for _, scheme in schemes.iterrows():
        if check_eligibility(user, scheme):
            eligible.append(scheme)

    return eligible


def main():

    schemes = load_schemes()

    user = get_user_profile()

    eligible = find_eligible_schemes(user, schemes)

    print("\nEligible Schemes:\n")

    if not eligible:
        print("No schemes found.")
        return

    for scheme in eligible:
        print("-", scheme["scheme_name"])

total = calculate_total_benefit(eligible)

print("\nTotal potential benefits: ₹", total)

if __name__ == "__main__":
    main()