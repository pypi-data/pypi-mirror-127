# Install
You can use pip to install ascimage.

    pip install ascimage

# running

## on bash

    imprint <filename> [-s size-of-asciiart] [-z zoom x y]

examples)

If you want to output the image to the terminal, put it as follows:

    imprint hoge.jpg

If you want to shift the center position of the image by x = 80pixel, y = -20pixel and output up to W32xH28 characters at 4.6x magnification, enter as follows.

    imprint hoge.jpg -s 32 28 -z 4.6 80 -20

If you want to enlarge the image to the same size, set zoom = `0`.

## on python

    import ascimage
    
    ascimage.imprint(imgfile,[targetsizeWH],[zoomxy],[valrange])

- targetsizeWH: 
  - put `size-of-asciiart` as tuple.

- zoomxy:
  - put `zoom x y` as tuple.

-valrange:
  - `(vmin,vmax)`: `vmin` to `vmax` are expressed on a color scale.
