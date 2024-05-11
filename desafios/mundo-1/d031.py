print('Uma companhia aérea vai fazer uma viagem de avião combrando passagens de R$0,50 por Km/h e R$0,45 para viagens acima de 200Km.')
d = int(input('Digite uma distância de uma viagem de avião em Km: '))
if d > 200:
    print(f'A passagem da viagem vai custar R${d * 0.45:.2f}')
else:
    print(f'A passagem da viagem vai custar R${d * 0.5:.2f}')