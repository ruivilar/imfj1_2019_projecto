# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Copy of visualizer that will be tuned to look like an FPS
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

    # Moves the camera back 3 units
    scene.camera.position -= vector3(0,0,5)

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
    obj2.position += vector3(1, -2 , 2)
    obj2.scale = vector3(3,3,3)
    obj2.mesh = Mesh.create_pyramid((1, 1, 1))
    obj2.material = Material(color(1,1,1,1), "TestMaterial2")
    obj1.add_child(obj2)

    # Create a cube for the environment
    obj3 = Object3d("ChildObject")
    obj3.scale = vector3(2, 2, 2)
    obj3.position = vector3(3, 1, 2)
    obj3.mesh = Mesh.create_cube((1, 1, 1))
    obj3.material = Material(color(1,0,0,1), "TestMaterial1")
    obj1.add_child(obj3)

    # Middle screen circle
    # circle_location_x = res_x/2
    # circle_location_y= res_y/2
    # pygame.draw.circle(screen,(1,1,0),(circle_location_x,circle_location_y),12)

    # Create a cube ( Adapted middle screen circle)
    obj4 = Object3d("cube")
    obj4.scale = vector3(0.01,0.01,0.01)
    obj4.position += vector3(0,0.,0)
    obj4.mesh = Mesh.create_cube((3,3,3))
    obj4.material = Material(color(1,1,0,0), "TestMaterial3")
    scene.add_object(obj4)

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

        # Moves character
        k = pygame.key.get_pressed()

        # Moving Left - A (Inverted from Visualizer)
        if (k[pygame.K_a]):
            desloca = vector3(-0.005,0,0)
            obj1.position += desloca

        # Moving Right - D (Inverted from Visualizer)
        if (k[pygame.K_d]):
            desloca = vector3(0.005,0,0)
            obj1.position += desloca

        # Moving Forward - W (Q in Visualizer)
        if (k[pygame.K_w]):
            desloca = vector3(0,0,-0.005)
            obj1.position += desloca

        # Moving Back - S (E in Visualizer)
        if (k[pygame.K_s]):
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
