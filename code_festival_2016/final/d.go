package main

import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"os"
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
	xcnt := make(map[int]int, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(r, &x)
		xcnt[x]++
	}

	// by reminder
	// reminder -> x -> count
	xsbyrem := make(map[int]map[int]int)

	for x, cnt := range xcnt {
		rem := x % m
		if _, ok := xsbyrem[rem]; !ok {
			xsbyrem[rem] = make(map[int]int)
		}
		xsbyrem[rem][x] = cnt
	}

	pairNum := 0

	calced := make([]bool, m)

	for rem, cntByX := range xsbyrem {
		if calced[rem] {
			continue
		}
		calced[rem] = true
		want := m - rem
		if rem == 0 || rem == want {
			pairNum += sum(cntByX) / 2
			continue
		}
		if calced[want] {
			continue
		}
		calced[want] = true
		t := xsbyrem[want]
		if t == nil {
			t = make(map[int]int)
		}
		s := cntByX
		sNum := sum(cntByX)
		tNum := sum(t)
		if sNum < tNum {
			s, t = t, s
			sNum, tNum = tNum, sNum
		}
		for x, cnt := range s {
			if !(sNum > tNum+1) {
				break
			}
			if cnt > 1 {
				c := sNum - tNum
				if c > cnt {
					c = cnt
				}
				s[x] -= c
				sNum -= c
				pairNum += c / 2
			}
		}
		pairNum += tNum
	}

	fmt.Fprintln(w, pairNum)
}

func sum(m map[int]int) int {
	s := 0
	for _, c := range m {
		s += c
	}
	return s
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
