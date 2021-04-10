## Bu dosyada fonksiyonların tanımı ve kullanımı anlatılmıştır. 
## Yorumlu kod satırlarını kullanarak kendiniz de inceleyebilirsiniz.

def factorial(n):
  result = 1 #Döndüreceğimiz sayı
  for num in range(n+1): #0'dan başlayarak n'e kadar olan sayılar
    if num == 0:
      result = 1 #0 ise 0! = 1 den dolayı 1 e eşitle
    else:
      result = result * num # 0'dan büyük ise sayının kendisi ile çarp
  return result #Sayıyı döndür

# Permütasyonun tanımı P(n, r) = n!/(n-r)!
def permutation(n, r):
  return factorial(n) // factorial(n-r) #Faktöriyel fonksiyonunu kullanarak permütasyon hesapla

def combination(n,r):
  return factorial(n) // (factorial(n-r) * factorial(r))
# Kombinasyon permütasyon kullanarak da hesaplanabilir yani: "return permutation(n, r) // factorial(r)" şeklinde de yazılabilir.
print(permutation(5,2))
print(combination(5,2))

#Bir sayının asal olup olmadığına o sayıdan küçük ve 1den büyük tüm sayıları bölerek kontrol edebiliriz.
def is_it_prime(n):
  for divider in range(2, n):
    if n % divider == 0:
      return False
  return True

def test_default_args(non_default_arg, default_arg = 'Already defined'):
  print(non_default_arg)
  print(default_arg)

# test_default_args("I'm positional", default_arg = 'Im default')

def our_append(item, L = []):
  L.append(item)

# our_append(12, test_list)

# '*args' yazarak verilen tüm argümanlara bir tuple içinden ulaşabiliriz.
# Böylece kaç tane argüman verildiğinin hiçbir önemi olmaz.
def our_print(*args):
  print(args)
  for item in args:
    print(item, end = ' ')
# our_print('Bunu', 'kendi', 'print', 'fonksiyonumuzu', 'kullanarak', 'yazdık')

# Default argümanlara '**kwargs ile bir dict içinden ulaşabiliriz.
def our_print_kw(**kwargs):
  print(kwargs)
  for k, v in kwargs.items():
    print(k, v)

# our_print_kw(first_item = 'asd', sec_item = 'bcd')
