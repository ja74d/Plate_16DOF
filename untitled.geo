//+
Point(1) = {1, 1, 0, 1.0};
//+
Point(2) = {1, 0, 0, 1.0};
//+
Point(3) = {0, 1, 0, 1.0};
//+
Point(4) = {0, 0, 0, 1.0};
//+
Line(1) = {3, 1};
//+
Line(2) = {1, 2};
//+
Line(3) = {2, 4};
//+
Line(4) = {4, 3};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1};
//+
Physical Curve("L", 5) = {4};
//+
Physical Curve("R", 6) = {2};
//+
Physical Curve("T", 7) = {1};
//+
Physical Curve("b", 8) = {3};
//+
Transfinite Surface {1} = {3, 1, 2, 4};
//+
Recombine Surface {1};
