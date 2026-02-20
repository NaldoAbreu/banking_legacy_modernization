from modern_interest_calculator import ModernInterestCalculator
from golden_master_tester import run_regression_test
import json

def calculate_with_modern_calculator(client_profile: dict, loan_amount: float, loan_term_months: int) -> float:
    calculator = ModernInterestCalculator()
    return calculator.calculate_interest(client_profile, loan_amount, loan_term_months)


if __name__ == "__main__":
    test_cases_file = "test_cases.json"
    golden_master_file = "golden_master_data.json"

    print("\n--- Executando Teste de Regressão com a Nova Calculadora (Padrão Strategy) --- ")
    # A função run_regression_test espera uma função que simule o cálculo.
    # Passamos nossa função wrapper que usa a ModernInterestCalculator.
    if run_regression_test(test_cases_file, golden_master_file, calculate_with_modern_calculator):
        print("\nParabéns! A nova implementação com Padrão Strategy é compatível com o sistema legado.")
    else:
        print("\nATENÇÃO: A nova implementação com Padrão Strategy NÃO é compatível com o sistema legado.")
