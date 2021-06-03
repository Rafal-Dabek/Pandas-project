import pandas as pd

pilkarze = pd.read_csv('players_21.csv', sep=',')
p=pd.read_excel('fifa.xlsx')
del pilkarze['sofifa_id']
del pilkarze['player_url']
del pilkarze['long_name']
del pilkarze['dob']
del pilkarze['rb']
del pilkarze['rcb']
del pilkarze['cb']
del pilkarze['lcb']
del pilkarze['lb']
del pilkarze['rwb']
del pilkarze['rdm']
del pilkarze['cdm']
del pilkarze['ldm']
del pilkarze['lwb']
del pilkarze['rm']
del pilkarze['rcm']
del pilkarze['cm']
del pilkarze['lcm']
del pilkarze['lm']
del pilkarze['ram']
del pilkarze['cam']
del pilkarze['lam']
del pilkarze['rw']
del pilkarze['rf']
del pilkarze['cf']
del pilkarze['lf']
del pilkarze['lw']
del pilkarze['rs']
del pilkarze['ls']
del pilkarze['st']

del pilkarze['league_rank']
del pilkarze['real_face']
del pilkarze['loaned_from']
del pilkarze['defending_marking']
p2=pilkarze.loc[pilkarze['club_name']=="Manchester United"]
#print(pilkarze.)
#print(pilkarze.head())
#print(p.head())
pilkarze['value/overall']=pilkarze['value_eur']/pilkarze['overall']
print(pilkarze.loc[pilkarze['club_name']=="Juventus"].sort_values('wage_eur',ascending=False))


