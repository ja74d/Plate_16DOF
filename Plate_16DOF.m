clear all
clc
Lx=2; Ly=2; h=1; E=10.92; nu=0.3;
Nex=20; Ney=20; %number of elements in x and y directions
p0=1; ro=7.85;
BCleft='S'; BCtop='S'; BCright='S'; BCbottom='S';
%---------------------------SHAPE FUNCTIONS--------------------------------

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

%--------------------------ELEMENT MATRICES--------------------------------
B=[-1*diff(N,x,2); -1*diff(N,y,2); -2*diff(diff(N,x),y)];
d=E*h^3/12/(1-nu^2); D=d*[1, nu, 0; nu, 1, 0; 0, 0, (1-nu)/2];

WW=[0.568889, 0.478629, 0.478629, 0.236927, 0.236927]; %gauss point weight
XX=[0, 0.538469, -0.538469, 0.90618, -0.90618]; %gauss point cordinates
ke = zeros(16, 16); kgxe = zeros(16, 16); kgye = zeros(16, 16);
me = zeros(16, 16); fe = zeros(16, 1);

for i=1:5
    for j=1:5
        ke=ke+a*b/4*WW(i)*WW(j)*double(subs(subs(B'*D*B,x,0.5*a*XX(i)+...
            0.5*a),y,0.5*b*XX(j)+0.5*b));
        fe=fe+a*b/4*WW(i)*WW(j)*double(subs(subs(p0*N',x,0.5*a*XX(i)+...
            0.5*a),y,0.5*b*XX(j)+0.5*b));
        me=me+a*b/4*WW(i)*WW(j)*double(subs(subs(ro*h*N'*N,x,0.5*a*XX(i)+...
            a*XX(i)+0.5*a),y,0.5*b*XX(j)+0.5*b));

    end
end

disp((ke^-1)*fe)

%------------RESTRAINED DOFs-----------------------------------------------

if BCleft == 'S'
    for i=1:Ney+1
        resL(3*i-2)=(i-1)*4*(Nex+1)+1;
        resL(3*i-1)=(i-1)*4*(Nex+1)+2;
        resL(3*i)=(i-1)*4*(Nex+1)+4;
    end
end

if BCleft == 'C'
    for i =1:Ney+1
        resL(4*i-3)=(i-1)*4*(Nex+1)+1;
        resL(4*i-2)=(i-1)*4*(Nex+1)+2;
        resL(4*i-1)=(i-1)*4*(Nex+1)+3;
        resL(4*i)=(i-1)*4*(Nex+1)+4;
    end
end

if BCleft == 'F'
    resL=[];
end
if BCtop == 'S'
    for i=1:Nex+1
        resT(3*i-2)=4*i-3;
        resT(3*i-1)=4*i-1;
        resT(3*i)=4*i;
    end
end

if BCtop == 'C'
    for i=1:4*(Nex+1)
        resT(i)=i;
    end
end

if BCtop == 'F'
    rest=[];
end

if BCright == 'S'
    for i=1:Ney+1
        resR(3*i-2)=i*4*(Nex+1)-3;
        resR(3*i-1)=i*4*(Nex+1)-2;
        resR(3*i)=i*4*(Nex+1);
    end
end

if BCright == 'C'
    for i=1:Ney+1
        resR(4*i-3)=i*4*(Nex+1)-3;
        resR(4*i-2)=i*4*(Nex+1)-2;
        resR(4*i-1)=i*4*(Nex+1)-1;
        resR(4*i)=i*4*(Nex+1);
    end
end

if BCright == 'F'
    resR=[];
end

if BCbottom == 'S'
    for i=1:Nex+1
        resB(3*i-2)=4*i-3+4*(Nex+1)*Ney;
        resB(3*i-1)=4*i-1+4*(Nex+1)*Ney;
        resB(3*i)=4*i+4*(Nex+1)*Ney;
    end
end

if BCbottom == 'C'
    for i=1:4*(Nex+1)
        resB(i)=i+4*(Nex+1)*Ney;
    end
end

if BCbottom == 'F'
    resB=[];
end

res=sort([resL, resT, resR, resB]);
sizeres=size(res);
for i=1:sizeres(2)-1
    if i<sizeres(2)
        if res(i)==res(i+1)
            res=[res(1:i),res(i+1:sizeres(2))];
            sizeres=size(res);
            i=i-1;
        end
    end
end


%-----------------CODE TABLE-----------------------------------------------
for j=1:Ney
    for i=1:Nex
        ne=(j-1)*Nex+i;
        for k=1:8
            code(ne,k)=(j-1)*4*(Nex+1)+4*(i-1)+k;
        end
        for k=1:4
            code(ne, k+8)=j*4*(Nex+1)+4*(i-1)+k;
        end
        for k=1:4
            code(ne, k+12)=j*4*(Nex+1)+4*(i-1)+k;
        end
    end
end
sizeres=size(res);
for k=sizeres(2):-1:1
    for j=1:Nex*Ney
        for i=1:16
            if code(j,i)==res(k)
                code(j,i)=0;
            end
            if code(j,i)>res(k)
                code(j,i)=code(j,i)-1;
            end
        end
    end
end

%---------------------ASSEMBLING-------------------------------------------

K=zeros(max(code(:)), max(code(:)));F=zeros(max(code(:)),1);

for i=1:16
    if code(i,j)~=0
        for k=1:16
            if code(i,k)~=0
                K(code(i,j), code(i,k))=K(code(i,j),code(i,k))+ke(j,k);
            end
        end
        F(code(i,j),1)=F(code(i,j),1)+fe(j,1);
    end
end



















