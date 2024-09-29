//+
Point(1) = {8, 8, 0, 1.0};
//+
Point(2) = {8, 0, 0, 1.0};
//+
Point(3) = {0, 0, 0, 1.0};
//+
Point(4) = {0, 8, 0, 1.0};
//+
Point(5) = {2, 2, 0, 1.0};
//+
Point(6) = {2, 6, 0, 1.0};
//+
Point(7) = {6, 6, 0, 1.0};
//+
Point(8) = {6, 2, 0, 1.0};
//+
Line(1) = {4, 1};
//+
Line(2) = {1, 2};
//+
Line(3) = {2, 3};
//+
Line(4) = {3, 4};
//+
Line(5) = {6, 7};
//+
Line(6) = {7, 8};
//+
Line(7) = {8, 5};
//+
Line(8) = {5, 6};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Curve Loop(2) = {8, 5, 6, 7};
//+
Plane Surface(1) = {1, 2};
//+
Physical Curve("Left", 9) = {4};
//+
Physical Curve("Top", 10) = {1};
//+
Physical Curve("Right", 11) = {2};
//+
Physical Curve("Bottom", 12) = {3};
//+
Physical Point("Left", 13) = {3, 4};
//+
Physical Point("Top", 14) = {4, 1};
//+
Physical Point("Right", 15) = {1, 2};
//+
Physical Point("Bottom", 16) = {2, 3};
//+
Transfinite Surface {1} = {4, 1, 2, 3};
//+
Recombine Surface {1};
