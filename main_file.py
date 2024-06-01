from PIL import ImageDraw, Image


class Schedule:
    def __init__(self, x, y, *pairs):  # the class contains chart's points
        self.points = [*pairs]  # and names of its axises
        self.x = x
        self.y = y

    def add_pairs(self, *pairs):
        self.points += pairs

    def change_names(self, x, y):
        self.x = x
        self.y = y


class TheChart:
    def __init__(self, name, format, chart: Schedule):  # this class will determine
        self.name = name  # the size of image and save it
        self.format = format
        self.sample = chart.points
        self.size = (600, 600)

    def size_file(self):
        weight = max(i[0] for i in self.sample) - min(i[0] for i in self.sample) + 40
        height = max(i[1] for i in self.sample) - min(i[1] for i in self.sample) + 40
        weight = 600 if weight < 600 else weight
        height = 600 if height < 600 else height
        self.size = (weight, height)

    def create(self):
        im = Image.new('RGB', self.size, color='aliceblue')
        draw, left = ImageDraw.Draw(im), min(i[0] for i in self.sample)
        but = min(i[1] for i in self.sample)
        but = -but if but < 0 else 0
        left = -left if left < 0 else 0
        draw.line((20 + left, 20, 20 + left, self.size[1] - 20), fill=(0, 0, 0))
        draw.line((20, self.size[1] - 20 - but, self.size[0] - 20, self.size[1] - 20 - but), fill=(0, 0, 0))
        im.save(f'res.{self.format}')

# TODO 
# 1 - interface; 2 - fix axises render; 3 - label axises
