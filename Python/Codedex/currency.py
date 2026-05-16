pesos = float(input("Enter the amount in pesos: "))
exchange_rate = 0.05  # Example exchange rate from pesos to dollars
dollars = pesos * exchange_rate
soles = float(input("Enter the amount in soles: "))
exchange_rate_soles = 0.25  # Example exchange rate from soles to dollars
dollars_from_soles = soles * exchange_rate_soles
reais = float(input("Enter the amount in reais: "))
exchange_rate_reais = 0.20  # Example exchange rate from reais to dollars
dollars_from_reais = reais * exchange_rate_reais
total_dollars = dollars + dollars_from_soles + dollars_from_reais
print("Total amount in dollars: ", total_dollars)