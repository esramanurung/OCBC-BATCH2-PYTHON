# python dictionary
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

 # akses value
print(MLB_team['Minnesota']) 
MLB_team['Boston'] = 'Red Fox'
MLB_team['Boston'] = ['Red Fox', 'White Fox']
MLB_team['Boston'].append('Grey Fox')


print(MLB_team)
MLB_team(['Milwaukee'])
print(f"MLB team of Milwaukee {MLB_team['Milwaukee']}")

#Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
MLB_team['Kansas City'] = 'Royals'
print(f"MLB team of Kansas City {MLB_team['Kansas City']}")
print(MLB_team)

# If you want to update an entry, you can just assign a new value to an existing key:
MLB_team['Seattle'] = 'Seahawks'
MLB_team

# To delete an entry, use the del statement, specifying the key to delete:
del MLB_team['Seattle']
MLB_team