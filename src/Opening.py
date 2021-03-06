# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices = [ 
                # Définir ici les sommets
                [0,0,0],
                [0,0,self.parameters['height']],
                [self.parameters['width'],0,self.parameters['height']],
                [self.parameters['width'],0,0],
                [0,self.parameters['thickness'],0],
                [0,self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],0],
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']]
                ]
                
        self.faces = [
                # définir ici les faces
                # seules 4 faces sont necessaires pour créer une ouverture
                [0,3,6,4],
                [5,1,2,7],
                [0,4,5,1],
                [3,6,7,2]
                ]

        # Tracer les arêtes
    def drawEdges(self):
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],
                       self.parameters['position'][1], 
                       self.parameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        # on definit la couleur des arêtes qui sera plus sombre que celle des faces
        gl.glColor3fv([self.parameters['color'][0]*0.5,
                       self.parameters['color'][1]*0.5,
                       self.parameters['color'][2]*0.5]) 
        
        #iteration sur chaque face
        for i in self.faces:
            #dans chaque face on colorie chaque sommet
            for sommet in i:
                gl.glVertex3fv(self.vertices[sommet])
        gl.glEnd() 
        gl.glPopMatrix() 

    # Draws the faces
    # affichage d'une ouverture par construction de murs (sections) et d'arêtes        
    def draw(self): 
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],
                      self.parameters['position'][1],
                      self.parameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) 
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv([self.parameters['color'][0]*0.5,
                         self.parameters['color'][1]*0.5,
                         self.parameters['color'][2]*0.5])
        for face in self.faces:
             for sommet in face:
              gl.glVertex3fv(self.vertices[sommet])
        gl.glEnd()

    #les aretes ne sont pas indispensables
#        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) 
#      gl.glBegin(gl.GL_QUADS) 
#      gl.glColor3fv([self.parameters['color'][0]*0.1,
#                     self.parameters['color'][1]*0.1,
#                     self.parameters['color'][2]*0.1])
#      for face in self.faces:
#        for vertex in face:
#          gl.glVertex3fv(self.vertices[vertex])
#      gl.glEnd()
      
        gl.glPopMatrix()   
