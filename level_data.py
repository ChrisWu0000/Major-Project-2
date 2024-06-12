import pygame

level_data = {
    1:{"room": pygame.image.load("Rooms/Level 1.png"), "num_bell": 15, "num_sax": 0,"num_drum": 0,"num_wave":1, "num_pillar":7, "pillar_posx1":-502,"pillar_posxjump":368, "pillar_posy1": 660, "pillar_posyjump":0, "spawnx":640, "spawny":394, "top wall": 150, "left wall": -1100, "right wall": 2424, "bottom wall":759, "exit rect":(1475, 0, 250, 200)},
    2:{"room": pygame.image.load("Rooms/Level 1.png"), "num_bell": 6, "num_sax": 19,"num_drum": 0,"num_wave":1, "num_pillar":7, "pillar_posx1":-502,"pillar_posxjump":368, "pillar_posy1": 660, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 150, "left wall": -1100, "right wall": 2424, "bottom wall":759, "exit rect":(1475, 0, 250, 200)},
    3:{"room": pygame.image.load("Rooms/Level 1.png"), "num_bell": 15, "num_sax": 5,"num_drum": 15,"num_wave":2, "num_pillar":7, "pillar_posx1":-502,"pillar_posxjump":368, "pillar_posy1": 660, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 150, "left wall": -1100, "right wall": 2424, "bottom wall":759, "exit rect":(1475, 0, 250, 200)},
    4:{"room": pygame.image.load("Rooms/Level 1.png"), "num_bell": 45, "num_sax": 9,"num_drum": 12,"num_wave":3, "num_pillar":7, "pillar_posx1":-502,"pillar_posxjump":368, "pillar_posy1": 660, "pillar_posyjump":0, "spawnx":-640, "spawny":394, "top wall": 150, "left wall": -1100, "right wall": 2424, "bottom wall":759, "exit rect":(1475, 0, 250, 200)},
    5:{"room": pygame.image.load("Rooms/Level 1.png"), "num_bell": 20, "num_sax": 40,"num_drum": 12,"num_wave":3, "num_pillar":7, "pillar_posx1":-502,"pillar_posxjump":368, "pillar_posy1": 660, "pillar_posyjump":0, "spawnx":-640, "spawny":394,"top wall": 150, "left wall": -1100, "right wall": 2424, "bottom wall":759, "exit rect":(1475, 0, 250, 200)},
    6:{"room": pygame.image.load("Rooms/Level 2.png"), "num_bell": 40, "num_sax": 60,"num_drum": 16,"num_wave":4, "num_pillar":0, "spawnx":640, "spawny":900, "top wall": 140, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(550, 0, 200, 180)},
    7:{"room": pygame.image.load("Rooms/Level 2.png"), "num_bell": 100, "num_sax": 60,"num_drum": 25,"num_wave":4, "num_pillar":0, "spawnx":640, "spawny":900, "top wall": 140, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(550, 0, 200, 180)},
    8:{"room": pygame.image.load("Rooms/Level 2.png"), "num_bell": 80, "num_sax": 80,"num_drum": 25,"num_wave":4, "num_pillar":0, "spawnx":640, "spawny":900, "top wall": 140, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(550, 0, 200, 180)},
    9:{"room": pygame.image.load("Rooms/Level 2.png"), "num_bell": 50, "num_sax": 80,"num_drum": 45,"num_wave":2, "num_pillar":0, "spawnx":640, "spawny":900, "top wall": 140, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(550, 0, 200, 180)},
    10:{"room": pygame.image.load("Rooms/Level 2.png"), "num_bell": 200, "num_sax": 100,"num_drum": 0,"num_wave":5, "num_pillar":0, "spawnx":640, "spawny":900, "top wall": 140, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(550, 0, 200, 180)},
    11:{"room": pygame.image.load("Rooms/Level 3.png"), "num_bell": 50, "num_sax": 100,"num_drum": 50,"num_wave":4,"num_pillar":0, "spawnx":0, "spawny":900, "top wall": 120, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(-40, 0, 240, 180), "collision rects": [(840, 0, 450, 180), (870, 480, 400, 50)]},
    12:{"room": pygame.image.load("Rooms/Level 3.png"), "num_bell": 150, "num_sax": 50,"num_drum": 50,"num_wave":5,"num_pillar":0, "spawnx":0, "spawny":900, "top wall": 120, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(-40, 0, 240, 180), "collision rects": [(840, 0, 450, 180), (870, 480, 400, 50)]},
    13:{"room": pygame.image.load("Rooms/Level 3.png"), "num_bell": 100, "num_sax": 100,"num_drum": 80,"num_wave":6,"num_pillar":0, "spawnx":0, "spawny":900, "top wall": 120, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(-40, 0, 240, 180), "collision rects": [(840, 0, 450, 180), (870, 480, 400, 50)]},
    14:{"room": pygame.image.load("Rooms/Level 3.png"), "num_bell": 120, "num_sax": 120,"num_drum": 60,"num_wave":6,"num_pillar":0, "spawnx":0, "spawny":900, "top wall": 120, "left wall": -1100, "right wall": 2424, "bottom wall":948, "exit rect":(-40, 0, 240, 180), "collision rects": [(840, 0, 450, 180), (870, 480, 400, 50)]},
    15:{"room": pygame.image.load("Rooms/Final Level Map.png"), "num_bell": 210, "num_sax": 140,"num_drum": 70,"num_wave":1, "num_pillar":0, "spawnx":-640, "spawny":2000, "top wall": 128, "left wall": -1100, "right wall": 2400, "bottom wall":2500, "collision rects": [(-80, 2314, 560, 186), (801, 2314, 560, 186), (560, 120, 160, 130)], "exit rect": (0, 0, 0, 0)},
    0:{"room": pygame.image.load("Rooms/Shop.png"),"spawnx":800, "spawny":1000, "top wall": 120, "left wall": -1100, "right wall": 2424, "bottom wall":1759, "collision rects": [(0, 0, 480, 300), (792, 292, 112, 4), (954, 0, 327, 297)], "exit rect": (480, 0, 260, 180)}
}