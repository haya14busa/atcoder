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
	var n int
	fmt.Fscanln(r, &n)
	for _, p := range problems(n) {
		fmt.Fprintln(w, p)
	}
}

func problems(n int) []int {
	for max := 1; max <= n; max++ {
		s := sum(max)
		if s < n {
			continue
		} else if s == n {
			return genRange(1, max+1)
		}
		rs := make([]int, 0, max-1)
		for i := 1; i <= max; i++ {
			if s-i == n {
				continue
			}
			rs = append(rs, i)
		}
		return rs
	}
	return nil
}

func genRange(i, j int) []int {
	rs := make([]int, 0, j-i)
	for ; i < j; i++ {
		rs = append(rs, i)
	}
	return rs
}

func sum(max int) int {
	r := 0
	for i := 1; i <= max; i++ {
		r += i
	}
	return r
}

func test() {
	tests := []struct {
		in   string
		want string
	}{
		{
			in: "4",
			want: `1
3
`,
		},
		{
			in: "7",
			want: `1
2
4
`,
		},
		{
			in: "1",
			want: `1
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
