//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 8, 0, 1.0};
//+
Point(3) = {8, 8, 0, 1.0};
//+
Point(4) = {8, 0, 0, 1.0};
//+
Line(1) = {2, 3};
//+
Line(2) = {3, 4};
//+
Line(3) = {4, 1};
//+
Line(4) = {1, 2};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("l", 5) = {4};
//+
Physical Curve("r", 6) = {2};
//+
Physical Curve("t", 7) = {1};
//+
Physical Curve("b", 8) = {3};
//+
Transfinite Surface {1};
//+
Transfinite Surface {1} = {2, 3, 4, 1};
//+
Recombine Surface {1};
