snatch = float(input("Enter snatch in kg: "))
#cleanAndJerk = input("Enter clean and jerk in kg: ")
#backSquat = input("Enter back squat max in kg: ")
#frontSquat = input("Enter front squat max in kg: ")
#OHS = input("Enter overhead squat max in kg: ")
#pushPress = input("Enter push press max in kg: ")

snatchWeights = [snatch*0.6, snatch*0.75, snatch*0.8, snatch*1]
snatchSetsReps = ["3x3", "3x3", "3x2", "3x1"]

rows = {}

for idx, weight in enumerate(snatchWeights):
    rows[idx+1] = [snatchSetsReps[idx], weight]

print("{:<8} {:<15} {:<10}".format('snatch', 'sets x reps', 'weight'))
for k, v in rows.items():
    setReps, weight = v
    print("{:<8} {:<15} {:<10}".format(k, setReps, "%.2f" % weight))

# print("\n It took me 58 minutes and 23 seconds to print the above table out")
