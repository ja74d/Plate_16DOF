clear all
clc

function [d ,w] = GaussQuad(n, s0, s1)
  if nargin == 1
    s0=-1; s1=1;
  endif

  if nargin < 1
    n=2;
  endif

  if n==1
    d=(s0+s1)/2;w=s1-s0; return;
  endif
  j=1:n-1; bta=j./sqrt(4*j.^2-1); Q=diag(beta, -1)+diag(bta, 1);
  [U, L] = eig(Q);
  [U, K] = sort(diag(L));
  w = 2*U(1, k).^2;w=w(:);
  d=s0+0.5*(s1-s0)*(d+1);
end

[d, w] = GaussQuad(4);
