import requests

def convert_currency(amount, from_currency, to_currency):
    # Mock exchange rates (you can replace with real API calls like exchangerate-api.com or openexchangerates.org)
    exchange_rates = {
        "USD": {"INR": 83.2, "EUR": 0.92},
        "INR": {"USD": 0.012, "EUR": 0.011},
        "EUR": {"USD": 1.08, "INR": 90.0}
    }

    try:
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return round(converted_amount, 2)
    except KeyError:
        return "Conversion rate not available."

def main():
    print("Currency Converter")
    amount = float(input("Enter amount: "))
    from_currency = input("From Currency (e.g., USD, INR, EUR): ").upper()
    to_currency = input("To Currency (e.g., USD, INR, EUR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")

if __name__ == "__main__":
    main()
