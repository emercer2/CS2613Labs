#hello
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

disp(countLetters("Hello Programming Languages Lab!"));
