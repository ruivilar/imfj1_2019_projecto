# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create a pyramid and place it in a scene, at position (0,0,0)
    # This pyramid has a squared base that has 1 unit of side, and is pink.
    obj1 = Object3d("TestObject")
    obj1.scale = vector3(1, 1, 1)
    obj1.mesh = Mesh.create_pyramid((1, 1, 1))
    obj1.material = Material(color(1,0,1,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, 0.75, 0)
    obj2.mesh = Mesh.create_pyramid((0.5, 0.5, 0.5))
    obj2.material = Material(color(1,1,1,1), "TestMaterial2")
    obj1.add_child(obj2)

    # Specify the rotation of the object. It will rotate 15 degrees around the axis given, 
    # every second
    angle = 15
    axis = vector3(1,1,1)
    axis.normalize()

    # Timer
    delta_time = 0
    prev_time = time.time()

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))

        # Rotates and moves the object
        k = pygame.key.get_pressed()
        
        # Around y axis - RIGHT/LEFT
        if (k[pygame.K_RIGHT]):
            angle = 35
            axis = vector3(0,1,0)
            axis.normalize()
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        
        if (k[pygame.K_LEFT]):
            angle = 35
            axis = vector3(0,-1,0)
            axis.normalize()
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        # Around x axis - UP/DOWN
        if (k[pygame.K_UP]):
            angle = 35
            axis = vector3(1,0,0)
            axis.normalize()
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        
        if (k[pygame.K_DOWN]):
            angle = 35
            axis = vector3(-1,0,0)
            axis.normalize()
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        # Around z axis - PAGEUP/PAGEDOWN
        if (k[pygame.K_PAGEUP]):
            angle = 35
            axis = vector3(0,0,1)
            axis.normalize()
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation
        
        if (k[pygame.K_PAGEDOWN]):
            angle = 35
            axis = vector3(0,0,-1)
            axis.normalize()
            q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        # Object moves right - S
        if (k[pygame.K_d]):
            desloca = vector3(-0.005,0,0)

            
            obj1.position += desloca

        # Object moves left - A
        if (k[pygame.K_a]):
            desloca = vector3(0.005,0,0)

            
            obj1.position += desloca
       

        # Object moves up - W
        if (k[pygame.K_w]):
            desloca = vector3(0,0.005,0)

            
            obj1.position += desloca


        # Object moves down - S
        if (k[pygame.K_s]):
            desloca = vector3(0,-0.005,0)

            
            obj1.position += desloca

        # Object moves forward - Q
        if (k[pygame.K_q]):
            desloca = vector3(0,0,-0.005)

            
            obj1.position += desloca

        # 0bject moves back - E
        if (k[pygame.K_e]):
            desloca = vector3(0,0,0.005)

            
            obj1.position += desloca

        

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
