import pygame

img = pygame.image.load('source/0_测试/路飞.jpeg')
pygame.image.save(img, 'source/0_测试/路飞-1.png')

newimg = pygame.transform.flip(img, True, False)
pygame.image.save(newimg, 'source/0_测试/路飞-2.png')

newimg = pygame.transform.flip(img, False, True)
pygame.image.save(newimg, 'source/0_测试/路飞-3.png')

newimg = pygame.transform.scale(img, (1200, 600))
pygame.image.save(newimg, 'source/0_测试/路飞-4.png')

newimg = pygame.transform.scale2x(img)
pygame.image.save(newimg, 'source/0_测试/路飞-5.png')

newimg = pygame.transform.rotate(img, 30.0)
pygame.image.save(newimg, 'source/0_测试/路飞-6.png')

newimg = pygame.transform.rotozoom(img, 30.0, 2.0)
pygame.image.save(newimg, 'source/0_测试/路飞-7.png')

newimg = pygame.transform.chop(img, (50, 50, 100, 100))
pygame.image.save(newimg, 'source/0_测试/路飞-8.png')
