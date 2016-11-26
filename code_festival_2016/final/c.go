package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	if true {
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

	// lang1 -> lang2 -> bool where lang1 < lang2
	transtable := make(map[int]map[int]bool)

	for _, langs := range planet {
		for lang1 := range langs {
			for lang2 := range langs {
				if lang1 == lang2 {
					continue
				}
				l1, l2 := lang1, lang2
				if lang1 > lang2 {
					l1, l2 = lang2, lang1
				}
				if _, ok := transtable[l1]; !ok {
					transtable[l1] = make(map[int]bool)
				}
				transtable[l1][l2] = true
			}
		}
	}
	if communicatable(planet, transtable) {
		fmt.Fprintln(w, "YES")
	} else {
		fmt.Fprintln(w, "NO")
	}
}

func communicatable(planet map[int]map[int]bool, transtable map[int]map[int]bool) bool {
	for p1, langs1 := range planet {
	P:
		for p2, langs2 := range planet {
			if !(p1 < p2) {
				continue P
			}
			for l1 := range langs1 {
				if _, ok := langs2[l1]; ok {
					continue P
				}
				for l2 := range langs2 {
					if l1 == l2 {
						continue
					}
					from, to := l1, l2
					if l1 > l2 {
						from, to = l2, l1
					}
					if t, ok := transtable[from]; ok {
						if _, ok := t[to]; ok {
							continue P
						}
					}
				}
			}
			fmt.Println(p1, p2)
			return false
		}
	}
	return true
}

func genRange(i, j int) []int {
	rs := make([]int, 0, j-i)
	for ; i < j; i++ {
		rs = append(rs, i)
	}
	return rs
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
