ffmpeg -i lorentz_attractor.mp4 -r 10 output%05d.png
convert output*.png lorrentz_attractor.gif
rm output*.png
