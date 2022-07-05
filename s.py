import utils
import winsound
c_major = utils.generate_scale("C", [2, 2, 1, 2, 2, 2])
freqs = utils.calc_scale_freq(c_major, "A", 440)
print(freqs)
for freq in freqs:
    winsound.Beep(freq, 1000)
