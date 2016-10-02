import csv
# #
# with open("stat_sheet.file") as read_stats:
#     stats = read_stats.read()
#
# csw = stats
#
# for line in stats:
#     csw = csw.replace(" ", ",")
with open('stat_sheet.csv') as stats:
    stats = list(csv.DictReader(stats, fieldnames=["RANK", "LASTNAME", "FIRSTNAME", "FIGHTS",
                                                   "STR", "TSAC", "TD", "TDAC", "KD", "PASS", "REV", "SUB"]))


# print(stats)

#
# FIGHTS STR TSAC TD TDAC KD PASS REV SUB
