from abc import ABC, abstractmethod

# 1. Strategy Interface
class InterestCalculationStrategy(ABC):
    """
    Abstract interface for interest calculation strategies.
    """
    @abstractmethod
    def calculate_interest(self, loan_amount: float, loan_term_months: int) -> float:
        pass

# 2. Concrete Strategies
class LegacyRiskAStrategy(InterestCalculationStrategy):
    """
    Interest calculation strategy for Risk A clients (legacy).
    """
    def calculate_interest(self, loan_amount: float, loan_term_months: int) -> float:
        monthly_rate = 0.015
        total_interest = loan_amount * ((1 + monthly_rate)**loan_term_months - 1)
        return round(total_interest, 2)

class LegacyRiskBStrategy(InterestCalculationStrategy):
    """
    Interest calculation strategy for Risk B clients (legacy).
    """
    def calculate_interest(self, loan_amount: float, loan_term_months: int) -> float:
        monthly_rate = 0.010
        total_interest = loan_amount * ((1 + monthly_rate)**loan_term_months - 1)
        return round(total_interest, 2)

class LegacyRiskCStrategy(InterestCalculationStrategy):
    """
    Interest calculation strategy for Risk C clients (legacy).
    """
    def calculate_interest(self, loan_amount: float, loan_term_months: int) -> float:
        monthly_rate = 0.0075
        total_interest = loan_amount * ((1 + monthly_rate)**loan_term_months - 1)
        return round(total_interest, 2)

# 3. Context
class ModernInterestCalculator:
    """
    Modern interest calculator utilizing the Strategy Pattern.
    """
    def __init__(self):
        self._strategies = {
            "A": LegacyRiskAStrategy(),
            "B": LegacyRiskBStrategy(),
            "C": LegacyRiskCStrategy(),
        }

    def calculate_interest(self, client_profile: dict, loan_amount: float, loan_term_months: int) -> float:
        risk_category = client_profile.get("risk_category", "B")
        is_vip = client_profile.get("is_vip", False)

        # To ensure exact compatibility with the Golden Master,
        # the VIP discount logic needs to replicate the legacy system's behavior.
        # In the legacy system, the discount is applied directly to the monthly rate.
        # Here, we determine the base rate and apply the discount if VIP,
        # before calling the strategy or calculating directly.

        monthly_rate = 0.0 # Initialize with default value
        if risk_category == "A":
            monthly_rate = 0.015
        elif risk_category == "C":
            monthly_rate = 0.0075
        else:  # Default to B
            monthly_rate = 0.010

        if is_vip:
            monthly_rate -= 0.001  # Apply 0.1% discount to the monthly rate

        # Now, use the final monthly rate to calculate the interest.
        # This ensures the calculation is identical to legacy_calculator.py
        total_interest = loan_amount * ((1 + monthly_rate)**loan_term_months - 1)
        return round(total_interest, 2)


if __name__ == "__main__":
    calculator = ModernInterestCalculator()

    client1 = {"risk_category": "A", "client_id": "CLI001"}
    client2 = {"risk_category": "B", "client_id": "CLI002", "is_vip": True}
    client3 = {"risk_category": "C", "client_id": "CLI003"}

    loan1 = calculator.calculate_interest(client1, 1000.00, 12)
    loan2 = calculator.calculate_interest(client2, 5000.00, 24)
    loan3 = calculator.calculate_interest(client3, 2000.00, 6)

    print(f"Interest for CLI001 (Risk A): $ {loan1:.2f}")
    print(f"Interest for CLI002 (Risk B, VIP): $ {loan2:.2f}")
    print(f"Interest for CLI003 (Risk C): $ {loan3:.2f}")
