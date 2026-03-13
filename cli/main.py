from core.scheme_loader import load_schemes
from core.eligibility_engine import check_eligibility

schemes = load_schemes()

user = {
    "age": int(input("Enter your age: ")),
    "income": int(input("Enter your family income: ")),
    "gender": input("Enter gender (male/female): "),
    "state": input("Enter state: ").lower()
}

eligible = []

for _, scheme in schemes.iterrows():

    if check_eligibility(user, scheme):
        eligible.append(scheme["scheme_name"])

print("\nYou qualify for:")

for s in eligible:
    print("-", s)