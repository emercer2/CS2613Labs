vector = [8, 10, 12, 14]

function [result] = unitVec(vec)
  if or(rows(vec) == sum(vec == 0), columns(vec) == sum(vec == 0))
    result = vec;
  else
    result = vec./sqrt(sum(vec.^2));
  endif
endfunction

num = input("How many values would you like to input? ");
vars = NaN(1, num);
for i=1:num
	vars(i) = input("");
endfor

result = unitVec(vars);
disp(result);
