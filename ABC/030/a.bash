vim -u NONE -i NONE -N -n -e -s -S <(cat <<EOF
function! s:main(input) abort
  let [a, b, c, d] = map(split(a:input[0], ' '), 'str2float(v:val)')
  if (b / a) > (d / c)
    return 'TAKAHASHI'
  elseif (b / a) < (d / c)
    return 'AOKI'
  else
    return 'DRAW'
  endif
endfunction

let s:input = getline(1, '$')
enew
put =s:main(s:input)
1 delete _
%print
EOF
) <(cat)
