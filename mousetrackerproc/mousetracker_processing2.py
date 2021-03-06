import pandas as pd
import os
#rootdir = 'C:/Users/Bryan/Desktop/MT_corrected'
rootdir = os.getcwd()

def self_chips(line):
    pid = ""
    answer = ""
    for i, char in enumerate(line):
        if i <= 6:
            pid = str(pid) + str(char)
        if i > 64 and i < 68:
            answer = answer + char
    return [pid, answer]

def oth_chips(line):
    pid = ""
    answer = ""
    for i, char in enumerate(line):
        if i <= 6:
            pid = str(pid) + str(char)
        if i > 74 and i < 78:
            answer = answer + char
    return answer
    
def all_participant_colors(rootdir):
    pid = []
    participant_colors = []
    partner_colors = []
    
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_name = open(rootdir + "/" + file)
        
            for i, line in enumerate(file_name):
                try:
                    if i > 4 and i < 75 and line[23] == 'Y':
                        pid.append(self_chips(line)[0])
                        participant_colors.append(self_chips(line)[1])
                except IndexError:
                    pass
                try:
                    if i > 4 and i < 75 and line[28] == 'P':  
                        partner_colors.append(oth_chips(line))
                except IndexError:
                    pass
            
            file_name.close()
    return zip(pid, participant_colors, partner_colors)


hopefully_this_works = all_participant_colors(rootdir)
hopefully_this_works = pd.DataFrame(hopefully_this_works)
hopefully_this_works.to_csv("answer.csv", index = False, header = False)

