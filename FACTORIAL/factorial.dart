factorial(int x) {
  if (x == 1 || x == 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
//5*4*3*2*1

loopedFactorial(int x) {
  int result = 1;
  for (var i = 1; i <= x; i++) {
    result *= i;
  }
  return result;
}

void main() {
  print(factorial(10));
  print(loopedFactorial(5));
}
