package edu.uob;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class TriangleTests {

  private static void assertShapeVariant(TriangleVariant expectedType, Triangle shape) {
    assertEquals(expectedType, shape.getVariant(), "failed to classify " + shape + " as " + expectedType);
  }

  // Equilateral: all equal
  @Test
  void testEquilateral() {
    assertShapeVariant(TriangleVariant.EQUILATERAL, new Triangle(8, 8, 8));
  }

  // Isosceles: any two equal
  @Test
  void testIsosceles() {
    assertShapeVariant(TriangleVariant.ISOSCELES, new Triangle(5, 5, 3));
    assertShapeVariant(TriangleVariant.ISOSCELES, new Triangle(5, 3, 5));
    assertShapeVariant(TriangleVariant.ISOSCELES, new Triangle(3, 5, 5));
    assertShapeVariant(TriangleVariant.ISOSCELES, new Triangle(5, 5, 7));
    assertShapeVariant(TriangleVariant.ISOSCELES, new Triangle(5, 7, 5));
    assertShapeVariant(TriangleVariant.ISOSCELES, new Triangle(7, 5, 5));
  }

  // Scalene: all three different (but not special)
  @Test
  void testScalene() {
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(12, 14, 15));
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(14, 12, 15));
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(12, 15, 14));
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(14, 15, 12));
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(15, 12, 14));
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(15, 14, 12));
  }

  // Right-angled: Pythagoras's theorem
  @Test
  void testRight() {
    assertShapeVariant(TriangleVariant.RIGHT, new Triangle(5, 12, 13));
    assertShapeVariant(TriangleVariant.RIGHT, new Triangle(12, 5, 13));
    assertShapeVariant(TriangleVariant.RIGHT, new Triangle(5, 13, 12));
    assertShapeVariant(TriangleVariant.RIGHT, new Triangle(12, 13, 5));
    assertShapeVariant(TriangleVariant.RIGHT, new Triangle(13, 5, 12));
    assertShapeVariant(TriangleVariant.RIGHT, new Triangle(13, 12, 5));
  }

  // Flat: two sides add up to the third
  @Test
  void testFlat() {
    assertShapeVariant(TriangleVariant.FLAT, new Triangle(7, 7, 14));
    assertShapeVariant(TriangleVariant.FLAT, new Triangle(7, 14, 7));
    assertShapeVariant(TriangleVariant.FLAT, new Triangle(14, 7, 7));
    assertShapeVariant(TriangleVariant.FLAT, new Triangle(7, 9, 16));
    assertShapeVariant(TriangleVariant.FLAT, new Triangle(7, 16, 9));
    assertShapeVariant(TriangleVariant.FLAT, new Triangle(9, 16, 7));
    assertShapeVariant(TriangleVariant.FLAT, new Triangle(16, 7, 9));
  }

  // Impossible: two sides add up to less than the third
  @Test
  void testImpossible() {
    assertShapeVariant(TriangleVariant.IMPOSSIBLE, new Triangle(2, 3, 13));
    assertShapeVariant(TriangleVariant.IMPOSSIBLE, new Triangle(2, 13, 3));
    assertShapeVariant(TriangleVariant.IMPOSSIBLE, new Triangle(13, 2, 3));
  }

  // Illegal: a side is zero
  @Test
  void testZero() {
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(0, 0, 0));
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(0, 10, 12));
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(10, 0, 12));
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(10, 12, 0));
  }

  // Illegal: a side is negative
  @Test
  void testNegative() {
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(-1, -1, -1));
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(-1, 10, 12));
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(10, -1, 12));
    assertShapeVariant(TriangleVariant.ILLEGAL, new Triangle(10, 12, -1));
  }

  // Overflow: check that the program doesn't have overflow problems due to
  // using int, float or double. If there are overflow problems, the program will not say Scalene.
  @Test
  void testOverflow() {
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(1100000000, 1705032704, 1805032704));
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(2000000001, 2000000002, 2000000003));
    assertShapeVariant(TriangleVariant.SCALENE, new Triangle(150000002, 666666671, 683333338));
  }
}
