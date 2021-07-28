from math import sqrt, atan, cos, sin, tan
from random import randint, uniform


pi = 3.141592653589793238462643

class Position:
    def __init__(self, phi, r):
        self.phi = phi
        self.r = r
    
    def check(self):
        while self.phi < 0:
            self.phi += 2 * pi
        while self.phi > 2 * pi:
            self.phi -= 2 * pi

    def get_cartesian_coordinates(self, flag = False):
        x = self.r * cos(self.phi)
        y = self.r * sin(self.phi)
        if flag:
            return x+500, y+500
        return x,y
    
    def set_polar_coordinates(self, x, y):
        self.r = sqrt(x ** 2 + y ** 2)
        if x != 0:
            self.phi = atan(y/x)
        elif y >= 0:
            self.phi = pi/2
        else:
            self.phi = 3*pi/2

        self.check()
        if x > 0 and self.phi > pi/2 and self.phi < 3*pi/2:
            self.phi += pi
        elif x < 0 and self.phi < pi/2 and self.phi > 3*pi/2:
            self.phi += pi     
        elif y > 0 and self.phi > pi and self.phi < 2*pi:
            self.phi += pi
        elif y < 0 and self.phi < pi and self.phi > 0:
            self.phi += pi
        self.check()
     


class Vector(Position):
    def __init__(self, phi):
        super().__init__(phi,1)
            

class Entity:
    def __init__(self, position : Position, direction : Vector):
        self.position = position
        self.direction = direction
        self.color = (randint(0,255), randint(0,255), randint(0,255))

    def update_direction(self, target_direction : Position):
        target_direction.check()
        self.direction.check()
        x_dir, y_dir = self.position.get_cartesian_coordinates()
        x_tar, y_tar = target_direction.get_cartesian_coordinates()

        x = x_tar - x_dir
        y = y_tar - y_dir

        target_vector = Vector(0)
        target_vector.set_polar_coordinates(x,y)
        
        relative_direction = target_vector.phi

        if relative_direction > self.direction.phi and relative_direction - self.direction.phi < pi:
            self.direction.phi += 0.02
        else: 
            self.direction.phi -= 0.02
        
        self.direction.check()
        

    def update_position(self):
        x_pos, y_pos = self.position.get_cartesian_coordinates()
        x_dir, y_dir = self.direction.get_cartesian_coordinates()

        if x_pos < 0 or x_pos > 1500 or y_pos < 0 or y_pos > 800:
            x_pos = randint(0,1500)
            y_pos = randint(0,800)

        x = x_pos + x_dir
        y = y_pos + y_dir

        self.position.set_polar_coordinates(x,y)

def createEntities(number : int):
    entities = []
    for i in range(number):
        p_phi = uniform(0,pi/2)
        v_phi = uniform(0,2*pi)
        r = randint(0, 3000)
        p = Position(p_phi,r)
        v = Vector(v_phi)
        entity = Entity(p,v)
        entities.append(entity)
    return entities

def followEntity(entity: Entity, entities : list):
    i = randint(0, len(entities)-1)
    while entities[i] == entity:
        i = randint(0, len(entities)-1)
    
    entity.update_position()
    entity.update_direction(entities[i].position)

