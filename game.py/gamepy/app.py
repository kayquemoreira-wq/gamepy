import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('bg','pipe.png')))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('bird1','pipe.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('bird2','pipe.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('bird3','pipe.png')))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Passaro:
    IMGS = IMAGEM_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def init(self, x, y):
      self.x = x
      self.y = y
      self.angulo = 0
      self.velocidade = 0
      self.altura = self.y
      self.tempo = 0
      self.contagem_imagem = 0
      self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

        def mover(self):
            self.tempo += 1
            deslocamento = 1.5 * (self.tempo**2) + self. velocidade * self.tempo

            if deslocamento > 16:
                deslocamento = 16
            elif deslocamento < 0:
                deslocamento -= 2

                self.y =+ deslocamento
                if deslocamento < 0 or self.y (self.altura + 50):
                    if self.angulo < self.ROTACAO_MAXIMA:
                       self.angulo = self.ROTACAO_MAXIMA

                else:
                    if self.angulo > -90:
                       self.angulo -= self.VELOCIDADE_ROTACAO

        def desenhar(self, tela):
            self.contagem_imagem += 1

            if self.contagem_imagem < self.TEMPO_ANIMACAO:
                self.imagem = self.IMGS[0]

            elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
                self.imagem = self.IMGS[1]

            elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
                self.imagem = self.IMGS[2]

            elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
                self.imagem = self.IMGS[1]

            elif self.contagem_imagem < self.TEMPO_ANIMACAO*4 + 1:
                self.imagem = self.IMGS[0]
                self.contagem_imagem = 0

            if self.angulo <= -80:
                self.imagem = self.IMGS[1]
                self.contagem_imagem = self.TEMPO_ANIMACAO*2

            imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
            pos_centro_imagem = self.imagem.get.rect(topleft=(self.x, self.y)).center
            retangulo = imagem_rotacionada.get.rect(center=pos_centro_imagem)
            tela.blit(imagem_rotacionada, retangulo.topleft)

        def get_mask(self):
            return pygame.mask.from_surface(self.imagem)

class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))



