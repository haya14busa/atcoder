vim -u NONE -i NONE -N -n -e -s -S <(cat <<EOF
function! s:main(input) abort

  let [n, m] = split(a:input[0], ' ')
  let [x, y] = split(a:input[1], ' ')
  let as = split(a:input[2], ' ')
  let bs = split(a:input[3], ' ')

  let r1 = 0
  let ct = 0

  let flag = 1
  echo as
  echo bs
  " echo '='
  " echo 'x, y:' . x . ', ' . y
  while flag
    echo '--'
    echo 'ct: ' . ct
    " a -> b
    let ai = s:find(as, ct)
    if ai == -1
      break
    endif
    let ct = as[ai] + x
    echo 'ct: ' . ct
    " let as = as[ai+1:]
    let as = as[ai+1:]
    " b -> c
    let bi = s:find(bs, ct)
    if bi == -1
      break
    endif
    let ct = bs[bi] + y
    let bs = bs[bi+1:]
    let r1 += 1 
  endwhile
  return r1
endfunction

function! s:find(xs, x) abort
  if empty(a:xs)
    return -1
  endif

  let l = 1
  let r = len(a:xs) - 1
  let i = r
  if a:xs[-1] < a:x
    return -1
  endif

  if a:xs[0] >= a:x
    return 0
  endif

  while ! (a:xs[i - 1] <= a:x && a:x <= a:xs[i])
    if a:x < a:xs[i-1]
      let r = (l + r) / 2
      let i = r
    else
      let l = (l + r) / 2
      let i = l
    endif
  endwhile
  return i
endfunction

" echo s:find([1, 3, 4, 5], 2)
" echo s:find([1, 3, 4, 5], 5)
" echo s:find([1, 3, 4, 5], 6)
" echo s:find([1, 3, 4, 5], 1)
"
" echo s:main([])

function! s:test() abort
  " echo s:main([
  " \ '3 4',
  " \ '2 3',
  " \ '1 5 7',
  " \ '3 8 12 13'
  " \ ])
  "
  " echo s:main([
  " \ '1 1',
  " \ '1 1',
  " \ '1',
  " \ '1',
  " \ ])

  echo s:main([
  \ '6 7',
  \ '5 3',
  \ '1 7 12 19 20 26',
  \ '4 9 15 23 24 31 33',
  \ ])
endfunction

call s:test()

let s:input = getline(1, '$')
enew
put =s:main(s:input)
1 delete _
%print
EOF
) <(cat)
