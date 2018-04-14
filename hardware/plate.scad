points = [[15.130052, -10.594177], [292.869945, -10.594177], [110.44052333333333, -10.594177], [197.5594736666667, -10.594177], [-2.637813, 90.172403], [310.637811, 90.172403], [153.999999, 118.900263], [75.681093, 104.536333], [232.318905, 104.536333]];

$fn = 200;

module mounting_holes(width) {
  for (point = points) {
    translate([point[0], point[1], 0])
      circle(width, true);
  }
}

/* linear_extrude(height=.1) */
difference() {
  hull() mounting_holes(4);
  mounting_holes((2.5 - .254)/2);
}

/* hull() mounting_holes(3.625); */
