import pytest
import math
import session11
from session11 import Polygon  # Importing Polygon from your module

ABS_TOL = 0.001
REL_TOL = 0.001

# =================== TESTING POLYGON CREATION ===================

def test_polygon_invalid_sides():
    """Test that Polygon raises an exception for less than 3 sides."""
    with pytest.raises(ValueError):
        Polygon(2, 10)


def test_polygon_creation():
    """Test creation of a Polygon with valid parameters."""
    p = Polygon(3, 1)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'


# =================== TESTING POLYGON PROPERTIES ===================

def test_polygon_vertex_count():
    """Test number of vertices in the Polygon."""
    p = Polygon(3, 1)
    assert p.count_vertices == 3, f'actual: {p.count_vertices}, expected: 3'


def test_polygon_edge_count():
    """Test number of edges in the Polygon."""
    p = Polygon(3, 1)
    assert p.count_edges == 3, f'actual: {p.count_edges}, expected: 3'


def test_polygon_circumradius():
    """Test circumradius property."""
    p = Polygon(3, 1)
    assert p.circumradius == 1, f'actual: {p.circumradius}, expected: 1'


def test_polygon_interior_angle():
    """Test calculation of interior angle."""
    p = Polygon(3, 1)
    assert math.isclose(p.interior_angle, 60, rel_tol=REL_TOL, abs_tol=ABS_TOL), \
        f'actual: {p.interior_angle}, expected: 60'


# =================== TESTING POLYGON MEASUREMENTS ===================

def test_polygon_side_length():
    """Test side length calculation for a square."""
    p = Polygon(4, 1)
    expected = math.sqrt(2)
    assert math.isclose(p.side_length, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL), \
        f'actual: {p.side_length}, expected: {expected}'


def test_polygon_perimeter():
    """Test perimeter calculation."""
    p = Polygon(4, 1)
    expected = 4 * math.sqrt(2)
    assert math.isclose(p.perimeter, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL), \
        f'actual: {p.perimeter}, expected: {expected}'


def test_polygon_apothem():
    """Test apothem calculation."""
    p = Polygon(4, 1)
    expected = 0.707
    assert math.isclose(p.apothem, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL), \
        f'actual: {p.apothem}, expected: {expected}'


def test_polygon_area():
    """Test area calculation."""
    p = Polygon(6, 2)
    expected = 10.3923
    assert math.isclose(p.area, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL), \
        f'actual: {p.area}, expected: {expected}'


# =================== TESTING POLYGON COMPARISONS ===================

def test_polygon_comparison_greater():
    """Test greater-than comparison between polygons."""
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    assert p2 > p1, "Expected p2 to be greater than p1"


def test_polygon_comparison_lesser():
    """Test less-than comparison between polygons."""
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    assert p2 < p3, "Expected p2 to be less than p3"


def test_polygon_comparison_not_equal():
    """Test inequality comparison."""
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    assert p3 != p4, "Expected p3 and p4 to be different due to circumradius"


def test_polygon_comparison_equal():
    """Test equality comparison."""
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    assert p4 == p5, "Expected p4 and p5 to be equal"