from ursina import *
import time

app = Ursina()

worldscale = 1
world_x = 1
world_y = 0

cube = Entity(model='cube', color=color.green,scale_y = 2, scale=worldscale )

def update():
    global worldscale
    global world_x
    global world_y

    
    world_x -= held_keys['d'] * time.dt *2
    world_x += held_keys['a'] * time.dt *2

    worldscale += held_keys['w'] * time.dt
    worldscale -= held_keys['s'] * time.dt 

    world_y -= held_keys['space'] * time.dt

    cube.x = world_x
    cube.y = world_y
    cube.scale = worldscale


def input(key):
    pass


app.run()