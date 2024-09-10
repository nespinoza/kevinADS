import numpy as np
import utils

nsigma = 4.

overheads_factor = 1.2 # fraction of time expected to go on overheads
wave = 15.0
ref_FpFs = 861. # eclipse depth for GJ 486b
ref_dur = 0.6010 / 24. # really the transit duration
ref_mag = 10.296 # Ks mag

# For GJ 486 b:
print('\n\nGJ 486b \n -----')
RpRs = 0.0364759
dur = 1.083 / 24.
mag = 6.362
Tp = 706
Ts = 3291
aRs = 10.96

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
neclipse = utils.neclipses(SNR, wave, RpRs, Ts, aRs, nsigma = nsigma)

time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Need',time_needed,'hours --- ',neclipse,'eclipses for GJ 486 b.')

# For TOI-1452 b:
print('\n\nTOI-1452 b \n -----')
RpRs = 0.05574076
dur = 1.75877767131505 / 24. 
mag = 9.740
Tp = 390.
Ts = 3185
aRs = 47.6980418

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
neclipse = utils.neclipses(SNR, wave, RpRs, Ts, aRs, nsigma = nsigma)
time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Need',time_needed,'hours --- ',neclipse,'eclipses for TOI-1452 b.')

# For LHS 1140 b:
print('\n\nLHS 1140 b \n -----')
RpRs = 0.07390
dur = 2.15 / 24. 
mag = 8.821
Tp = 226
Ts = 3096
aRs = 95.3

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
neclipse = utils.neclipses(SNR, wave, RpRs, Ts, aRs, nsigma = nsigma)
time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Need',time_needed,'hours --- ',neclipse,'eclipses for LHS 1140 b.')

# For TRAPPIST-1b:
print('\n\n TRAPPIST-1b \n -----')
RpRs = 0.08590
dur = 0.6010 / 24.
mag = 10.296
Tp = 397.6
Ts = 2520
aRs = 20.843

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
neclipse = utils.neclipses(SNR, wave, RpRs, Ts, aRs, nsigma = nsigma)
time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Time per eclipse:',time_needed/neclipse)
print('Need',time_needed,'hours --- ',neclipse,'eclipses for TRAPPIST-1b.')
