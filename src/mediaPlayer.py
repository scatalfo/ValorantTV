import pyglet
from pyglet import image
from pyglet.window import FPSDisplay
import glooey

pyglet.options['search_local_libs'] = True #look for ffmpeg dlls

print(pyglet.media.have_ffmpeg()) #test if it worked
window= pyglet.window.Window(fullscreen=False, width = 1280, height = 720+64, file_drops=True, caption="ValorantTV") #create window
fps_display = FPSDisplay(window) #Add fps display (for debugging, may remove later)
player = pyglet.media.Player() #create the player object


@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(0,64, height = 720, width = 1280) #draw the texture from the video translate 64 pixels up to make room for GUI
        fps_display.draw() #draw the fps display
        #Pause logic
        if(pauseToggle.is_checked and not player.playing):
            player.play()
        elif(not pauseToggle.is_checked and player.playing):
            player.pause()
        #ScrollBar Logic
        scrollBar.set_fraction_filled(player.time/player.source.duration)
        #print(scrollBar.get_fraction_filled())

    elif(gui.__contains__(hbox)): #destroy the gui and readd the gui after video's done
        gui.remove(hbox)
        gui.add(label)

@window.event
def on_file_drop(x, y, path):
    filename = path[0] #set the filename of the mediaplayer to the first dropped media
    src = pyglet.media.load(filename, decoder = pyglet.media.codecs.ffmpeg.FFmpegDecoder()) #creates the source using ffmpeg
    player.queue(src)
    player.play()
    player.pause()   #queue up, play and then pause the media, so it starts on a paused state
    gui.remove(label)
    gui.add(hbox) #add the playing gui and remove the sample text

#GUI STUFF GOES HERE
class PauseButton(glooey.Checkbox):
    #using checkbox as a play button
    playImage = image.load('resources/play_64.png')
    pauseImage = image.load('resources/pause_64.png')
    custom_checked_base = pauseImage
    custom_checked_over = pauseImage
    custom_checked_down = pauseImage
    custom_unchecked_base = playImage
    custom_unchecked_over = playImage
    custom_unchecked_down = playImage
    custom_alignment = 'bottom left' 
class ScrollBar(glooey.FillBar): 
    custom_alignment = 'fill bottom'
    custom_padding = 0

    class Base(glooey.Background): 
        custom_left = pyglet.image.load('resources\\purple.png')
        custom_center = pyglet.image.load('resources\\grey.png')
        custom_right = pyglet.image.load('resources\\purple.png')

    class Fill(glooey.Background):
        custom_center = pyglet.image.load('resources\\green.png')
        custom_horz_padding = 4

gui = glooey.Gui(window) #create gui
pauseToggle = PauseButton() #make a new pause button
scrollBar = ScrollBar()
label = glooey.Label('Drop your video to get started!') 
label.set_font_size(50)
label.set_color('white')

#set up our label (instructions)
hbox = glooey.HBox()
gui.add(label)
hbox.pack(pauseToggle)
hbox.add(scrollBar)
#add our pausebutton to the hbox that we just made
#gui.add(hbox)
pyglet.app.run()