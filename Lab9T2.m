# CS2613: Lab 9
# Starter Code

disp("");
function [charCounts] = countLetters(string)
  string = tolower(string);
  charCounts = zeros(1, 26);
  for i = 1:length(string)
  if isalpha(string(i))
    ++charCounts(double(string(i))-96);        
  endif
  endfor
endfunction


function retval = starterFunction()
	inputFile = fopen ("Input.txt", "r");
  	retval = {};
	while (!feof (inputFile))
	    line = fgetl(inputFile);
            charCounts = countLetters(line);
            [x, ix] = max(charCounts);
	    if(length(retval) == 0)
		    retval(1, 1) = char(ix+96);
		    retval(1, 2) = x;
	    else
	            retval(length(retval)+1, 1) = char(ix+96);
		    retval(length(retval), 2) = x;
		end
	end
	retval(2, :) = [];
end

disp(starterFunction());

