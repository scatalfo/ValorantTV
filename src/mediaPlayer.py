import pyglet
from pyglet import image
from pyglet.window import FPSDisplay
import glooey

pyglet.options['search_local_libs'] = True

print(pyglet.media.have_ffmpeg())
window= pyglet.window.Window(fullscreen=False, width = 1280, height = 720+64, file_drops=True, caption="ValorantTV")

fps_display = FPSDisplay(window)
player = pyglet.media.Player()
sameState = False


@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(0,64, height = 720, width = 1280)
        fps_display.draw()
        if(pauseToggle.is_checked and not player.playing):
            player.play()
        elif(not pauseToggle.is_checked and player.playing):
            player.pause()

    elif(gui.__contains__(hbox)):
        gui.remove(hbox)
        gui.add(label)

@window.event
def on_file_drop(x, y, path):
    filename = path[0]
    src = pyglet.media.load(filename, decoder = pyglet.media.codecs.ffmpeg.FFmpegDecoder())
    player.queue(src)
    player.play()
    player.pause()
    gui.remove(label)
    gui.add(hbox)

#GUI STUFF GOES HERE
class PauseButton(glooey.Checkbox):
    playImage = image.load('resources/play_64.png')
    pauseImage = image.load('resources/pause_64.png')
    custom_checked_base = pauseImage
    custom_checked_over = pauseImage
    custom_checked_down = pauseImage
    custom_unchecked_base = playImage
    custom_unchecked_over = playImage
    custom_unchecked_down = playImage
    custom_alignment = 'bottom left'

gui = glooey.Gui(window)
pauseToggle = PauseButton()
label = glooey.Label('Drop your video to get started!')
label.set_font_size(50)
label.set_color('white')
hbox = glooey.HBox()

gui.add(label)
hbox.add(pauseToggle)

#gui.add(hbox)
pyglet.app.run()