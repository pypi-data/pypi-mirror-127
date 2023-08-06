from geodome.tessellation import *
from geodome.neighbourhood_search import *

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestDomeCreation(unittest.TestCase):
    def test_icosahedron(self):
        vertices, triangles, adj_list = create_geodesic_dome.py_func(0)
        self.assertEqual(len(vertices), 12)
        self.assertEqual(len(triangles), 20)

        distances = calc_dist.py_func(vertices)
        for d in distances:
            self.assertEqual(d, 1)

    def test_icosahedron_freq_1(self):
        vertices, triangles, adj_list = create_geodesic_dome.py_func(1)
        self.assertEqual(len(vertices), 42)
        self.assertEqual(len(triangles), 80)

    def test_icosahedron_freq_2(self):
        vertices, triangles, adj_list = create_geodesic_dome.py_func(2)
        self.assertEqual(len(vertices), 162)
        self.assertEqual(len(triangles), 320)

    def test_default_0(self):
        vertices, triangles, adj_list = create_geodesic_dome.py_func()
        self.assertEqual(len(vertices), 12)
        self.assertEqual(len(triangles), 20)
