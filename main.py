equations_cnt, vars_cnt = [int(i) for i in input().split()];

#read data
input_str = [];
matrix = [];
for i in range(equations_cnt):
  input_str = [int(i) for i in input().split()];
  matrix.append(input_str);

for j in range(vars_cnt):
  #last equation
  i = equations_cnt - 1;
  while i > j:    
    #if first coef or first eq is 0
    if matrix[j][j] == 0:
      is_find_not_null = 0;
      for not_null_index in range(j, vars_cnt):
        if matrix[not_null_index][j] != 0:
          prom = matrix[not_null_index];
          matrix[not_null_index] = matrix[j];
          matrix[j] = prom;
          is_find_not_null = 1;
      if is_find_not_null == 0:
        print('INF');
        exit();   
    #subtract rows
    if matrix[i][j] != 0:
      if matrix[i][j] == matrix[j][j]:
        first = matrix[j];
        current = matrix[i];
      else:
        first = [a * matrix[i][j] for a in matrix[j]];
        current = [a * matrix[j][j] for a in matrix[i]];
      matrix[i] = [a-b for a, b in zip(first, current)];
    #0 + 0 + .. + 0 = b; b != 0
    if matrix[i][0:vars_cnt] == [0]*(vars_cnt):
      if matrix[i][vars_cnt] == 0:
        del matrix[i];
        vars_cnt -= 1;
      else:
        print('NO');
        exit();
    i -= 1;

if equations_cnt < vars_cnt:
  print('INF');
  exit();

res = [];
for i in range(1,equations_cnt+1):
  prom = 0;
  for j in range(1,i):
    prom += matrix[equations_cnt-i][vars_cnt-j] * res[j-1];

  x = (matrix[equations_cnt-i][vars_cnt] - prom)/matrix[equations_cnt-i][vars_cnt-i];
  res.append(x);
  
print('YES');
for i in res[::-1]:
  print(i, end = ' ');