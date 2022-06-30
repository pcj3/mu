
NOTES = ["A", "A#", "B", "C","C#", "D","D#", "E", "F","F#", "G", "G#"]

def generate_scale(root_note, pattern):
    return

def 
def get_interval_note_up(root_note, interval):
    return NOTES[(NOTES.index(root_note) + interval) % 12]

def get_interval_note_down(root_note, interval):
    return NOTES[(NOTES.index(root_note) - interval) % 12]

def get_interval_up(root_note, target_note):
    interval = NOTES.index(target_note) - NOTES.index(root_note)
    return interval + 12 if interval < 0 else interval

def get_interval_down(root_note, target_note):
    interval = NOTES.index(target_note) - NOTES.index(root_note)
    return interval - 12 if interval > 0 else interval
