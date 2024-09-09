import numpy as np
import utils

nsigma = 4.
overheads_factor = 1.2 # fraction of time expected to go on overheads
ADSref = 5.3 # 5.3 is what kevin said; it really should be (133 / (sqrt(2) * 14) = 6.7)?
wave = 15.0
ref_FpFs = 133. # eclipse depth for GJ 486b
ref_dur = 1.083 / 24. # really the transit duration
ref_mag = 6.362 # Ks mag

# For GJ 486 b:
RpRs = 0.0364759
dur = ref_dur 
mag = ref_mag
Tp = 706
Ts = 3291

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
ADS = SNR * ADSref
neclipse = ( nsigma / ADS )**2
time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Need',time_needed,'hours --- ',neclipse,'eclipses for GJ 486 b.')

# For TOI-1452 b:
RpRs = 0.05574076
dur = 1.75877767131505 / 24. 
mag = 9.740
Tp = 326
Ts = 3185

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
ADS = SNR * ADSref
neclipse = ( nsigma / ADS )**2
time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Need',time_needed,'hours --- ',neclipse,'eclipses for TOI-1452 b.')

# For LHS 1140 b:
RpRs = 0.07390
dur = 2.15 / 24. 
mag = 8.821
Tp = 226
Ts = 3096

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
ADS = SNR * ADSref
neclipse = ( nsigma / ADS )**2
time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Need',time_needed,'hours --- ',neclipse,'eclipses for LHS 1140 b.')

# For TRAPPIST-1b:
RpRs = 0.08590
dur = 0.6010 / 24.
mag = 10.296
Tp = 397.6
Ts = 2520

SNR = utils.eclipseSNR(RpRs, dur, mag, wave, Tp, Ts, ref_FpFs, ref_dur, ref_mag)
ADS = SNR * ADSref
neclipse = ( nsigma / ADS )**2
time_needed = (neclipse) * (dur*2*24. + 1.5) * overheads_factor

print('Need',time_needed,'hours --- ',neclipse,'eclipses for TRAPPIST-1b.')
