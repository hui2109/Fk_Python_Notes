import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from bullet import *

COMMON_SPEED_THRESHOLD = 10
MAN_SPEED_THRESHOLD = 8

TYPE_BOMB = 1
TYPE_FLY = 2
TYPE_MAN = 3


class Monster(Sprite):
    def __init__(self, view_manager, tp=TYPE_BOMB):
        super(Monster, self).__init__()
        self.type = tp
        self.x = 0
        self.y = 0
        self.is_die = False
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.draw_count = 0
        self.draw_index = 0
        self.die_max_draw_count = sys.maxsize
        self.bullet_list = Group()

        if self.type == TYPE_BOMB or self.type == TYPE_MAN:
            self.y = view_manager.Y_DEFALUT
        elif self.type == TYPE_FLY:
            self.y = view_manager.screen_height * 50 / 100 - randint(0, 99)
        self.x = view_manager.screen_width + randint(0, view_manager.screen_width >> 1) - (
                view_manager.screen_width >> 2)

    def draw(self, screen, view_manager):
        if self.type == TYPE_BOMB:
            if self.is_die:
                self.draw_anim(screen, view_manager, view_manager.bomb2_images)
            else:
                self.draw_anim(screen, view_manager, view_manager.bomb_images)
        elif self.type == TYPE_FLY:
            if self.is_die:
                self.draw_anim(screen, view_manager, view_manager.fly_die_images)
            else:
                self.draw_anim(screen, view_manager, view_manager.fly_images)
        elif self.type == TYPE_MAN:
            if self.is_die:
                self.draw_anim(screen, view_manager, view_manager.man_die_images)
            else:
                self.draw_anim(screen, view_manager, view_manager.man_images)
        else:
            pass

    def draw_anim(self, screen, view_manager, bitmap_arr):
        if self.is_die and self.die_max_draw_count == sys.maxsize:
            self.die_max_draw_count = len(bitmap_arr)
        self.draw_index %= len(bitmap_arr)
        bitmap = bitmap_arr[self.draw_index]
        if bitmap is None:
            return None
        draw_x = self.x
        if self.is_die:
            if type == TYPE_BOMB:
                draw_x = self.x - 50
            elif type == TYPE_MAN:
                draw_x = self.x + 50
        draw_y = self.y - bitmap.get_height()
        screen.blit(bitmap, (draw_x, draw_y))
        self.start_x = draw_x
        self.start_y = draw_y
        self.end_x = self.start_x + bitmap.get_width()
        self.end_y = self.start_y + bitmap.get_height()
        self.draw_count += 1

        if type == TYPE_MAN:
            if self.draw_count >= COMMON_SPEED_THRESHOLD:
                if self.type == TYPE_MAN and self.draw_index == 2:
                    self.add_bullet()
                if self.type == TYPE_FLY and self.draw_index == len(bitmap_arr) - 1:
                    self.add_bullet()
                self.draw_index += 1
                self.draw_count = 0
        else:
            if self.draw_count >= MAN_SPEED_THRESHOLD:
                if self.type == TYPE_MAN and self.draw_index == 2:
                    self.add_bullet()
                if self.type == TYPE_FLY and self.draw_index == len(bitmap_arr) - 1:
                    self.add_bullet()
                self.draw_index += 1
                self.draw_count = 0
        if self.is_die:
            self.die_max_draw_count -= 1

        self.draw_bullets(screen, view_manager)
