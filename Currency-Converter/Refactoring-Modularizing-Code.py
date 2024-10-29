def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount')

def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD', 'RUPEE')
    while True:
        currency = input(f'{label} (USD/EUR/CAD/RUPEE): ').upper()
        if currency not in currencies:
            print('Invalid currency')
        else:
            return currency
        
def convert(amount, source_currency, target_currency):
    exchange_rates = {
        'USD': { 'EUR': 0.85, 'CAD': 1.25, 'RUPEE': 1.35},
        'EUR': {'USD': 1.18, 'CAD': 1.47, 'RUPEE': 1.60},
        'CAD': { 'USD':0.80, 'EUR': 0.60, 'RUPEE': 1.15},
        'RUPEE': { 'USD': 1.35, 'EUR':1.65, 'CAD': 1.12}
    }

    if source_currency == target_currency:
        return amount
    
    return amount * exchange_rates[source_currency][target_currency]

def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f}')


if __name__ == "__main__":
    main()
