import pyglet
from pyglet.window import FPSDisplay
import glooey

pyglet.options['search_local_libs'] = True

print(pyglet.media.have_ffmpeg())
window= pyglet.window.Window(fullscreen=False, width = 1280, height = 720, file_drops=True, caption="ValorantTV")

fps_display = FPSDisplay(window)
player = pyglet.media.Player()
#filename = "resources/scarra.mp4"



@window.event
def on_draw():

    if player.source and player.source.video_format:
        player.get_texture().blit(0,0, height = 720, width = 1280)
        fps_display.draw()
    else:
        #print('hi')
        gui = glooey.Gui(window)
        label = glooey.Label('Drop your video to get started!')

        gui.add(label)

@window.event
def on_file_drop(x, y, path):    
    print(x, y, path)
    filename = path[0]
    src = pyglet.media.load(filename, decoder = pyglet.media.codecs.ffmpeg.FFmpegDecoder())
    player.queue(src)
    player.play()




pyglet.app.run()