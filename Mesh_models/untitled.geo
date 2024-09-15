//+
Point(1) = {8, 8, 0, 1.0};
//+
Point(2) = {8, 0, 0, 1.0};
//+
Point(3) = {0, 0, 0, 1.0};
//+
Point(4) = {0, 8, 0, 1.0};
//+
Line(1) = {4, 1};
//+
Line(2) = {1, 2};
//+
Line(3) = {2, 3};
//+
Line(4) = {3, 4};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Left", 5) = {4};
//+
Physical Curve("Right", 6) = {2};
//+
Physical Curve("Top", 7) = {1};
//+
Physical Curve("Bottom", 8) = {3};
//+
Physical Point("Bottom", 9) = {3, 2};
//+
Physical Point("Left", 10) = {4, 3};
//+
Physical Point("Top", 11) = {4, 1};
//+
Physical Point("Right", 12) = {1, 2};
//+
Transfinite Surface {1} = {4, 1, 2, 3};
//+
Recombine Surface {1};
