import pygame

level_data = {
    1:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 15, "num_sax": 1,"num_drum": 1,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    2:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 5, "num_sax": 15,"num_drum": 1,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    3:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 15, "num_sax": 5,"num_drum": 15,"num_wave":3, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    4:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 45, "num_sax": 9,"num_drum": 12,"num_wave":4, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    5:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 20, "num_sax": 40,"num_drum": 12,"num_wave":4, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    6:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 40, "num_sax": 60,"num_drum": 16,"num_wave":4, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    7:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 100, "num_sax": 60,"num_drum": 25,"num_wave":5, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    8:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 80, "num_sax": 80,"num_drum": 25,"num_wave":5, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    9:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 50, "num_sax": 80,"num_drum": 45,"num_wave":5, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    10:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 150, "num_sax": 100,"num_drum": 1,"num_wave":5, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    11:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 50, "num_sax": 100,"num_drum": 50,"num_wave":5, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    12:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 150, "num_sax": 50,"num_drum": 50,"num_wave":5, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    13:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 100, "num_sax": 100,"num_drum": 60,"num_wave":6, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    14:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 120, "num_sax": 120,"num_drum": 60,"num_wave":6,"num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 200, "left wall": -1100, "right wall": 2424, "bottom wall":788},
    15:{"room": pygame.image.load("Rooms/BossRoom.png"), "num_bell": 210, "num_sax": 140,"num_drum": 70,"num_wave":7, "num_pillar":0, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":-640, "spawny":2000, "top wall": 80, "left wall": -1100, "right wall": 960, "bottom wall":2136},
    0:{"room": pygame.image.load("Rooms/Shop.png"),"spawnx":800, "spawny":1000, "top wall": -100, "left wall": -1100, "right wall": 2424, "bottom wall":1788}
}