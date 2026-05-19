from modern_interest_calculator import ModernInterestCalculator
from golden_master_tester import run_regression_test
import json

def calculate_with_modern_calculator(client_profile: dict, loan_amount: float, loan_term_months: int) -> float:
    calculator = ModernInterestCalculator()
    return calculator.calculate_interest(client_profile, loan_amount, loan_term_months)


if __name__ == "__main__":
    test_cases_file = "test_cases.json"
    golden_master_file = "golden_master_data.json"

    print("\n--- Running Regression Test with New Calculator (Strategy Pattern) --- ")
    # The run_regression_test function expects a function that simulates the calculation.
    # We pass our wrapper function that uses the ModernInterestCalculator.
    if run_regression_test(test_cases_file, golden_master_file, calculate_with_modern_calculator):
        print("\nCongratulations! The new implementation with Strategy Pattern is compatible with the legacy system.")
    else:
        print("\nATTENTION: The new implementation with Strategy Pattern is NOT compatible with the legacy system.")
