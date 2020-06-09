import packages.dbconfig

mydb = packages.dbconfig.db()

s = mydb.select("鬼滅之刃 16")

print(s)