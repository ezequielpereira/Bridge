import pygame

class Bridge:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.world = game.world
        self.joints = []

    def create_world(self):
        rect = pygame.Rect((0,800), (350, -250))
        rect.normalize()
        pygame.draw.rect(self.screen, (100,180,255), rect, 3)
        self.world.add.rect(rect.center, rect.width / 2, rect.height / 2,
            dynamic=False)
        rect = pygame.Rect((1200,800), (-350, -250))
        rect.normalize()
        pygame.draw.rect(self.screen, (100,180,255), rect, 3)
        self.world.add.rect(rect.center, rect.width / 2, rect.height / 2,
            dynamic=False)

    def joint_added(self, joint):
        print "joint added!"
        self.joints.append(joint)

    def for_each_frame(self):
        for joint in self.joints:
            force = joint.GetReactionForce().Length()
            if force > 500:
                print "destroy joint!"
                self.world.world.DestroyJoint(joint)
                self.joints.remove(joint)

