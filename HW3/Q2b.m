syms cbar lamdbda

cbar = sym('cbar');
lambda = sym('lambda');

A = [1/3*cbar-lamdbda,1/3*cbar,1/3*cbar,1/3*cbar;
    2/3*cbar,2/3*cbar-lamdbda,2/3*cbar,2/3*cbar;
    cbar,cbar,cbar-lamdbda,cbar;
    4/3*cbar,4/3*cbar,4/3*cbar,4/3*cbar-lamdbda];

det(A)