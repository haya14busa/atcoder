cat > input.txt
cat <<EOF >script.vim
function! s:main(input) abort
  return len(filter(a:input, "stridx(v:val, 'r') != -1"))
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
