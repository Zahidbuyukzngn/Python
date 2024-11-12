import sys

values=[7,"Rigby",0,1,"Mordecai"]

for x in values:
    try:
        print("sayı: "+str(x))
        conclusion=1/int(x)
        print("sonuç= "+str(conclusion))

    except ValueError:
        print(str(x)+" bir sayı değil")
    # except ZeroDivisionError:
    #     print(str(x)+" sıfıra bölünemez")

    #sys modulünü import ederek aiağıdaki gibi hatayı belirlemek için kullanabilirim,sistem çökmeden düzenleme için kullanışlı
    except:
        print(str(x)+ " Hesaplanamadı")
        print("sistem diyor ki: "+str(sys.exc_info()[0]))
    
    #sqlitedemodaki gibi en son veritabanından çıkacağımızda close methodunu finally de kullanabiliriz
    finally:
        print("PROGRAM İS FİNİSHED")