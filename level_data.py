import pygame

level_data = {
    1:{"room": pygame.image.load("Rooms/Level1.png"), "num_bell": 20, "num_sax": 50, "num_pillar":6, "pillar_posx1":-592,"pillar_posxjump":492, "pillar_posy1": 630, "pillar_posyjump":0, "spawnx":640, "spawny":394},
    2:{"room": pygame.image.load("Rooms/Bossroom.png"), "num_bell": 0, "num_sax": 0, "num_pillar":0, "pillar_posx1":0,"pillar_posxjump":0, "pillar_posy1": 0, "pillar_posyjump":0, "spawnx":640, "spawny":2848},
    3:{"room": pygame.image.load("Rooms/Shop.png"),"spawnx":800, "spawny":1000}
}