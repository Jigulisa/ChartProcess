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
        self.chart = chart
        self.size = (600, 600)
        self.im = Image.new('RGB', self.size, color='aliceblue')
        self.draw = ImageDraw.Draw(self.im)

    def size_file(self):
        weight = max(i[0] for i in self.chart.points) - min(i[0] for i in self.chart.points) + 40
        height = max(i[1] for i in self.chart.points) - min(i[1] for i in self.chart.points) + 40
        weight = 600 if weight < 600 else weight
        height = 600 if height < 600 else height
        self.size = (weight, height)
        self.im.resize(self.size)

    def create_axis(self):
        left, but = min(i[0] for i in self.chart.points), min(i[1] for i in self.chart.points)
        but = -but if but < 0 else 0
        left = -left if left < 0 else 0
        self.draw.line((20 + left, 20, 20 + left, self.size[1] - 20), fill=(0, 0, 0))
        self.draw.line((20, self.size[1] - 20 - but, self.size[0] - 20, self.size[1] - 20 - but), fill=(0, 0, 0))
        self.draw.text((10 + left, 10), self.chart.y, fill=(0, 0, 0, 255))
        self.draw.text((self.size[0] - 15, self.size[1] - 15 - but), self.chart.x, fill=(0, 0, 0, 255))

    def draw_points(self):
        weight = max(i[0] for i in self.chart.points) - min(i[0] for i in self.chart.points)
        height = max(i[1] for i in self.chart.points) - min(i[1] for i in self.chart.points)
        ed_otr = min(self.size[0] // weight, self.size[1] // height)
        for i in self.chart.points:
            self.draw.point((i[0] * ed_otr, i[1] * ed_otr), (0, 0, 0, 255))

    def save(self):
        self.im.save(f'res.{self.format}')

# TODO
# 1 - interface; 2 - fix axises render;


