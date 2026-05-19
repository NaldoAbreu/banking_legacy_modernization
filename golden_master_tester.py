import json
from legacy_calculator import calculate_legacy_interest

def generate_golden_master_data(test_cases_file: str, output_file: str):
    """
    Generates the 'Golden Master' data by running the legacy system simulator
    with a set of test cases and saving the results.
    """
    with open(test_cases_file, 'r') as f:
        test_cases = json.load(f)

    golden_master_results = []
    for i, case in enumerate(test_cases):
        client_profile = case['client_profile']
        loan_amount = case['loan_amount']
        loan_term_months = case['loan_term_months']

        result = calculate_legacy_interest(client_profile, loan_amount, loan_term_months)
        golden_master_results.append({
            'test_case_id': i + 1,
            'input': case,
            'expected_output': result
        })

    with open(output_file, 'w') as f:
        json.dump(golden_master_results, f, indent=4)

    print(f"Golden Master data generated and saved in {output_file}")

def run_regression_test(test_cases_file: str, golden_master_file: str, new_calculator_function):
    """
    Runs a regression test by comparing the results of a new calculation function
    with the 'Golden Master' data.
    """
    with open(test_cases_file, 'r') as f:
        test_cases = json.load(f)

    with open(golden_master_file, 'r') as f:
        golden_master_data = json.load(f)

    failures = []
    for i, case in enumerate(test_cases):
        client_profile = case['client_profile']
        loan_amount = case['loan_amount']
        loan_term_months = case['loan_term_months']

        current_result = new_calculator_function(client_profile, loan_amount, loan_term_months)
        expected_result = golden_master_data[i]['expected_output']

        if current_result != expected_result:
            failures.append({
                'test_case_id': i + 1,
                'input': case,
                'expected': expected_result,
                'actual': current_result
            })

    if not failures:
        print("Regression Test PASSED: All results match the Golden Master.")
        return True
    else:
        print("Regression Test FAILED: Discrepancies found.")
        for failure in failures:
            print(f"  Test Case ID {failure['test_case_id']}:")
            print(f"    Input: {failure['input']}")
            print(f"    Expected: {failure['expected']}")
            print(f"    Actual: {failure['actual']}")
        return False


if __name__ == '__main__':
    # This block will be used to generate the initial Golden Master
    # and run a regression test against the legacy system itself for validation.
    # Later, the run_regression_test function will be used with the new implementation.

    test_cases_file = 'test_cases.json'
    golden_master_file = 'golden_master_data.json'

    print("\n--- Generating Golden Master --- ")
    generate_golden_master_data(test_cases_file, golden_master_file)

    print("\n--- Validating Golden Master with the legacy system itself --- ")
    # Run the regression test using the legacy system function as the 'new' function
    # This should pass, as we are comparing the system with itself.
    run_regression_test(test_cases_file, golden_master_file, calculate_legacy_interest)
