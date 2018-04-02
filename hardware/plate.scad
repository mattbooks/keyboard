:/* points = [[15.13005222144496, -10.59417718175523], [292.86994577855506, -10.59417718175523], [-2.6378138182447697, 90.17240322144497], [310.63781181824476, 90.17240322144497], [153.999999, 118.90026310392955]]; */

points = [[15.130052, -10.594177], [292.869945, -10.594177], [110.44052333333333, -10.594177], [197.5594736666667, -10.594177], [-2.637813, 90.172403], [310.637811, 90.172403], [153.999999, 118.900263], [75.681093, 104.536333], [232.318905, 104.536333]];

$fn = 200;

module mounting_holes(width) {
  for (point = points) {
    translate([point[0], point[1], 0])
      circle(width, true);
  }
}

/* linear_extrude(height=4) */
difference() {
  hull() mounting_holes(4);
  mounting_holes(1.6 - .125);
}

/* hull() mounting_holes(3.625); */
