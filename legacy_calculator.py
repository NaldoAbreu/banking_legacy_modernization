import json

def calculate_legacy_interest(client_profile: dict, loan_amount: float, loan_term_months: int) -> float:
    """
    Simula o cálculo de juros de um sistema legado da década de 90.
    Este é um exemplo simplificado e não reflete a complexidade real de um sistema bancário real,
    mas serve para ilustrar o conceito de um sistema com lógica de negócio embutida e difícil de modificar.

    Regras de juros (simplificadas para o exemplo):
    - Clientes de risco 'A' (alto risco): 1.5% ao mês
    - Clientes de risco 'B' (médio risco): 1.0% ao mês
    - Clientes de risco 'C' (baixo risco): 0.75% ao mês
    - Juros compostos simples (para simplificar o exemplo de regressão).
    - Clientes com 'is_vip': True recebem 0.1% de desconto na taxa mensal.
    """
    risk_category = client_profile.get("risk_category", "B")
    is_vip = client_profile.get("is_vip", False)

    if risk_category == "A":
        monthly_rate = 0.015
    elif risk_category == "C":
        monthly_rate = 0.0075
    else:  # Default para 'B'
        monthly_rate = 0.010

    if is_vip:
        monthly_rate -= 0.001  # Desconto de 0.1%

    # Cálculo de juros compostos simples (para o exemplo)
    total_interest = loan_amount * ((1 + monthly_rate)**loan_term_months - 1)
    return round(total_interest, 2)


if __name__ == "__main__":
    # Exemplo de uso do calculador legado
    client1 = {"risk_category": "A", "client_id": "CLI001"}
    client2 = {"risk_category": "B", "client_id": "CLI002", "is_vip": True}
    client3 = {"risk_category": "C", "client_id": "CLI003"}

    loan1 = calculate_legacy_interest(client1, 1000.00, 12)
    loan2 = calculate_legacy_interest(client2, 5000.00, 24)
    loan3 = calculate_legacy_interest(client3, 2000.00, 6)

    print(f"Juros para CLI001 (Risco A): R$ {loan1:.2f}")
    print(f"Juros para CLI002 (Risco B, VIP): R$ {loan2:.2f}")
    print(f"Juros para CLI003 (Risco C): R$ {loan3:.2f}")
