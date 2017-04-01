'''Script to convert multiple images into a gif. Found out about imageio here:
http://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python'''
import glob
import sys

import imageio

DURATION = 1.5
OUT_GIF = 'out.gif'
VALID_EXTENSIONS = ('png', 'jpg')


def create_gif(filenames, duration=DURATION):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(OUT_GIF, images, duration=duration)


if __name__ == "__main__":

    script = sys.argv.pop(0)
    args = sys.argv

    if len(args) == 0:
        print('Usage: {} <glob pattern or list images>'.format(script))
        sys.exit(1)

    elif len(args) == 1:
        filenames = glob.glob(args[0])

    else:
        filenames = args

    if not all(f.lower().endswith(VALID_EXTENSIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    create_gif(filenames)
