import math 
def calculate_thirdedge(f_edge, s_edge, angl):
  costheorem = math.sqrt(f_edge**2 + s_edge**2 - 2 * f_edge * s_edge * math.cos(math.radians(angl)))
  return costheorem

first_edge = float(input("Üçgenin birinci kenarını giriniz: "))
second_edge = float(input("Üçgenin ikinci kenarını giriniz: "))
angle = float(input("İki kenar arasında kalan açıyı giriniz: "))


print(f"Üçüncü Kenar uzunluğu: {calculate_thirdedge(first_edge, second_edge, angle)}")