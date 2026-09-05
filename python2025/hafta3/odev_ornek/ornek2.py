"""10.	Kullanıcı Adı Uzunluğu Kontrolü Kullanıcıdan bir kullanıcı adı oluşturmasını isteyin. Eğer kullanıcı adı 8 karakterden kısaysa "Kullanıcı adı çok kısa.", 12 karakterden uzunsa "Kullanıcı adı çok uzun.", bu aralıktaysa "Kullanıcı adı uygun." mesajı verin."""

kullanici_adi = input("Lütfen bir kullanıcı adı oluşturunuz: ")

uzunluk = len(kullanici_adi)
if uzunluk < 8:
    print("Kullanıcı adı çok kısa.")
elif uzunluk > 12:
    print("Kullanıcı adı çok uzun.")
else:
    print("Kullanıcı adı uygun.")
