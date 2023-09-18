##Snow##

init -1 python:

    import random

    random.seed()

    def Snow(image, max_particles=25, speed=100, wind=100, xborder=(0,30), yborder=(0,30), **kwargs):

        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))

    class SnowFactory(object):
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            self.max_particles = max_particles
            self.speed = speed
            self.wind = wind

            self.xborder = xborder
            self.yborder = yborder

            self.depth = kwargs.get("depth", 10)

            self.image = self.image_init(image)

        def create(self, particles, st):

            if particles is None or len(particles) < self.max_particles:

                depth = random.randint(1, self.depth)
                depth_speed = 1.5-depth/(self.depth+0.0)

                return [ SnowParticle(self.image[depth-1],      # the image used by the particle
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]

        def image_init(self, image):
            rv = [ ]

            for depth in range(self.depth):
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0

                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv

        def predict(self):
            return self.image

    class SnowParticle(object):
        def __init__(self, image, wind, speed, xborder, yborder):

            self.image = image

            if speed <= 0:
                speed = 1

            self.wind = wind
            self.speed = speed
            self.oldst = None

            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder


        def update(self, st):

            if self.oldst is None:
                self.oldst = st

            lag = st - self.oldst
            self.oldst = st

            self.xpos += lag * self.wind
            self.ypos += lag * self.speed

            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None

            return int(self.xpos), int(self.ypos), st, self.image