vector = [10, -2]

function [result] = unitVec(vec)
  if or(rows(vec) == sum(vec == 0), columns(vec) == sum(vec == 0))
    result = vec;
  else
    result = vec./sqrt(sum(vec.^2));
  endif
endfunction

result = unitVec(vector);


display(result);
