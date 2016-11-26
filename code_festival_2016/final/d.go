package main

import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"runtime/debug"
	"strings"
)

func main() {
	b, _ := ioutil.ReadAll(os.Stdin)
	if len(b) == 0 {
		test()
	} else {
		solve(bytes.NewReader(b), os.Stdout)
	}
}

func solve(r io.Reader, w io.Writer) {
	var n, m int
	fmt.Fscanln(r, &n, &m)
	cntByX := make(map[int]int)
	cntByMod := make(map[int]int)
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(r, &x)
		cntByX[x]++
		cntByMod[x%m]++
	}
	pairN := 0

	for mod := 0; mod <= m/2; mod++ {
		cnt := cntByMod[mod]
		if mod == 0 || (m%2 == 0 && mod == m/2) {
			pairN += cnt / 2
			cntByMod[mod] %= 2
			continue
		}
		that := m - mod
		assert(mod < that)
		if cnt > cntByMod[that] {
			cnt = cntByMod[that]
		}
		pairN += cnt
		cntByMod[mod] -= cnt
		cntByMod[that] -= cnt
	}

	for x, cnt := range cntByX {
		if cnt > 1 && cntByMod[x%m] > 1 {
			if cnt > cntByMod[x%m] {
				cnt = cntByMod[x%m]
			}
			c := cnt / 2
			pairN += c
			cntByMod[x%m] -= c * 2
		}
	}

	fmt.Fprintln(w, pairN)
}

func test() {
	tests := []struct {
		in   string
		want string
	}{
		{
			in: `
7 5
3 1 4 1 5 9 2
`,
			want: `3`,
		},
		{
			in: `
15 10
1 5 6 10 11 11 11 20 21 25 25 26 99 99 99
`,
			want: `6`,
		},
		{
			in: `
3 10
8 8 8
`,
			want: `1`,
		},
		{
			in: `
20 10
1 5 6 10 11 11 11 11 11 11 31 31 20 21 25 25 26 99 99 99
`,
			want: `8`,
		},
	}
	for i, tt := range tests {
		fmt.Printf("=== TEST %d\n", i)
		buf := new(bytes.Buffer)
		solve(strings.NewReader(chomp(tt.in)), buf)
		if got, want := chomp(buf.String()), chomp(tt.want); got != want {
			fmt.Printf("%d: got %v, want %v\n", i, got, want)
		}
	}
}

func chomp(s string) string {
	return strings.Trim(s, "\n")
}

func assert(b bool) {
	if !b {
		debug.PrintStack()
	}
}
