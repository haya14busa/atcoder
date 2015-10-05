cat > input.txt
cat <<EOF >script.vim
function! s:brute_force(xs, n) abort
  if a:n < 2
    return a:xs
  endif

  let rs = []

  for x in a:xs
    let rs += map(copy(s:brute_force(a:xs, a:n - 1)), 'x . v:val')
  endfor

  return rs
endfunction

function! s:main(input) abort
  let n = a:input[0]
  return join(s:brute_force(['a', 'b', 'c'], n), "\n")
endfunction




let s:input = getline(1, '$')
% delete _
let s:output = s:main(s:input)

put =s:output
1 delete _
write! output.txt
qa!
EOF

vim -u NONE -i NONE -N -n -e -s -S script.vim input.txt

cat output.txt

rm input.txt script.vim output.txt

