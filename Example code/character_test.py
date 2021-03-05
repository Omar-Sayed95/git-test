from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()
'''
# Add some conversation for Dave when he is talked to
dave.set_conversation("Another head hangs lowly.")

# Trigger a conversation with Dave
dave.talk()
'''
dave.set_weakness("cheese") 
#dave.get_weakness() 

# Fight with dave
print("What will you fight with?") 
fight_with = input() 
dave.fight(fight_with) 
