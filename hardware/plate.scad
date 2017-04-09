fn=100;
grid_size=19;
cutout_size=14;
border=10;
offset=5;
screw_size=2.8;

module cutout() {
  square(cutout_size,true);
}

module column() {
  union() {
    cutout();
    translate([grid_size,0,0]) {
      cutout();
      translate([grid_size,0,0]) {
        cutout();
        translate([grid_size,0,0]) {
          cutout();
          translate([grid_size,0,0]) {
            cutout();
          }
        }
      }
    }
  }
}

module plate() {
  hull() {
    translate([0,-grid_size*7,0]) {
      rotate([0,0,-10]) {
        translate([-17.5,-20,0]) {
          square([(grid_size*5 + (5*4)),(grid_size*8 + 15)]);
        }
      }
    }
    translate([0,grid_size*7,0]) {
      rotate([0,0,10]) {
        mirror([0,1,0]) {
          translate([-17.5,-20,0]) {
            square([(grid_size*5 + (5*4)),(grid_size*8 + 15)]);
          }
        }
      }
    }
  }
}

module pad() {
  union() {
    rotate([0,0,-90])
    union() {
      column();
      translate([-offset,grid_size,0]) {
        column();
        translate([-offset,grid_size,0]) {
          column();
          translate([offset,grid_size,0]) {
            column();
            translate([offset,grid_size,0]) {
              column();
              translate([offset,grid_size,0]) {
                column();
              }
            }
          }
        }
      }
      translate([grid_size*4,grid_size*6,0]) cutout();
      translate([grid_size*4,grid_size*7,0]) cutout();
    }
    translate([-grid_size/2-border/2,grid_size/2+offset*2+border/2]) circle(screw_size/2);
    translate([-grid_size/2-border/2,-1*(grid_size*4.5+offset*3-border/2)]) circle(screw_size/2);
    translate([(grid_size*5.5+border/2),(grid_size*0.5+offset*2+border/2)]) circle(screw_size/2);
    translate([(grid_size*7.5+border/2),-1*(grid_size*4.5+offset*3-border/2)]) circle(screw_size/2);
  }
}

module plate() {
  difference() {
    translate([-(grid_size/2+border),(grid_size/2+offset*2+border)])
    mirror([0,1,0])
    square([grid_size*8+border*2+8.22,grid_size*5+offset*3+2*border]);
  }
}

module cutouts() {
  union() {
    translate([0,-grid_size*7,0]) {
      rotate([0,0,-10]) {
        pad();
      }
    }
    translate([0,grid_size*7,0]) {
      rotate([0,0,10]) {
        mirror([0,1,0]) {
          pad();
        }
      }
    }
  }
}

module rounder(rot) {
  translate([rot*80,35,0])
  rotate([0,0,rot*10])
  difference() {
    square([cutout_size*10,40],true);
  }
}

module half() {
  difference() {
  plate();
  pad();
  }
}

rotate([0,0,-10])
translate([-1*(grid_size*7+10),0])
half();
mirror([1,0,0])
rotate([0,0,-10])
translate([-1*(grid_size*7+10),0])
half();

/* translate([0,0,-10]) */
/* difference() { */
/*   plate(); */
/*   rounder(1); */
/*   rounder(-1); */

/*   translate([-160,-90]) circle(1.4); */
/*   rotate([0,0,-90]) { */
/*     cutouts(); */
/*   } */
/* } */
