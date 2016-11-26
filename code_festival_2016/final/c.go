package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	// if true {
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
			planet[i][lang] = true
		}
	}

	if communicatable(planet, n) {
		fmt.Fprintln(w, "YES")
	} else {
		fmt.Fprintln(w, "NO")
	}
}

func communicatable(planet map[int]map[int]bool, n int) bool {
	// p1 -> p2 -> bool
	table := make(map[int]map[int]bool)
	for i := 0; i < n; i++ {
		table[i] = make(map[int]bool)
	}

	for p1, langs1 := range planet {
	P:
		for p2, langs2 := range planet {
			if !(p1 < p2) {
				continue P
			}
			for l2 := range langs2 {
				if _, ok := langs1[l2]; ok {
					table[p1][p2] = true
					table[p2][p1] = true
					continue P
				}
			}
		}
	}

	seen := make([]bool, n)
	traverse(table, 0, seen)
	for i := 0; i < n; i++ {
		if !seen[i] {
			return false
		}
	}
	return true
}

func traverse(g map[int]map[int]bool, i int, seen []bool) {
	seen[i] = true
	for v := range g[i] {
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
