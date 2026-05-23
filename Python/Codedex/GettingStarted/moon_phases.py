def moon_phase(phase):
    phases = {
        "New Moon": "New Moon",
        "Waxing Crescent": "Waxing Crescent",
        "First Quarter": "First Quarter",
        "Waxing Gibbous": "Waxing Gibbous",
        "Full Moon": "Full Moon",
        "Waning Gibbous": "Waning Gibbous",
        "Last Quarter": "Last Quarter",
        "Waning Crescent": "Waning Crescent"
    }
    if phase == "New Moon":
        return "🌑"
    elif phase == "Waxing Crescent":
        return "🌒"
    elif phase == "First Quarter":  
        return "🌓"
    elif phase == "Waxing Gibbous":
        return "🌔"
    elif phase == "Full Moon":  
        return "🌕"
    elif phase == "Waning Gibbous":
        return "🌖"
    elif phase == "Last Quarter":
        return "🌗"
    elif phase == "Waning Crescent":
        return "🌘"
    return phases.get(phase, "Invalid phase")
# Example usage:
print(moon_phase("Full Moon"))  # Output: 🌕