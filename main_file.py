from PIL import ImageDraw, Image


class TheChart:
    def __init__(self, if_sort: bool, frt: str, name: str, x: str, y: str, *pairs: tuple[int, int]):
        """
        The class contains chart's points

        :param if_sort:
        :param frt:
        :param name:
        :param x:
        :param y:
        :param pairs:
        """

        self.points = [*pairs]  # and names of its axises
        self.x = x
        self.y = y
        self.name = name
        self.frt = frt
        self.sorting = if_sort

    def add_pairs(self, *pairs: tuple[int, int]):
        """

        :param pairs:
        :return:
        """

        self.points += pairs

    def change_names(self, x: str, y: str):
        """

        :param x:
        :param y:
        :return:
        """

        self.x = x
        self.y = y


class TheGrafics:
    def __init__(self, chart: TheChart):
        """
        This class will determine

        :param chart:
        """

        self.chart = chart  # the size of image and save it
        self.size = (600, 600)
        self.im = Image.new('RGB', self.size, color='aliceblue')
        self.draw = ImageDraw.Draw(self.im)
        self.center = (0, 0)

    def size_file(self) -> None:
        """

        :return: None
        """

        weight = max(i[0] for i in self.chart.points) - min(i[0] for i in self.chart.points) + 40
        height = max(i[1] for i in self.chart.points) - min(i[1] for i in self.chart.points) + 40
        weight = 600 if weight < 600 else weight
        height = 600 if height < 600 else height
        self.size = (weight, height)
        self.im.resize(self.size)

    def create_axis(self) -> None:
        """

        :return: None
        """

        left, but = min(i[0] for i in self.chart.points), min(i[1] for i in self.chart.points)
        but = -but if but < 0 else 0
        left = -left if left < 0 else 0
        self.draw.line((20 + left, 20, 20 + left, self.size[1] - 20), fill=(0, 0, 0))
        self.draw.line((20, self.size[1] - 20 - but, self.size[0] - 20, self.size[1] - 20 - but), fill=(0, 0, 0))
        self.draw.text((10 + left, 10), self.chart.y, fill=(0, 0, 0, 255))
        self.draw.text((self.size[0] - 15, self.size[1] - 15 - but), self.chart.x, fill=(0, 0, 0, 255))
        self.center = (20 + left, self.size[1] - 20 - but)

    def sort_points(self) -> None:
        """

        :return: None
        """

        if self.chart.sorting:
            self.chart.points = sorted(self.chart.points, key=lambda x: x[0])

    def draw_points(self) -> None:
        """

        :return: None
        """

        weight = max(i[0] for i in self.chart.points) - min(i[0] for i in self.chart.points)
        height = max(i[1] for i in self.chart.points) - min(i[1] for i in self.chart.points)
        ed_otr = min(self.size[0] // weight, self.size[1] // height)

        for i in range(len(self.chart.points) - 1):
            m, v, c, d = (self.chart.points[i][0] * ed_otr,
                          (self.size[1] - self.chart.points[i][1] * ed_otr),
                          self.chart.points[i + 1][0] * ed_otr,
                          (self.size[1] - self.chart.points[i + 1][1] * ed_otr))
            self.draw.line((m, v, c, d), (0, 0, 0, 255))

    def save(self) -> None:
        """

        :return: None
        """

        self.im.save(f'{self.chart.name}.{self.chart.frt}')


# TODO
# 1 interface; 2 fix axises render; 3 make current coordinates for cursor;


# example
b = Schedule(True, 'jpg', 'schedule', 'x axis', 'y axis', (1, 2), (3, 4), (-1, 3), (4, 2))
a = TheChart(b)
a.size_file()
a.create_axis()
a.sort_points()
a.draw_points()
a.save()
