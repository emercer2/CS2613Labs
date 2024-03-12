f1 = @(x) idivide(int32(x .^ 2), 3, "fix") - 5;  
f2 = @(x) log(x + 1);
compareTo = @(x, y) x <= y;

function retval = compareListPositions(f1, f2, comp, values)
        retval = 0;
        for i = values
	  if comp(f1(i), f2(i)) != 0
           retval = retval + 1;
          endif
	endfor
endfunction

display(compareListPositions(f1, f2, compareTo, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
