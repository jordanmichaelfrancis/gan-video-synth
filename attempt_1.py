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

# file format to dump output to
ext = '.mp4'

kwargs = {
    'bpm':bpm,
    'classes':classes, 
    'num_beats':num_beats,
    'ext':ext
}

generate_in_tempo(gvs, **kwargs)