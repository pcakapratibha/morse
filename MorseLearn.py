#  gcompris - morse code

import gtk
import gtk.gdk
import gcompris
import gcompris.utils
import gcompris.skin
import gcompris.anim
import gcompris.sound
import gcompris.bonus
import goocanvas
import pango
from string import ascii_uppercase
from MorseDes import *

from gcompris import gcompris_gettext as _

class Gcompris_watercycle:
  """morse code exercise"""

  def __init__(self, gcomprisBoard):
       
    self.gcomprisBoard = gcomprisBoard
    self.on = 0xFF0000FF
    self.off = 0X00000000L
    self.xaxis = 70
    self.xaxis1 = 100
    self.xaxis2 = 100
    self.yaxis = 300
    self.space = 130
    self.letter = "A"
    #Needed to get key_press
    gcomprisBoard.disable_im_context = True

  def start(self):
   
    # Set the buttons we want in the bar
    gcompris.bar_set(gcompris.BAR_LEVEL)

    # Set a background image
    gcompris.set_background(self.gcomprisBoard.canvas.get_root_item(),
                            "morse/morse.png")
    
    self.rootitem = goocanvas.Group(parent = self.gcomprisBoard.canvas.get_root_item())
    
    for i in ascii_uppercase:
      if i < "E":
        rect = MorseDes(self.rootitem,self.xaxis1,self.yaxis,100,True,False,"rectangle",self.on,self.off,"brown","black",i,"A")
        self.xaxis1 = self.xaxis1 + self.space

      if "E" < i and i <= "J":
        rect = MorseDes(self.rootitem,self.xaxis2,self.yaxis+70,100,True,False,"rectangle",self.on,self.off,"brown","black",i,"B")
        self.xaxis2 = self.xaxis2 + self.space
    self.w = gtk.Button ("Start Animation")
    self.rootitem.add_child(self.w)

    gcompris.bar_set(0)
    gcompris.bar_location(5,-1, 0.6)
    gcompris.bar_set_level(self.gcomprisBoard)
  
  def end(self):
    self.rootitem.remove()


  def ok(self):
    print("exercise ok.")
    

  def repeat(self):
    print("exercise repeat.")


  def config_stop(self):
    pass

  # Configuration function.
  def config_start(self, profile):
    print("exercise config_start.")

  def key_press(self, keyval, commit_str, preedit_str):
    utf8char = gtk.gdk.keyval_to_unicode(keyval)
    strn = u'%c' % utf8char

    print("Gcompris_exercise key press keyval=%i %s" % (keyval, strn))

  def pause(self, pause):
    print("morsecode pause. %i" % pause)


  def set_level(self, level):
    print("morsecode activity set level. %i" % level)

    
