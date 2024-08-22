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
Point(5) = {4, 4, 0, 1.0};
//+
Point(6) = {4, 4.5, 0, 1.0};
//+
Point(7) = {4, 3.5, 0, 1.0};
//+
Circle(5) = {6, 5, 7};
//+
Circle(6) = {7, 5, 6};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Curve Loop(2) = {5, 6};
//+
Plane Surface(1) = {1, 2};
//+
Physical Curve("tb", 7) = {1, 3};
//+
Physical Curve("lr", 8) = {4, 2};
//+
Physical Curve("c", 9) = {5, 6};
//+
Transfinite Surface {1} = {2, 3, 4, 1};
//+
Recombine Surface {1};
//+
Transfinite Curve {5, 6} = 10 Using Progression 1;
//+
Transfinite Curve {4, 2} = 40 Using Progression 1;
//+
Transfinite Surface {1} = {2, 3, 4, 1};
