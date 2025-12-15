en_volume = int(input("Please enter EN Volume in mL: "))
dol = int(input("Please enter Day Of Life: "))

match (en_volume, dol):
    
    case (ev, d) if ev < 40 and d == 1:
        target_l = 6
        target_total = 71
        total_a = target_total - en_volume - target_l

    case (ev, d) if ev < 40 and d == 2:
        target_l = 12
        target_total = 92
        total_a = target_total - en_volume - target_l

    case (ev, d) if ev < 40 and d == 3:
        target_l = 18
        target_total = 113
        total_a = target_total - en_volume - target_l

    case (ev, d) if ev < 40 and d >= 4:
        target_l = 18
        target_total = 123
        total_a = target_total - en_volume - target_l

    case (ev, d) if 40 <= ev < 50 and d == 2:
        target_l = 12
        target_total = 112
        total_a = target_total - en_volume - target_l

    case (ev, d) if 40 <= ev < 50 and d >= 3:
        target_l = 18
        target_total = 153
        total_a = target_total - en_volume - target_l

    case (ev, d) if 50 <= ev < 60 and d == 2:
        target_l = 12
        target_total = 117
        total_a = target_total - en_volume - target_l

    case (ev, d) if 50 <= ev < 60 and d >= 3:
        target_l = 18
        target_total = 153
        total_a = target_total - en_volume - target_l

    case (ev, d) if 60 <= ev < 70 and d == 2:
        target_l = 12
        target_total = 122
        total_a = target_total - en_volume - target_l

    case (ev, d) if 60 <= ev < 70 and d >= 3:
        target_l = 12
        target_total = 152
        total_a = target_total - en_volume - target_l

    case (ev, d) if 70 <= ev < 80:
        target_l = 12
        target_total = 152
        total_a = target_total - en_volume - target_l

    case (ev, d) if 80 <= ev < 90:
        target_l = 12
        target_total = 152
        total_a = target_total - en_volume - target_l

    case (ev, d) if 90 <= ev < 100:
        target_l = 12
        target_total = 152
        total_a = target_total - en_volume - target_l

    case (ev, d) if 100 <= ev < 110:
        target_l = 12
        target_total = 152
        total_a = target_total - en_volume - target_l

    case (ev, d) if 110 <= ev < 120:
        target_l = 12
        target_total = 152
        total_a = target_total - en_volume - target_l

    case (ev, d) if ev >= 120:
        cspn_type = None  # prevents crashing later
        print("Stop SPN unless clinically indicated")

if en_volume < 120:
    print("Target Aqueous ", total_a)

