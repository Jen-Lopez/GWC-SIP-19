
# What is the most profitable broadway show in NYC
# what is the most profitable, by theatre

import broadway
import matplotlib.pyplot as plot
import numpy as np

broadway =  broadway.get_shows()

# Year, name,gross, attendance
theaters = []
theater_dict = {}
filtered_broadway = []

# filter out data and extract theaters
for show in broadway:
    if show['Date']['Year'] < 2000:
        continue
    if show['Statistics']['Performances'] == 0:
        continue
    if show['Statistics']['Gross'] == 0:
        continue
    if show['Statistics']['Attendance'] == 0:
        continue

    t = show['Show']['Theatre']
    if t not in theaters:
        theaters.append(t)
    filtered_broadway.append(show)

# create dictionary with theaters as key
for theater in theaters:
    theater_dict[theater] = {}

# add shows and if the show is already there, just update profit and attendance values
for s in filtered_broadway:
    showinfo = {}

    theater = s['Show']['Theatre']
    show = s['Show']['Name']
    attendance = s['Statistics']['Attendance']
    profit = s['Statistics']['Gross']
    year = s['Date']['Year']


    showinfo['year'] = year
    showinfo['profit'] = profit
    showinfo['attendance'] = attendance


    if (show not in theater_dict[theater]):
        theater_dict[theater][show] = showinfo
    else:
        theater_dict[theater][show]['profit'] += profit
        theater_dict[theater][show]['attendance'] += attendance

# iterates throught each
for theater in theater_dict:
    movie_set = {}
    info_set= {}
    info = theater_dict[theater]
    curr_top = ''
    curr_prof = 0

    for show in info:
        if info[show]['profit'] > curr_prof:
            curr_top = show
            curr_prof = info[show]['profit']
    movie_set[curr_top] = curr_prof
    info_set[theater] = movie_set
    most_profitable.append(info_set)

theater_show_label = []
profit = []

print("The most profitable shows per Theatre:\n")
for line in most_profitable:
    for key in line:
        thing = list(line[key])
        print ('Theatre:',key,'| Show:', thing[0],'| Revenue:' ,'$'+'{:,}'.format(line[key][thing[0]]),'\n')
        theater_show_label.append(key + ' - ' + thing[0])
        profit.append((line[key][thing[0]])/10**6) # convert it to per million

# Horizontal Bar Graph
y_font = {'size'   : 6}
y_pos = np.arange(len(theater_show_label))
plot.figure(figsize=(10,7))

plot.barh(y_pos,profit)
plot.yticks(y_pos, theater_show_label)

plot.ylabel('Theatre-Show')
plot.xlabel('Revenue (in millions)')
plot.title('Most Profitable Broadway Shows in NYC (2000-2016)', y = 1.05)
plot.yticks(y_pos,theater_show_label,**y_font)
plot.tight_layout()
plot.show()
