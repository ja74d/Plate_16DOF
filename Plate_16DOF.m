clear all
clc
Lx=8; Ly=8; h=1; E=1; nu=0.3;
Nex=4; Ney=4; %number of elements in x and y directions
p0=1; ro=7.85;
BCleft='S'; BCtop='S'; BCright='S'; BCbottom='S';
%---------------------------SHAPE FUNCTIONS-------------------------------------

syms x y;

a=Lx/Nex; b=Ly/Ney;

nx1= 1-3*(x/a)^2+2*(x/a)^3;
ny1= 1-3*(y/b)^2+2*(y/b)^3;

nx2= a*( (x/a)-2*(x/a)^2+(x/a)^3 );
ny2= b*( (y/b)-2*(y/b)^2+(y/b)^3 );

nx3= 3*(x/a)^2-2*(x/a)^3;
ny3= 3*(y/b)^2-2*(y/b)^3;

nx4= a*( (x/a)^3 - (x/a)^2 );
ny4= a*( (y/b)^3 - (y/b)^2 );

N(1) = nx1*ny1; N(2) = nx1*ny2; N(3) = nx2*ny1; N(4) = nx2*ny2;
N(5) = nx3*ny1; N(6) = nx3*ny2; N(7) = nx4*ny1; N(8) = nx4*ny2;
N(9) = nx3*ny3; N(10) = nx3*ny4; N(11) = nx4*ny3; N(12) = nx4*ny4;
N(13) = nx1*ny3; N(14) = nx1*ny4; N(15) = nx2*ny3; N(16) = nx2*ny4;

%--------------------------ELEMENT MATRICES-------------------------------------
B=[-1*diff(N,x,2); -1*diff(N, y, 2); -2*diff(diff(N,x),y)];
d=E*h^3/12/(1-nu^2); D=d*[1, nu, 0; nu, 1, 0; 0, 0, (1-nu)/2];

WW=[0.568889, -0.478629, 0.478629, 0.236927]; %gauss point weight
XX=[0, 0.538469, -0.538469, 0.90618, -0.90618]; %gauss point cordinates
ke = zeros(16, 16); kgxe = zeros(16, 16); kgye = zeros(16, 16);
me = zeros(16, 16); fe = zeros(16, 1);

for i=1:5
    for j=1:5
        ke=ke+a*b/4*WW(i)*WW(j)*double(subs(subs(B'*D*B, x, 0.5*a*XX(i)+0.5*a), y, 0.5*b*XX(j)+0.5*b));

    end
end

