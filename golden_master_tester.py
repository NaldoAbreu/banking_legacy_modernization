import json
from legacy_calculator import calculate_legacy_interest

def generate_golden_master_data(test_cases_file: str, output_file: str):
    """
    Gera os dados do 'Golden Master' executando o simulador do sistema legado
    com um conjunto de casos de teste e salvando os resultados.
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

    print(f"Dados do Golden Master gerados e salvos em {output_file}")

def run_regression_test(test_cases_file: str, golden_master_file: str, new_calculator_function):
    """
    Executa um teste de regressão comparando os resultados de uma nova função de cálculo
    com os dados do 'Golden Master'.
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
        print("Teste de Regressão PASSOU: Todos os resultados correspondem ao Golden Master.")
        return True
    else:
        print("Teste de Regressão FALHOU: Discrepâncias encontradas.")
        for failure in failures:
            print(f"  Caso de Teste ID {failure['test_case_id']}:")
            print(f"    Entrada: {failure['input']}")
            print(f"    Esperado: {failure['expected']}")
            print(f"    Atual: {failure['actual']}")
        return False


if __name__ == '__main__':
    # Este bloco será usado para gerar o Golden Master inicial
    # e rodar um teste de regressão contra o próprio sistema legado para validação.
    # Posteriormente, a função run_regression_test será usada com a nova implementação.

    test_cases_file = 'test_cases.json'
    golden_master_file = 'golden_master_data.json'

    print("\n--- Gerando Golden Master --- ")
    generate_golden_master_data(test_cases_file, golden_master_file)

    print("\n--- Validando Golden Master com o próprio sistema legado --- ")
    # Rodar o teste de regressão usando a função do sistema legado como a 'nova' função
    # Isso deve passar, pois estamos comparando o sistema consigo mesmo.
    run_regression_test(test_cases_file, golden_master_file, calculate_legacy_interest)
