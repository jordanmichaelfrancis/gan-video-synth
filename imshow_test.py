import os

import numpy as np
import cv2


FPS = 30
WAIT_TIME_MS = int(1000 / FPS)


def load():
    try:
        ims = np.load(os.path.join('npys', 'out.npy'))
        num_frames = ims.shape[0]
    except Exception as e:
        print(e)
        ims = np.zeros((1, 1, 1))
        num_frames = 1
    return ims, num_frames


def main():
    last_hash = None

    ims, num_frames = load()

    cur_frame = 0
    try:
        while True:
            if cur_frame >= num_frames:
                cur_frame = 0

                # Check if file has changed
                with open(os.path.join('npys', 'last_hash.txt'), 'r') as f:
                    cur_hash = f.readlines()

                # If the file has changed, then load the new one
                if cur_hash != last_hash:
                    last_hash = cur_hash
                    ims, num_frames = load()

            cv2.imshow('win', ims[cur_frame])
            cv2.waitKey(WAIT_TIME_MS)
            cur_frame += 1
    except KeyboardInterrupt:
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
