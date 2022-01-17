# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
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
            #coordonnees du coin gauche (numero 0) de la face externe
                [0, 0, 0 ], 
                
                #coordonnees des 7 autres sommets de la section dans l'ordre suivant :    
                #1 en haut à gauche
                [0, 0, self.parameters['height']],
                #2 en haut à gauche
                [self.parameters['width'], 0, self.parameters['height']],
                #3 en bas à gauche
                [self.parameters['width'], 0, 0], 
                #4 en bas à droite
                [0,self.parameters['thickness'],0],
                #5 en haut à droite
                [0,self.parameters['thickness'],self.parameters['height']],
                #6 en bas à droite
                [self.parameters['width'],self.parameters['thickness'],0],
                #7 en haut à droite
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']]   
                # Définir ici les sommets
                ]
        self.faces = [
            #chaque face est composee de 4 sommets
            #on initialise les 6 faces
                [0, 3, 2, 1],
                [2,3,6,7],
                [6,7,5,4],
                [0,4,5,1],
                [1,2,7,5], 
                [0,3,6,4]
                ]
              
          

    # Checks if the opening can be created for the object x
    #Cette méthode retourne True si une ouverture, représentée par x, 
    #peut être ajoutée dans la section, représentée par self, et False sinon
    def canCreateOpening(self, x):
        #on compare la position et la taille de chacune des 3 dimensions
        return (self.parameters["width"] >= x.parameters["width"] 
                and self.parameters["height"] >= x.parameters["height"] 
                and self.parameters["position"][1] == x.parameters["position"][1] 
                and self.parameters["position"][0] <= x.parameters["position"][0] 
                and self.parameters["position"][0] + self.parameters["width"]>= x.parameters["position"][0] + x.parameters["width"] 
                and self.parameters["position"][2] <= x.parameters["position"][2] 
                and self.parameters["position"][2] + self.parameters["height"]>= x.parameters["position"][2]+ x.parameters["height"]) 
#        #position de x + longueur
#        if self.parameters['position'][0]<x.parameters['position'][0]:
#            
#            if self.parameters['position'][0]+self.parameters['width']>x.parameters['position'][0]+x.parameters['width']:
#        #position de y + épaisseur
#               if self.parameters['position'][1]<x.parameters['position'][1]:
#                   if self.parameters['position'][1]+self.parameters['thickness']>x.parameters['position'][1]+x.parameters['thickness']:
#                       #position de z + hauteur
#                       if self.parameters['position'][2]<x.parameters['position'][2]:
#                           if self.parameters['position'][2]+self.parameters['height']>x.parameters['position'][2]+x.parameters['height']:
#                               return True
#        return False
                   
        
    # Creates the new sections for the object x
    #Retourne la liste des sections engendrées par la création de l’ouverture
    def createNewSections(self, x):
        #on initialise la liste de sortie
        rep = [] 
        
        #on simplifie les noms des parametres de la section
        position=self.parameters['position'] 
        width=self.parameters['width'] 
        height=self.parameters['height'] 
        thickness=self.parameters['thickness'] 
        orientation=self.parameters['orientation'] 
        edges=self.parameters['color'] 
        color=self.parameters['color'] 

        if self.canCreateOpening(x): 
          if x.getParameter('position')[0]>position[0]: 
              #une ouverture va créer 4 sections dont 
        #l'epaisseur sera la même que celle de la section initiale

            sect1= Section({'position': position, 

            'width': x.getParameter('position')[0]-position[0], 
            'height': height, 
            'thickness': thickness})   
            rep.append(sect1) 

          if (x.getParameter('position')[2] + x.getParameter('height')!=height+position[2]): 

             

              sect2=Section({ 

              'position': [x.getParameter('position')[0], position[1],x.getParameter('position')[2]+x.getParameter('height')], 
              'width': x.getParameter('width'), 
              'height': position[2]+height - (x.getParameter('position')[2]+x.getParameter('height')), 
              'thickness': thickness, 
              'orientation': orientation, 
              'edges':edges, 
              'color': color}) 

              rep.append(sect2) 


          if (x.getParameter('position')[2]>position[2]): 

            sect3=Section({ 

            'position': [x.getParameter('position')[0], position[1],position[2]], 
            'width': x.getParameter('width'), 
            'height': x.getParameter('position')[2]-position[2], 
            'thickness': thickness, 
            'orientation': orientation, 
            'edges':edges, 
            'color': color}) 
            rep.append(sect3) 

           
          if (width+position[0]>(x.getParameter('position')[0]+x.getParameter('width'))): 

            sect4= Section({ 

            'position': [x.getParameter('position')[0]+x.getParameter('width'), position[1],position[2]], 
            'width': position[0]+width-(x.getParameter('position')[0]+x.getParameter('width')), 
            'height': height, 
            'thickness': thickness, 
            'orientation': orientation, 
            'edges':edges, 
            'color': color}) 
            rep.append(sect4) 

          
        return rep     
        
        
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
        
    # Tracer les faces de la section en gris
    def draw(self):
        #on execute drawEdges() avant de dessiner les faces
        if self.parameters['edges']:
            self.drawEdges()
        gl.glPushMatrix()    
        #on effectue une translation en se plaçant au coin inferieur gauche
        gl.glTranslate(self.parameters['position'][0],
                       self.parameters['position'][1], 
                       self.parameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # on definit la couleur gris moyen
        
        #iteration sur chaque face
        for i in self.faces:
            #dans chaque face on colorie chaque sommet
            for sommet in i:
                gl.glVertex3fv(self.vertices[sommet])
        gl.glEnd()
        gl.glPopMatrix()
       
  
  

  
  
