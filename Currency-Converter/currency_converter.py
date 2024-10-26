# loop 
    # Ask the user for an amount
    # If invalid
    #   Print an error

# loop
    # Ask for the source currency
    # If invalid
    #   Print an error

# loop
    # Ask for the target currency
    # If invalid
    #   Print an error

# Do the conversion
# Print the result


while True:
    try:
        amount = float(input('Enter the amount: '))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print('Invalid amount')