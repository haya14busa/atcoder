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
	max := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(r, &x)
		xcnt[x]++
		if x > max {
			max = x
		}
	}

	max = max * 2

	pairNum := 0

	for i := 1; m*i <= max; i++ {
		mi := m * i
		for x, cnt := range xcnt {
			if cnt < 1 {
				delete(xcnt, x)
				continue
			}
			want := mi - x
			if want < 1 || (x == want) || cnt > 1 {
				continue
			}
			if c, ok := xcnt[want]; ok && c > 0 {
				xcnt[x]--
				xcnt[want]--
				pairNum++
				fmt.Println("pair", x, want)
			}
		}
	}

	for x, cnt := range xcnt {
		if cnt > 1 {
			pairNum += cnt / 2
			fmt.Println("pair", x, x, " x ", cnt/2)

			if cnt%2 == 1 {
				for i := 1; m*i <= max; i++ {
					mi := m * i
					want := mi - x
					if want < 1 {
						continue
					}
					if c, ok := xcnt[want]; ok && c > 0 {
						xcnt[x]--
						xcnt[want]--
						pairNum++
						fmt.Println("pair", x, want)
						break
					}
				}
			}
		}
	}

	fmt.Fprintln(w, pairNum)
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
