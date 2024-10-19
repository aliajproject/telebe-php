# 12 tələbənin məlumatlarını daxil edin
students_data = [
    ("Ali", 22, "Bakı Dövlət Universiteti", 91.50),
    ("Aysel", 21, "Azərbaycan Texniki Universiteti", 88.00),
    ("Rəşad", 23, "Xəzər Universiteti", 85.25),
    ("Elgün", 20, "Azərbaycan Dövlət İqtisad Universiteti", 92.10),
    ("Nigar", 22, "ADA Universiteti", 89.75),
    ("Kamran", 21, "Qafqaz Universiteti", 90.50),
    ("Leyla", 24, "Azərbaycan Tibb Universiteti", 95.00),
    ("Səməd", 22, "Naxçıvan Dövlət Universiteti", 87.40),
    ("Zaur", 23, "Gəncə Dövlət Universiteti", 84.30),
    ("Arif", 20, "Sumqayıt Dövlət Universiteti", 83.90),
    ("Gülşən", 21, "Bakı Ali Neft Məktəbi", 94.20),
    ("Elçin", 22, "Azərbaycan Memarlıq və İnşaat Universiteti", 86.80)
]

# Hər bir tələbəni çərçivə içində göstərən döngü
for students in students_data:
    print("+------------------------------------------+")
    print(f"| Ad: {students[0]:<35} |")
    print(f"| Yaş: {students[1]:<34} |")
    print(f"| Universitet: {students[2]:<28} |")
    print(f"| Bal: {students[3]:<34} |")
    print("+------------------------------------------+\n")
