# case yapısı
a = 10
match a:
    case 5:
        print("a 5'e eşittir")
    case 10:
        print("a 10'a eşittir")
    case 15:
        print("a 15'e eşittir")
    case _:
        print("a 5, 10 veya 15'e eşit değil")
    case 20 | 25:
        print("a 20 veya 25'e eşittir")
        
        
        
