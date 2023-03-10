import numpy as np
import lightkurve as lk
import math
import trc_funcs as trc

# FIX THESE AND MAKE THEM REAL TESTS LATER

def pixels_to_radius_test():
    """
    Test the conversion of pixels to arcseconds. 
    """
    px = 20
    trc.roundup(px / np.sqrt(2) * 21 / 3600, pow=-2)
    assert trc.pixels_to_radius(20) == 0.9

def roundup_test():
    """
    Test roundup function works correctly. 
    """
    assert trc.roundup(40.11, pow=-1) == 40.2
    assert trc.roundup(40.11, pow=0) == 41.

def fit_bkg_test():
    """
    
    """
    bkg = trc.estimate_bkg(tpf_cutout, source_cat)
    # print(np.median(tpf_cutout[0].flux.value))
    # np.median(tpf_cutout.flux.value, axis=[1,2])

    # bkg = trc.estimate_bkg(tpf_cutout, source_cat)
    # print(np.shape(bkg))
    # plt.imshow(bkg[0])

    # b = bkg[:, np.newaxis, np.newaxis]
    # b[0,:,:]
    # # b, _ = np.broadcast_arrays(b, a)
    # # b
    assert True# that the shape of the bkg == shape of the input cut out
    assert True# that the median value of the bkg model and the image are within 10% of each other

def generate_basic_field_test():
    # test that the shape of the output field matches the input tpf_cutout
    # some index handling testing?
    # test a funky shape of cut out
    # some flux level testing?
    assert True

def flux_mag_converstion_test():
    assert(trc.mag_to_flux(12), trc.mag_to_flux(14))
    assert(trc.flux_to_mag(1.74e5), trc.flux_to_mag(27577))

