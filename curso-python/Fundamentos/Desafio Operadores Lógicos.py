trabalho_terca = True
trabalho_quinta = True
# Tendo os dois trabalhos televisao de 50 inch + sorvete
# Se só um deles televisao de 32 inch + sorvete
# Se não tiver nenhum, não terá nada

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
nada = not sorvete
print('Tv50={} Tv32={} Sorvete={} Nada={}'
      .format(tv_50, tv_32, sorvete, nada))

# "{}, {} = {} ".format(1, False, 'Resultado' ) # '1, False = Resultado'
