import pygame
weapon_data = {
  "bell":{"availible":False,"ranged":False},
  "sax":{"availible":False,"ranged":True,"damage":5,"cooldown":100,"projectiles":1,"speed":4,"duration":200,"spread":1,"sprite":"Weapons/Enemy_Bullet.png","scaling":0.8},
  #--------
  "Basic":{"type":"weapon","purchased":True,"availible":True,"cost":25,"ranged":False,"damage":50,"cooldown":30,"projectiles":1,"speed":12,"duration":55,"spread":1,"sprite":"Weapons/Bullet.png","scaling":4,"image": pygame.image.load("Enemies/Bell.png")},
  "Shotgun":{"type":"weapon","purchased":False,"availible":True,"cost":25,"ranged":False,"damage":35,"cooldown":60,"projectiles":9,"speed":20,"duration":25,"spread":60,"sprite":"Weapons/Bullet.png","scaling":4,"image": pygame.image.load("Enemies/Sax.png")},
  "Minigun":{"type":"weapon","purchased":False,"availible":True,"cost":10,"ranged":False,"damage":10,"cooldown":15,"projectiles":3,"speed":10,"duration":35,"spread":30,"sprite":"Weapons/Bullet.png","scaling":4,"image": pygame.image.load("Player/Trent.png")},
  "Lag_Maker":{"type":"weapon","purchased":False,"availible":True,"cost":400,"ranged":False,"damage":200,"cooldown":10,"projectiles":20,"speed":20,"duration":25,"spread":300,"sprite":"Weapons/Bullet.png","scaling":4,"image": pygame.image.load("Enemies/DevlinDeving.png")}
}