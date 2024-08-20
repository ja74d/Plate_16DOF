clear all
clc

[d, w] = GaussQuad1(3); % Call the function

% Function definitions start here
function [d ,w] = GaussQuad1(n, s0, s1)
  if nargin==1
    s0=-1; s1=1;
  end

  if n==1
    d=(s0+s1)/2; w=s1-s0; return;
  end

  j=1:n-1;
  bta=j./sqrt(4*j.^2-1);
  Q=diag(bta, -1)+diag(bta, 1); % Fix: Corrected "beta" to "bta"

  [U, L] = eig(Q);
  [d, k] = sort(diag(L));
  w = 2*U(1, k).^2;
  w=w(:);
  d=s0+0.5*(s1-s0)*(d+1);

  disp([w, d]); % Fix: disp only takes one argument
end


