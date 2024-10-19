import mysql.connector

# MySQL ilə bağlantı yaradın
baglanti = mysql.connector.connect(
    host="localhost",    # MySQL serverinizin hostu
    user="root",         # MySQL istifadəçi adı
    password="root"     # MySQL şifrəniz
)

# Cursor yaradın
cursor = baglanti.cursor()

# Verilənlər bazasını yaradın və ya seçin
cursor.execute("CREATE DATABASE IF NOT EXISTS telebe_db")
cursor.execute("USE telebe_db")

# Telebeler cədvəlini yaradın
cursor.execute("""
    CREATE TABLE IF NOT EXISTS telebeler (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ad VARCHAR(100),
        yas INT,
        unversitet_adi VARCHAR(100),
        bal DECIMAL(5, 2)
    )
""")

# 12 tələbənin məlumatlarını daxil edin
telebeler_data = [
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

# Məlumatları cədvələ daxil edin
cursor.executemany("INSERT INTO telebeler (ad, yas, unversitet_adi, bal) VALUES (%s, %s, %s, %s)", telebeler_data)

# Dəyişiklikləri tətbiq edin
baglanti.commit()

# Telebeler cədvəlindən məlumatları çəkin
cursor.execute("SELECT ad, yas, unversitet_adi, bal FROM telebeler")

# Nəticələri əldə edin və ekranda göstərin
telebeler = cursor.fetchall()

# Hər bir tələbəni çərçivə içində göstərən döngü
for telebe in telebeler:
    print("+------------------------------------------+")
    print(f"| Ad: {telebe[0]:<35} |")
    print(f"| Yaş: {telebe[1]:<34} |")
    print(f"| Universitet: {telebe[2]:<28} |")
    print(f"| Bal: {telebe[3]:<34} |")
    print("+------------------------------------------+\n")

# Bağlantını bağlayın
cursor.close()
baglanti.close()
