import pygame

level_data = {
    1:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 0, "num_sax": 20,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    2:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 5, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    3:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 10, "num_sax": 5,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    4:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 0, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    5:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 40, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    6:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 50, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    7:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 60, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    8:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 80, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    9:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 100, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    10:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 130, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    11:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 150, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    12:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 200, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    13:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 230, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    14:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 290, "num_sax": 0,"num_wave":3,"num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    15:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 500, "num_sax": 0,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 160, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    0:{"room": pygame.image.load("Rooms/Shop.png"),"spawnx":800, "spawny":1000, "top wall": -100, "left wall": -1100, "right wall": 2424, "bottom wall":1788}
}