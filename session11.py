import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        self._interior_angle = None

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length
    
    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area = 0.5 * self.count_vertices * self.side_length * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self.count_vertices * self.side_length
        return self._perimeter
    
    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self._n - 2) * 180 / self._n
        return self._interior_angle
    
    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self._n == other._n and self._R == other._R
        return False
    
    def __lt__(self, other):
        if isinstance(other, Polygon):
            return self._n < other._n
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self._n > other._n
        return NotImplemented


class Polygons:
    def __init__(self, max_vertices, common_radius):
        if max_vertices < 3:
            raise ValueError('Polygons must have at least 3 vertices.')
        self._max_vertices = max_vertices
        self._common_radius = common_radius

    def __iter__(self):
        return self.PolygonIterator(self._max_vertices, self._common_radius)
    
    class PolygonIterator:
        def __init__(self, max_vertices, common_radius):
            self._max_vertices = max_vertices
            self._common_radius = common_radius
            self._current_n = 2
        
        def __iter__(self):
            return self
        
        def __next__(self):
            self._current_n += 1
            if self._current_n > self._max_vertices:
                raise StopIteration
            return Polygon(self._current_n, self._common_radius)
