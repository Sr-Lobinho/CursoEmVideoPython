times = ("Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "Internacional", "Bahia", "Cruzeiro","Atlético-MG", "Vasco", "Fluminense", "Criciúma", "Grêmio", "Red Bull Bragantino", "Juventude", "Vitória", "Corinthians", "Athletico-PR", "Cuiabá", "Atlético-GO")
print('-='*20)
print(f"Lista de times do Brasileirão: {times}")
print('-='*20)
print(f"Os 5 primeiros são: {times[:5]}")
print('-='*20)
print(f"Os 4 últimos são: {times[-4:]}")
print('-='*20)
print(f"Times em ordem alfabética: {sorted(times)}")
print('-='*20)
print(f"O Palmeiras está na {times.index("Palmeiras")+1}ª posição")
