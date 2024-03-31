import os
import sys
import wget
import matplotlib.pyplot as plt

if not os.path.exists('thinkdsp.py'):
    wget.download('https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py')
sys.path.append('./')
import thinkdsp as dsp

wave = dsp.read_wave('comin-as-you-are.wav')

wave.plot()
plt.savefig("./img/full-wave.png", bbox_inches='tight')
plt.clf()

segment = wave.segment(start=2.75, duration=0.5)
segment.plot()
plt.savefig("./img/segment.png", bbox_inches='tight')
plt.clf()

spectrum = segment.make_spectrum()
spectrum.plot()
plt.savefig("./img/spectrum-full.png", bbox_inches='tight')
plt.clf()

spectrum.plot(high=800)
plt.savefig("./img/spectrum.png", bbox_inches='tight')
plt.clf()

print(spectrum.peaks()[:5])

low_pass = segment.make_spectrum()
low_pass.low_pass(1500)
low_pass.make_wave().play()

high_pass = segment.make_spectrum()
high_pass.high_pass(1500)
high_pass.make_wave().play()

band_stop = segment.make_spectrum()
band_stop.band_stop(500,1000)
band_stop.make_wave().play()

#1.3

from thinkdsp import CosSignal, SinSignal

mix = CosSignal(freq=100, amp=1.0, offset=0) + \
    SinSignal(freq=1000, amp=0.25, offset=0)
mix.plot()
plt.savefig("./img/mix-sig.png", bbox_inches='tight')
plt.clf()
mix.make_wave().play()

spectrum = mix.make_wave().make_spectrum()
spectrum.plot(high=1500)
plt.savefig("./img/mix-spec.png", bbox_inches='tight')
plt.clf()

mix += SinSignal(freq=333, amp=0.50, offset=0)
mix.make_wave().play()

#1.4

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave, 0.5)
wave.plot()
plt.savefig("./img/full-stretch.png", bbox_inches='tight')
plt.clf()

wave.play()

spec = wave.make_spectrum()
spec.plot(high=1600)
plt.savefig("./img/spec-stretch.png", bbox_inches='tight')
plt.clf()