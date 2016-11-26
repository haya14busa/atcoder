package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	if false {
		test()
	} else {
		solve(os.Stdin, os.Stdout)
	}
}

func solve(r io.Reader, w io.Writer) {
	var n int // number of participants
	var m int // number of languages
	fmt.Fscanln(r, &n, &m)

	g := make(map[int][]int)

	for i := 0; i < n; i++ {
		var langs int
		fmt.Fscan(r, &langs)
		g[i] = make([]int, 0, langs)
		for j := 0; j < langs; j++ {
			var lang int
			fmt.Fscan(r, &lang)
			langi := n + lang - 1
			g[i] = append(g[i], langi)
			g[langi] = append(g[langi], i)
		}
	}

	seen := make([]bool, n+m)
	q := []int{0}
	for len(q) > 0 {
		v := q[0]
		q = q[1:]
		if !seen[v] {
			seen[v] = true
			q = append(q, g[v]...)
		}
	}

	for i := 0; i < n; i++ {
		if !seen[i] {
			fmt.Fprintln(w, "NO")
			return
		}
	}
	fmt.Fprintln(w, "YES")
	return
}

func test() {
	tests := []struct {
		in   string
		want string
	}{
		{
			in: `4 6
3 1 2 3
2 4 2
2 4 6
1 6`,
			want: `YES
`,
		},
		{
			in: `4 4
2 1 2
2 1 2
1 3
2 4 3`,
			want: `NO
`,
		},
	}
	for i, tt := range tests {
		fmt.Printf("=== TEST %d\n", i)
		buf := new(bytes.Buffer)
		solve(strings.NewReader(tt.in), buf)
		if got := buf.String(); got != tt.want {
			fmt.Printf("%d: got %v, want %v\n", i, got, tt.want)
		}
	}
}
