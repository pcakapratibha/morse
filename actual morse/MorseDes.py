#  description of morse

import gtk
import gtk.gdk
import gcompris
import gcompris.utils
import gcompris.skin
import goocanvas
import pango
import string

# dot = 0,dash = 1

class MorseDes:
  """morse charater description"""
  def __init__(self, rootitem,x,y,width,clickable,display,typef,on,off,fill_color,stroke_color,letter,Morse_L = "letter"):
    self.clickable = clickable
    self.display_letter = letter
    self.typef = typef
    self.display = display
    self.fill_color = fill_color
    self.stroke_color = stroke_color
    self.width = width
    self.rootitem = goocanvas.Group(parent = rootitem)
    self.letter = letter
#letters of morse
    Morse_L = {
      "A": [0, 1],
      "B": [1, 0, 0, 0],
      "C": [1, 0, 1, 0], 
      "D": [1, 0, 0], 
      "E": [0],
      "F": [0, 0, 1, 0], 
      "G": [1, 1, 0], 
      "H": [0, 0, 0, 0], 
      "I": [0, 0],
      "J": [0, 1, 1, 1], 
      #" ": [ ],	
      #"K": [1, 0, 1], 
      #"L": [0, 1, 0, 0], 
      #"M": [1, 1],
      #"N": [1, 0], 
      #"O": [1, 1, 1], 
      #"P": [0, 1, 1, 0], 
      #"Q": [1, 1, 0, 1],
      #"R": [0, 1, 0], 
      #"S": [0, 0, 0], 
      #"T": [1], 
      #"U": [0, 0, 1],
      #"V": [0, 0, 0, 1], 
      #"W": [0, 1, 1], 
      #"X": [1, 0, 0, 1], 
      #"Y": [1, 0, 1, 1],
      #"Z": [1, 1, 0, 0] 
      #1: [0, 1, 1, 1, 1], 
      #2: [0, 0, 1, 1, 1], 
      #3: [0, 0, 0, 1, 1], 
      #4: [0, 0, 0, 0, 1], 
      #5: [0, 0, 0, 0, 0], 
      #6: [1, 0, 0, 0, 0], 
      #7: [1, 1, 0, 0, 0], 
      #8: [1, 1, 1, 0, 0], 
      #9: [1, 1, 1, 1, 0], 
      #0: [1, 1, 1, 1, 1]
      }
        
    height = width/2.33
    self.on = on
    self.off = off
    if(self.typef == "rectangle"):
      self.item = goocanvas.Rect(parent = self.rootitem,
                                 x = x,
                                 y = y,
                                 width = width,
                                 height = height,
                                 radius_x = 5,
                                 radius_y = 5,
                                 line_width = 2.0,
                                 stroke_color = self.stroke_color,
                                 fill_color = self.fill_color
                                 )
      self.rootitem.add_child(self.item)
      if (self.letter != None):
        letter3 = self.letter
                        
        if (self.letter != None):
          self.text1 = goocanvas.Text(parent = self.rootitem,
                                      x = x+40,
                                      y = y+5,
                                      width = 700,
                                      text = str(letter),
                                      fill_color = self.stroke_color,
                                      font = 'Sans BOLD')
            #self.text2 = goocanvas.Text(parent = self.rootitem,
            #                           x = x + 30,
            #                          y = y + 5,
            #                         text = Morse_L[self.letter],
            #                        fill_color = self.stroke_color,
            #                       font = 'Sans BOLD')
          self.rootitem.add_child(self.text1)
           # self.rootitem.add_child(self.text2)
          letter2 = self.letter
          if (self.display == False):
            self.dodo(Morse_L,letter2,x,y,clickable)
          if ((self.clickable == False) and (self.letter != None)):
            self.text1.set_property("text", str.upper(self.letter))
            self.text1.set_property("y",y+5)
            self.text1.set_property("x",x+60)
            self.text1.set_property("font",'Sans 70px')
            
            
                #rect6  = morsedes(self.rootitem,550,150,180,False,True,"rectangle",self.on,self.off,"white","red",None,"A")              
            
            text6 = MorseDes(self.rootitem,600,150,0,False,False,"text",self.on,self.off,"white","black",self.letter,"A") 
            
    if(self.typef == "text"):
      print "hwyeyeyeyey"
      self.dodo(Morse_L,letter,x,y,clickable)
    if(self.typef == "ecllipse"):
      self.ecllipse = goocanvas.Ellipse(parent = self.rootitem,
                                        center_x = x,
                                        center_y = y,
                                        radius_x = x/11,
                                        radius_y = x/11,
                                        stroke_color = "black",
                                        fill_color = "white",
                                        line_width = 2)
      self.rootitem.add_child(self.ecllipse)
    if(self.clickable == True):
      self.item.connect("button_press_event",self.rect_event)
    if isinstance(letter,int):
      fillings = Morse_L.get(letter)
        
    #def rect(self,x,y,width,fill_color,stroke_color):
            
    #def ellipse(self,x,y):
        
  def dodo(self,Morse_L,letter,x,y,clickable):
    i = 20
    j = 10
    em = []
    for k in sorted(Morse_L):
      if k == self.letter:
        print k
        print Morse_L[k]
        for u in Morse_L[k]:
          if (Morse_L[k][u] == 0):
            self.ecllipse1 = goocanvas.Ellipse(parent = self.rootitem,
                                               center_x = x + 22,
                                               center_y = y + 30,
                                               radius_x = 4,
                                               radius_y = 4,
                                               stroke_color = "black",
                                               fill_color = "black",
                                               line_width = 1.0)
            if(self.clickable == False):
              i = 20
              self.ecllipse1.set_property("x",x - 26)
              self.ecllipse1.set_property("y",y + 30)
              self.ecllipse1.set_property("radius_x",6)
              self.ecllipse1.set_property("radius_y",6)
            self.rootitem.add_child(self.ecllipse1)
            x = x + i
            print "dot",
            if Morse_L[k][u] == 1:
              self.rect4 = goocanvas.Rect(parent = self.rootitem,
                                          x = x + 22,
                                          y = y + 28,
                                          width = 15.5,
                                          height = 6,
                                          line_width = 0.5,
                                          stroke_color = "black",
                                          fill_color = "black",
                                          )
              if(self.clickable == False):
                i = 40
                self.rect4.set_property("x",x - 46)
                self.rect4.set_property("y",y + 30)
                self.rect4.set_property("width",30)
                self.rect4.set_property("height",11)
                
              self.rootitem.add_child(self.rect4)
              x = x + i
              print "dash",
        print " "
        
  def get_letter(self):
    """Return the morse item"""
    return self.letter
  
  
  def rect_event(self,event,target,item):
    if target.get_property("fill_color_rgba") == self.on: #to blank 
      target.set_property("fill_color_rgba",self.off)
      rect6  = MorseDes(self.rootitem,550,150,180,False,True,"rectangle",self.on,self.off,"white","black",None,"A")
    else:
      target.set_property("fill_color_rgba",self.on) # when clicked - red
      rect3  = MorseDes(self.rootitem,290,150,180,False,True,"rectangle",self.on,self.off,"white","black",self.letter,"A")
            
      
      
