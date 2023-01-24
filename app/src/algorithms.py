def calculate_rpp(hr, sbp):
    rpp = hr * sbp
    
    hp = None
    if rpp >= 30000:
        hp = "High"
    elif rpp >= 25000:
        hp = "High Intermediate"
    elif rpp >= 20000:
        hp = "Intermediate"
    elif rpp >= 15000:
        hp = "Low Intermediate"
    else:
        hp = "Low"

    return {
        "double-product": rpp,
        "hemodynamic-response": hp
    }