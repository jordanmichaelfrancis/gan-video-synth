from example import *
import numpy as np

gvs = GanVideoSynth()

### See full list of parameters in calls.py ###

# Tempo of the song in beats per minute.
bpm = 135

# Number of beats to generate an animation for.
num_beats = 16

# ImageNet class IDs to include in the y vector.
classes = [398, 402]

kwargs = {
    'bpm':bpm,
    'magnitudes':None,
    'funcs':None, 
    'axis_sets':None,
    'random_label':None, 
    'classes':classes, 
    'quantize_label':None,
    'y_scale':None, 
    'periods':None, 
    'num_beats':num_beats
    
}

generate_in_tempo(gvs, **kwargs)