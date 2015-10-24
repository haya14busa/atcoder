vim -u NONE -i NONE -N -n -e -s -S <(cat <<EOF
function! s:main(input) abort
  let [n, m] = split(a:input[0], ' ')
  let l = (360 / 12) * (n % 12) + (360 / 12) * (m / 60.0)
  let s = (360 / 60) * m
  let r = abs(l - s)
  if r > abs(360 - r)
    return abs(360 - r)
  else
    return r
  endif
endfunction

function! s:test() abort
  let cases = [
  \   [ ['15 0'], '90'],
  \   [ ['3 17'], '3.5'],
  \   [ ['0 0'], '0'],
  \   [ ['6 0'], '180'],
  \   [ ['23 59'], '5.5000'],
  \   [ ['1 0'], '30'],
  \   [ ['2 0'], '60'],
  \   [ ['12 0'], '0'],
  \   [ ['13 0'], '30'],
  \   [ ['23 0'], '30'],
  \   [ ['9 0'], '90'],
  \   [ ['0 30'], '165.0'],
  \ ]

  for case in cases
    let [in, want] = case
    let got = string(s:main(in))
    echo printf('in: %s, want: %s, got: %s', string(in), want, got)
    unlet case
  endfor
endfunction

call s:test()
 
let s:input = getline(1, '$')
enew
put =s:main(s:input)
1 delete _
%print
EOF
) <(cat)
