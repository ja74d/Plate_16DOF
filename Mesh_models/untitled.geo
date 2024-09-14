//+
Point(1) = {4, 4, 0, 1.0};
//+
Point(2) = {4, 0, 0, 1.0};
//+
Point(3) = {0, 0, 0, 1.0};
//+
Point(4) = {0, 4, 0, 1.0};
//+
Point(5) = {1, 3, 0, 1.0};
//+
Point(6) = {1, 1, 0, 1.0};
//+
Point(7) = {3, 1, 0, 1.0};
//+
Point(8) = {3, 3, 0, 1.0};
//+
Line(1) = {4, 1};
//+
Line(2) = {1, 2};
//+
Line(3) = {2, 3};
//+
Line(4) = {3, 4};
//+
Line(5) = {5, 8};
//+
Line(6) = {8, 7};
//+
Line(7) = {7, 6};
//+
Line(8) = {6, 5};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Curve Loop(2) = {8, 5, 6, 7};
//+
Plane Surface(1) = {1, 2};
//+
Physical Curve("Left", 9) = {4};
//+
Physical Curve("Right", 10) = {2};
//+
Physical Curve("Top", 11) = {1};
//+
Physical Curve("Bottom", 12) = {3};
//+
Physical Curve("H_bottom", 13) = {7};
//+
Physical Curve("H_top", 14) = {5};
//+
Physical Curve("H_left", 15) = {8};
//+
Physical Curve("H_right", 16) = {6};
//+
Physical Point("Left", 17) = {4, 3};
//+
Physical Point("Top", 18) = {4, 1};
//+
Physical Point("Right", 19) = {1, 2};
//+
Physical Point("Bottom", 20) = {3, 2};
//+
Physical Point("H_left", 21) = {5, 6};
//+
Physical Point("H_top", 22) = {5, 8};
//+
Physical Point("H_right", 23) = {8, 7};
//+
Physical Point("H_bottom", 24) = {6, 7};
//+
Transfinite Surface {1} = {4, 1, 2, 3};
//+
Recombine Surface {1};
