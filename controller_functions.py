import pygame


def get_controllers():
    controllers = []
    for controller in range(pygame.joystick.get_count()):
        controllers.append(pygame.joystick.Joystick(controller))
        controllers[-1].init()
    return controllers


def get_controller_events(cont):
    axes = [cont.get_axis(ax) for ax in range(cont.get_numaxes())]
    buttons = [cont.get_button(bt) for bt in range(cont.get_numbuttons())]
    hats = [cont.get_hat(hat) for hat in range(cont.get_numhats())]
    return axes, buttons, hats


###-------------------- SIMPLE CONTROLLER GUIDE --------------------###

#Buttons
#0 	X
#1 	Circle
#2 	Square
#3 	Triangle
#4 	Share
#5 	PS
#6 	Options
#7 	L3
#8 	R3
#9 	L1
#10 	R1
#11 	Down Arrow
#12 	Up Arrow 
#13 	Left Arrow
#14 	Right Arrow
#15 	D-Pad

#Axes
#0	L Right-Left
#1	L Up-Down
#2	R Right-Left
#3	R Up-Down
#4	L2
#5	R2

###-----------------------------------------------------------------###


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.joystick.init()
    controllers = get_controllers()

    for controller in controllers:
        print(get_controller_events(controller))

    try:
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")
                    for controller in controllers:
                        print(get_controller_events(controller))
                elif event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.")
                    for controller in controllers:
                        print(get_controller_events(controller))
            clock.tick(20)
    except Exception as error:
        print(error)
    pygame.quit()
                

if __name__ == '__main__':
    main()



