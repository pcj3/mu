NOTES = ["A", "A#", "B", "C","C#", "D","D#", "E", "F","F#", "G", "G#"]
MAJOR_CHORD_PATTERN = [0, 4, 7]
MINOR_CHORD_PATTERN = [0, 3, 7]

def generate_():
    pass

def generate_scale(root_note, pattern):
    scale = [root_note]
    for interval in pattern:
        scale.append(get_interval_note_up(scale[-1], interval))
    return scale

def generate_scale_triads(scale):
    return [generate_triad(note, scale) for note in scale]

def generate_triad(root_note, scale):
    return [scale[(scale.index(root_note) + scale_step) % len(scale)] for scale_step in [0, 2, 4]]

def get_pattern_from_scale(scale):
    return [get_interval_up(scale[i], scale[i+1]) for i in range(len(scale)-1)]

def generate_chord(root_note, intervals):
    return [get_interval_note_up(root_note, interval) for interval in intervals]

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

def calc_freq_multiplication(interval):
    return round(2 ** (interval/12), 2)

def calc_scale_freq(scale, given_note, given_note_freq):
    intervals = [get_interval_down(given_note, scale[i]) if i < scale.index(given_note) else get_interval_up(given_note, scale[i]) for i in range(len(scale))]
    return [int(given_note_freq * calc_freq_multiplication(interval)) for interval in intervals]

if __name__ == "__main__":
    c_major = generate_scale("C", [2, 2, 1, 2, 2, 2])
    d_blues = ["D", "F", "G", "G#", "A", "C"]
    blues_pattern = get_pattern_from_scale(d_blues)
    c_blues = generate_scale("C", blues_pattern)
    c_major_chord = generate_chord("C", MAJOR_CHORD_PATTERN)
    d_minor = generate_chord("D",  MINOR_CHORD_PATTERN)
    c_major_triads = generate_scale_triads(c_major)
    d_blues_triads = generate_scale_triads(d_blues)
