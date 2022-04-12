import hashlib

def str_count(str):
  lst_hash = []
  for i in range(len(str)+1):
    for j in range(i + 1, len(str)+1):
      h = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
      lst_hash.append(h)

  return len(lst_hash)

str_1 = input('Введите слово: ').lower()
print(f'Количество подстрок в строке: {str_count(str_1)}')