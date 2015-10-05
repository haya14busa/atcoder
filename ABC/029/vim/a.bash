cat > input.txt
cat <<EOF >script.vim
function! s:main(input) abort
  return a:input[0] . 's'
endfunction

let s:input = getline(1, '$')
let s:output = s:main(s:input)

% delete _
put =s:output
1 delete _
write! output.txt
qa!
EOF

vim -u NONE -i NONE -N -n -e -s -S script.vim input.txt

cat output.txt
