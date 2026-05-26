usernames = ['admin', 'Paladin_of_Light', 'ArasakaNetrunner', 'DrUg_D3al3r', 'xXx_1738_xXx', 'GGK420']
for user in usernames:
    if user == 'admin':
        print("Hallo Kapitan! Mochtest du kartoffeln essen?")
    else:
        print(f"Hallo {user}, willkommen zurück!")

if usernames == []:
    print("USER LEVEL CRITCAL: We need recruits, stat!")
