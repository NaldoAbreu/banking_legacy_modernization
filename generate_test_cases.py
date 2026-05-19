import json
import random

def generate_random_test_cases(num_cases: int = 100) -> list:
    test_cases = []
    risk_categories = ["A", "B", "C"]

    for i in range(num_cases):
        client_profile = {
            "risk_category": random.choice(risk_categories),
            "client_id": f"CLI{i+1:04d}",
            "is_vip": random.random() < 0.2 # 20% chance of being VIP
        }
        loan_amount = round(random.uniform(500.00, 10000.00), 2)
        loan_term_months = random.randint(3, 36)

        test_cases.append({
            "client_profile": client_profile,
            "loan_amount": loan_amount,
            "loan_term_months": loan_term_months
        })
    return test_cases


if __name__ == "__main__":
    # Generate 100 random test cases
    cases = generate_random_test_cases(100)

    # Save the test cases to a JSON file
    output_file = "test_cases.json"
    with open(output_file, "w") as f:
        json.dump(cases, f, indent=4)

    print(f"{len(cases)} test cases generated and saved in {output_file}")
