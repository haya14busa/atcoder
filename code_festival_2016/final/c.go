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
	// planet: paticipant -> lang -> bool
	planet := make(map[int]map[int]bool)
	for i := 0; i < n; i++ {
		planet[i] = make(map[int]bool)
		var langs int
		fmt.Fscan(r, &langs)
		for j := 0; j < langs; j++ {
			var lang int
			fmt.Fscan(r, &lang)
			planet[i][lang-1] = true
		}
	}

	if communicatable(planet, n, m) {
		fmt.Fprintln(w, "YES")
	} else {
		fmt.Fprintln(w, "NO")
	}
}

func communicatable(planet map[int]map[int]bool, n, m int) bool {
	g := make(map[int][]int)
	for i := 0; i < n+m; i++ {
		g[i] = make([]int, 0)
	}

	for p, langs := range planet {
		g[p] = make([]int, len(langs))
		for l := range langs {
			// fmt.Println("p", p)
			// fmt.Println("n+l", n+l)
			langi := n + l
			g[p] = append(g[p], langi)
			g[langi] = append(g[langi], p)
		}
	}

	seen := make([]bool, n+m)
	traverse(g, 0, seen)
	for i := 0; i < n; i++ {
		if !seen[i] {
			return false
		}
	}
	return true
}

func traverse(g map[int][]int, i int, seen []bool) {
	seen[i] = true
	for _, v := range g[i] {
		if !seen[v] {
			traverse(g, v, seen)
		}
	}
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
