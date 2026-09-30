import numpy as np
import math
from collections import deque
import matplotlib.pyplot as plt
import scipy as sp

import pygame

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 255)
LIME = (128, 255, 0)
PINK = (255, 105, 180)



class Double_Pendulum :
    def __init__(self,mass1, mass2, angle1, angle2, length1, length2, trail_color) :
        G = 6.6743 * 10 ** -11 # N*M^2/kg^2
        r_earth = 6.371 * 10 ** 6 # in m
        mass_e = 5.9722 * 10 ** 24 # in kg
        self.g = G * (mass_e / (r_earth ** 2))

        self.mass1 = mass1
        self.mass2 = mass2
        self.theta1 = math.radians(angle1) 
        self.theta2 = math.radians(angle2) 
        self.length1 = length1
        self.length2 = length2
        self.omega1 = 0.0
        self.omega2 = 0.0

        self.center_x = WIDTH / 2
        self.center_y = HEIGHT / 2

        self.trail_color = trail_color
        self.trail = deque(maxlen=150)


    def physics_update(self, dt) :
        g = self.g
        m1, m2 = self.mass1, self.mass2
        l1, l2 = self.length1, self.length2
        t1, t2 = self.theta1, self.theta2
        w1, w2 = self.omega1, self.omega2

        D = 2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2)

        delta_theta = t1 - t2

        alpha1 = (-g * (2 * m1 + m2) * math.sin(t1) - m2 * g * math.sin(t1 - 2 * t2) - 2 * math.sin(delta_theta) * m2 * (w2**2 * l2 + w1**2 * l1 * math.cos(delta_theta))) / (l1 * D)

        alpha2 = (2 * math.sin(delta_theta) * (w1**2 * l1 * (m1 + m2) + g * (m1 + m2) * math.cos(t1) + w2**2 * l2 * m2 * math.cos(delta_theta))) / (l2 * D)

        self.omega1 += alpha1 * dt
        self.omega2 += alpha2 * dt
        self.theta1 += self.omega1 * dt
        self.theta2 += self.omega2 * dt


    def draw(self, screen) :
        starting_pos_1 = (self.center_x, self.center_y)

        end_x_pos_1 = self.center_x + (self.length1 * math.sin(self.theta1))
        end_y_pos_1 = self.center_y + (self.length1 * math.cos(self.theta1))
        end_pos_1 = (end_x_pos_1, end_y_pos_1)


        starting_pos_2 = end_pos_1

        end_x_pos_2 = end_x_pos_1 + (self.length2 * math.sin(self.theta2))
        end_y_pos_2 = end_y_pos_1 + (self.length2 * math.cos(self.theta2))
        end_pos_2 = (end_x_pos_2, end_y_pos_2)

        pygame.draw.line(screen, GREY, starting_pos_2, end_pos_2, 3)

        pygame.draw.line(screen, GREY, starting_pos_1, end_pos_1, 3)
        pygame.draw.rect(screen, WHITE, (((WIDTH/2 - 50) , (HEIGHT/2 + - 30)), (100, 30)), border_radius=2)
        pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2), 10, draw_bottom_left=True, draw_bottom_right=True)

        self.trail.append(end_pos_2)

        if len(self.trail) > 1:
            trail_len = len(self.trail)
            for i in range(trail_len - 1):
                # progress goes from 0 (oldest) to 1 (newest)
                progress = i / trail_len
                
                # Scale the green brightness and add a bit of blue for a neon look
                fade_green = int(255 * progress)
                fade_blue = int(150 * progress)
                color = (0, fade_green, fade_blue)
                
                # Draw the segment with the faded color
                pygame.draw.line(screen, self.trail_color, self.trail[i], self.trail[i + 1], 2)

        # pygame.draw.circle(screen, WHITE, (0, 0), 500, draw_top_left=True, draw_top_right=True)

        
        pygame.draw.circle(screen, RED, end_pos_2, 15)
        pygame.draw.circle(screen, RED, end_pos_1, 15)






def main() :
    running = True

    pend_1 = Double_Pendulum(10, 10, 90.00, 90, 100, 100, GREEN)
    pend_2 = Double_Pendulum(10, 10, 90.05, 90, 100, 100, CYAN)
    pend_3 = Double_Pendulum(10, 10, 90.10, 90, 100, 100, MAGENTA)
    pend_4 = Double_Pendulum(10, 10, 90.15, 90, 100, 100, YELLOW)
    pend_5 = Double_Pendulum(10, 10, 90.20, 90, 100, 100, ORANGE)
    pend_6 = Double_Pendulum(10, 10, 90.25, 90, 100, 100, PURPLE)

    pendulums = [pend_1, pend_2, pend_3, pend_4, pend_5, pend_6]

    TIME_SCALE = 9.8




    while running :
        dt = CLOCK.tick(FPS) / 1000.0 * TIME_SCALE
        # CLOCK.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        for pendulum in pendulums :
            pendulum.physics_update(dt)
            pendulum.draw(screen)

        pygame.display.update()

    pygame.quit()



main()
