import json

def calculate_legacy_interest(client_profile: dict, loan_amount: float, loan_term_months: int) -> float:
    """
    Simulates the interest calculation of a legacy system from the 90s.
    This is a simplified example and does not reflect the real complexity of a banking system,
    but serves to illustrate the concept of a system with embedded business logic that is hard to modify.

    Interest rules (simplified for the example):
    - Risk 'A' clients (high risk): 1.5% per month
    - Risk 'B' clients (medium risk): 1.0% per month
    - Risk 'C' clients (low risk): 0.75% per month
    - Simple compound interest (to simplify the regression example).
    - Clients with 'is_vip': True receive a 0.1% discount on the monthly rate.
    """
    risk_category = client_profile.get("risk_category", "B")
    is_vip = client_profile.get("is_vip", False)

    if risk_category == "A":
        monthly_rate = 0.015
    elif risk_category == "C":
        monthly_rate = 0.0075
    else:  # Default to 'B'
        monthly_rate = 0.010

    if is_vip:
        monthly_rate -= 0.001  # 0.1% discount

    # Simple compound interest calculation (for example)
    total_interest = loan_amount * ((1 + monthly_rate)**loan_term_months - 1)
    return round(total_interest, 2)


if __name__ == "__main__":
    # Example of legacy calculator usage
    client1 = {"risk_category": "A", "client_id": "CLI001"}
    client2 = {"risk_category": "B", "client_id": "CLI002", "is_vip": True}
    client3 = {"risk_category": "C", "client_id": "CLI003"}

    loan1 = calculate_legacy_interest(client1, 1000.00, 12)
    loan2 = calculate_legacy_interest(client2, 5000.00, 24)
    loan3 = calculate_legacy_interest(client3, 2000.00, 6)

    print(f"Interest for CLI001 (Risk A): $ {loan1:.2f}")
    print(f"Interest for CLI002 (Risk B, VIP): $ {loan2:.2f}")
    print(f"Interest for CLI003 (Risk C): $ {loan3:.2f}")
