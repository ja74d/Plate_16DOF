//+
Point(1) = {8, 8, 0, 1.0};
//+
Point(2) = {0, 0, 0, 1.0};
//+
Point(3) = {0, 8, 0, 1.0};
//+
Point(4) = {8, -0, 0, 1.0};
//+
Line(1) = {3, 1};
//+
Line(2) = {1, 4};
//+
Line(3) = {4, 2};
//+
Line(4) = {2, 3};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Left", 5) = {4};
//+
Physical Curve("Top", 6) = {1};
//+
Physical Curve("Right", 7) = {2};
//+
Physical Curve("Bottom", 8) = {3};
//+
Physical Point("Bottom", 9) = {2, 4};
//+
Physical Point("Left", 10) = {2, 3};
//+
Physical Point("Top", 11) = {3, 1};
//+
Physical Point("Right", 12) = {1, 4};
//+
Transfinite Surface {1} = {3, 1, 4, 2};
//+
Recombine Surface {1};
