from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    veiksmas = int(input("1 - peržiūrėti, 2 - įvesti pajamas, 3 - įvesti išlaidas, 4 - balansas, 0 - išeiti: "))
    match veiksmas:
        case 1:
            biudzetas.parodyti_irasus()
        case 2:
            biudzetas.ivesti_pajamas()
        case 3:
            biudzetas.ivesti_islaidas()
        case 4:
            biudzetas.parodyti_balansa()
        case 0:
            break