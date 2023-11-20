import re
#FRET_REGEX = r"([A-G]|[E])([0-9]|\/)"
FRET_REGEX = r'([0-9]+|-|/)'


# Define the tuning of the guitar strings
tuning = ['E','A','D','G','B','E']
string_map = {t: i for i, t in enumerate(tuning)}

# Define a mapping of techniques and their codes
technique_map = {'/': 20, 'h': 21, 'p': 22, 'b': 23, 'r': 24}

# Function to encode a guitar tab
def encode_tab(tab):
    encoding = []
    lines = tab.strip().split('\n')
    doll = 0


    for beat in range(len(lines[0])):
        if doll == 1:
            doll = 0
            continue
        else:
            for string_num, line in enumerate(lines):
            # Use regular expression to find frets in each column/beat
              match = re.search(FRET_REGEX, line[beat:])
              if match:
                  note = match.group(1)
                  if note.isdigit():
                      fret = int(note)
                      if fret >= 10:
                          encoding.append(fret + (5 - string_num) * 100)
                          doll = 1
                      else:
                          encoding.append(fret + (5 - string_num) * 10)
                  else:
                    if note == "/":
                      encoding.append(technique_map[note])


    return encoding


# Ed Sheeran - Shape of You :) 
tab = """
E|--0---0-0-0------0---0---0------------------------------------------------------------------------------------------------------------------------------------------------------------------
B|-2-2-2-2-2-4-0-2--2-2-2-2-2-4-2-0----------------------------0-----------------------------------------------------0-0--------------0-------------------------------------------------------
G|-----------------------------------------------------------------1-1-1-1------------------------1-1-1-1-1-1-1-1-1-1---1---1----------1--------------------------------------1-------1------1
D|----------------------------------------------------------1-1-4-4--------4-4-4-4-4-4-2-2-2-4-2-2-----------------------4-2-4-2-2-2-2--4-4-4-4-4-4-4-4-2----------------------4-2-2-4-4-2-2-6
A|---------------------------------2-2-2-2-2-2-2-2-2-2-2-2-2------------------------------------4--------------------------------------------------------4---2-4-4-4-4-4-4-2-4------------4---
E|--------------------------------------------------------------------------------------------------------------------------------------------------------4-4---------------------------------
"""

# A part of the Seven Nation Army Tab :)
tab1 = """
E|--------------------------
B|--------------------------
G|--------------------------
D|--------------------------
A|-7--7--/10--7--5--3--2----
E|--------------------------
"""





# Reverse mapping for decoding
string_map_rev = {0: 'E', 1: 'B', 2: 'G', 3: 'D', 4: 'A', 5: 'E'}
technique_map_rev = {20: '/', 21: 'h', 22: 'p', 23: 'b', 24: 'r'}

# Function to decode an encoded guitar tab
def decode_tab(encoding):

  # Increase max_beats to represent longer tabs  
  max_beats = 32
  tab_matrix = [['-' for _ in range(max_beats)] for _ in range(6)]
  SPACE = 0
  beat = -1
  technique = 0
  placeholder = 0

  for code in encoding:
    beat += 1

    if code >= 100:
          fret = code % 100
          string_num = code // 100
    elif code == 20:
        technique = 1
        placeholder = 1
    else:
          fret = code % 10
          string_num = code // 10


    if technique == 1:
        technique = 0
    else:
        if placeholder == 1:
            tab_matrix[5 - string_num][beat] = '/' + str(fret)
            placeholder = 0
        else:
            tab_matrix[5 - string_num][beat] = str(fret)


  tab = ''
  reversed_tuning = tuning[::-1]
  for i, row in enumerate(tab_matrix):
    tab += reversed_tuning[i] + '|' + '|'.join(row) + '|\n'

  return tab


# Example decoding an encoded tab
print(encode_tab(tab1))
encoding = encode_tab(tab1)
print(decode_tab(encoding))
