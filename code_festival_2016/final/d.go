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

type RemCnt struct {
	Same map[int]int
	Diff int
	Num  int
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

	rm := make(map[int]*RemCnt)

	ones := make([]int, 0)

	for x, cnt := range xcnt {
		r := x % m
		if _, ok := rm[r]; !ok {
			rm[r] = &RemCnt{}
		}
		rm[r].Num += cnt
		if cnt > 1 {
			if rm[r].Same == nil {
				rm[r].Same = make(map[int]int)
			}
			rm[r].Same[x] += cnt
		} else {
			rm[r].Diff += cnt
			ones = append(ones, x)
		}
	}

	pairNum := 0
	for _, x := range ones {
		xm := x % m
		want := m - xm
		if m == want {
			want = 0
		}
		if xm == want {
			if rm[want].Diff > 1 {
				rm[want].Num -= 2
				rm[want].Diff -= 2
				pairNum++
				// fmt.Println("pair", x, "?")
			} else {
				y := -1
				for xthat, cnt := range rm[want].Same {
					y = xthat
					if cnt%2 == 1 {
						break
					}
				}
				if y != -1 {
					rm[want].Num -= 2
					rm[want].Diff--
					rm[want].Same[y]--
					pairNum++
					// fmt.Println("pair", x, y)
				}
			}
			continue
		}
		if c, ok := rm[want]; ok {
			if c.Diff > 0 {
				c.Num--
				c.Diff--
				rm[xm].Num--
				rm[xm].Diff--
				pairNum++
				// fmt.Println("pair", x, "?")
			} else {
				y := -1
				for xthat, cnt := range c.Same {
					y = xthat
					if cnt%2 == 1 {
						break
					}
				}
				if y != -1 {
					c.Num--
					c.Same[y]--
					rm[xm].Num--
					rm[xm].Diff--
					pairNum++
					// fmt.Println("pair", x, y)
				}
			}
		}
	}

	for x, c := range rm {
		if c.Num == 0 {
			delete(rm, x)
			continue
		}
		xm := x % m
		want := m - xm
		if m == want {
			want = 0
		}
		if cthat, ok := rm[want]; ok && cthat.Num > 0 {
			num := c.Num
			if num > cthat.Num {
				num = cthat.Num
			}
			plus := num / 2
			c.Num -= plus
			cthat.Num -= plus
			pairNum += plus
			// fmt.Printf("%d cthat: %#v\n", want, cthat)
		}
		if plus := (c.Num - c.Diff) / 2; plus > 0 {
			pairNum += plus
			c.Num -= plus * 2
			// fmt.Println("pair", x, x)
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
17 10
1 5 6 10 11 11 11 20 21 25 25 26 99 99 99 19 19
`,
			want: `7`,
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
