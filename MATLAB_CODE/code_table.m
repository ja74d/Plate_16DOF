% Initialize empty arrays for boundary restraints
resL = [];
resT = [];
resR = [];
resB = [];

% Boundary Conditions (Left)
if BCleft == 'S'
    for i = 1:Ney+1
        resL = [resL, (i-1)*4*(Nex+1) + [1, 2, 4]];
    end
elseif BCleft == 'C'
    for i = 1:Ney+1
        resL = [resL, (i-1)*4*(Nex+1) + [1, 2, 3, 4]];
    end
end

% Boundary Conditions (Top)
if BCtop == 'S'
    for i = 1:Nex+1
        resT = [resT, 4*i - [3, 1, 0]];
    end
elseif BCtop == 'C'
    resT = 1:4*(Nex+1);
end

% Boundary Conditions (Right)
if BCright == 'S'
    for i = 1:Ney+1
        resR = [resR, i*4*(Nex+1) - [3, 2, 0]];
    end
elseif BCright == 'C'
    for i = 1:Ney+1
        resR = [resR, i*4*(Nex+1) - [3, 2, 1, 0]];
    end
end

% Boundary Conditions (Bottom)
if BCbottom == 'S'
    for i = 1:Nex+1
        resB = [resB, 4*i - [3, 1, 0] + 4*(Nex+1)*Ney];
    end
elseif BCbottom == 'C'
    resB = (1:4*(Nex+1)) + 4*(Nex+1)*Ney;
end

% Combine and sort restrained DOFs, then remove duplicates
res = unique([resL, resT, resR, resB]);

%-----------------CODE TABLE-----------------------------------------------
code = zeros(Ney*Nex, 16);
for j = 1:Ney
    for i = 1:Nex
        ne = (j-1)*Nex + i;  % Element number
        % Assign global DOFs for each element
        code(ne, 1:8) = (j-1)*4*(Nex+1) + 4*(i-1) + (1:8);
        code(ne, 9:12) = j*4*(Nex+1) + 4*i + (1:4);
        code(ne, 13:16) = j*4*(Nex+1) + 4*(i-1) + (1:4);
    end
end

% Perform DOF reduction
for k = length(res):-1:1
    code(code == res(k)) = 0;
    code(code > res(k)) = code(code > res(k)) - 1;
end

disp(code)
