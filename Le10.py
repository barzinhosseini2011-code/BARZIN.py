colors = ["red", "green", "blue", "yellow", "purple"]

for i in range(len(colors)):
    for j in range(i + 1, len(colors)):
        if colors[i] > colors[j]:
            colors[i], colors[j] = colors[j], colors[i]

print(colors)
#==================================================================
colors1 = ["red", "green", "blue", "yellow", "purple"]

colors1[0], colors1[-1] = colors1[-1], colors1[0]

print(colors1)