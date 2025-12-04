en_volume = int(input("Please enter EN Volume in mL: "))
dol = int(input("Please enter Day Of Life: "))
weight = float(input("Please enter weight in kg: "))

match (en_volume, dol):
    case (en_volume, dol) if en_volume < 40 and dol == 1:
        cspn_type = "cSPN1"
        print("Target Aqueous SPN : 65")
        print("Target Lipid SPN: 6")
        print("Target Total SPN: 71")

    case (en_volume, dol) if en_volume < 40 and dol == 2:
        cspn_type = "cSPN1"
        print("Target Aqueous SPN : 80")
        print("Target Lipid SPN: 12")
        print("Target Total SPN: 92")

    case (en_volume, dol) if en_volume < 40 and dol == 3:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 95")
        print("Target Lipid SPN: 18")
        print("Target Total SPN: 113")

    case (en_volume, dol) if en_volume < 40 and dol >= 4:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 105")
        print("Target Lipid SPN: 18")
        print("Target Total SPN: 123")

    case (en_volume, dol) if (40 <= en_volume < 50) and dol == 2:
        cspn_type = "cSPN1"
        print("Target Aqueous SPN : 60")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 112")

    case (en_volume, dol) if (40 <= en_volume < 50) and dol >= 3:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 95")
        print("Target Lipid SPN: 18")
        print("Target Total Fluid Volume: 153")

    case (en_volume, dol) if (50 <= en_volume < 60) and dol == 2:
        cspn_type = "cSPN1"
        print("Target Aqueous SPN : 55")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 117")

    case (en_volume, dol) if (50 <= en_volume < 60) and dol >= 3:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 85")
        print("Target Lipid SPN: 18")
        print("Target Total Fluid Volume: 153")

    case (en_volume, dol) if (60 <= en_volume < 70) and dol == 2:
        cspn_type = "cSPN1"
        print("Target Aqueous SPN : 50")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 122")

    case (en_volume, dol) if (60 <= en_volume < 70) and dol >= 3:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 80")
        print("Target Lipid SPN: 18")
        print("Target Total Fluid Volume: 152")

    case (en_volume, dol) if 70 >= en_volume < 80:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 70")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 152")

    case (en_volume, dol) if 80 >= en_volume < 90:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 60")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 152")

    case (en_volume, dol) if 90 >= en_volume < 100:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 50")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 152")

    case (en_volume, dol) if 100 >= en_volume < 110:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 40")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 152")

    case (en_volume, dol) if 110 >= en_volume < 120:
        cspn_type = "cSPN2"
        print("Target Aqueous SPN : 30")
        print("Target Lipid SPN: 12")
        print("Target Total Fluid Volume: 152")

    case( en_volume, dol) if 120 <= en_volume:
        print("Stop SPN unless clinically indicated")


