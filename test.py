def atm():
    mojoudi = 10000000
    while True:
        gozine = int(input("gozineye morede nazar ra vared konid:"))
        print("1. mojoudi feeli")
        print("2. variz")
        print("3. bardasht")
        print("4. khorouj")
        if gozine == 1:
            print(mojoudi)
        elif gozine == 2:
            meghdare_varizi = int(input("mablaghe morede nazar jahate varizi ra vared konid:"))
            mojoudi += meghdare_varizi
            print("mablaghe morede nazar variz shod", mojoudi)
        elif gozine == 3:
            meghdar_bardasht = input("meghdare bardashti ra vared konid:")
            if meghdar_bardasht <= mojoudi:
                mojoudi -= meghdar_bardasht
                print("meghdare morede nazar az hesab bardasht shod.", mojoudi)
            else:
                print("mojoudi kaafi nemibashad.")
        elif gozine == 4:
            print("khoda negahdar")
            break

atm()