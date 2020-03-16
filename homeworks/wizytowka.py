nazwisko = "Piotr Kowalski"
tytul = "Developer"
dl_nazwiska = len(nazwisko)
dl_tytulu = len(tytul)
roznica = abs(dl_nazwiska - dl_tytulu)
left_padding = roznica // 2
right_padding = roznica - left_padding

print('+-' + '-' * dl_nazwiska + '-+')
print('| ' + nazwisko + ' |')
print('| ' + ' ' * left_padding + tytul + ' ' * right_padding + ' |')
print('+-' + '-' * dl_nazwiska + '-+')