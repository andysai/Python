import select_db
import random
import time

prizes = select_db.select_table()

prize = random.choice(prizes)
time.sleep(0.5)
print(prize)


