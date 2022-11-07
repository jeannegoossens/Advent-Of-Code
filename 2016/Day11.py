import copy

# starting situation
# F4 .  .  .  .  .  .  .  .  .  .  .
# F3 .  .  .  .  .  .  .  PG PM RG RM
# F2 .  .  .  .  LM .  SM .  .  .  .
# F1 E  TG TM LG .  SG .  .  .  .  .

# rules:
# - E can take 2 things
# - E must take at least 1 thing
# - An M cannot be on the same floor as a different G without its own G present


spread = [['TG', 'TM', 'LG', 'SG'],
          ['LM', 'SM'],
          ['PG', 'PM', 'RG', 'RM'],
          []]
elevator = 0
