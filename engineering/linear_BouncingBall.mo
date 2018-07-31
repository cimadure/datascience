model linear_BouncingBall
  parameter Integer n = 2; // states
  parameter Integer k = 0; // top-level inputs
  parameter Integer l = 0; // top-level outputs
  parameter Real x0[2] = {0.04243354772883932,-0.5463586255138767};
  parameter Real u0[0] = {i for i in 1:0};
  parameter Real A[2,2] = [0,1;0,0];
  parameter Real B[2,0] = zeros(2,0);
  parameter Real C[0,2] = zeros(0,2);
  parameter Real D[0,0] = zeros(0,0);
  Real x[2](start=x0);
  input Real u[0];
  output Real y[0];

  Real 'x_h' = x[1];
Real 'x_v' = x[2];

equation
  der(x) = A * x + B * u;
  y = C * x + D * u;
end linear_BouncingBall;
