package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path/filepath"
	"runtime"
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
	var n, a int
	fmt.Fscanln(r, &n, &a)
	dp := make(map[int]int)
	for i := 0; ; i++ {
		max := i
		if x := dp[i-3-a]; x*3 > max {
			max = x * 3
		}
		dp[i] = max
		fmt.Println(i, max)
		if max >= n {
			fmt.Fprintln(w, i)
			return
		}
	}
}

func test() {
	tests := []struct {
		in   string
		want string
	}{
		{in: `8 1`, want: `7`},
		// {in: `1000000000000 1000000000000`, want: `1000000000000`},
		// {in: `10 10`, want: `10`},
		// {in: `100 0`, want: `13`},
		// {in: `100 1`, want: `16`},
		// {in: `100 2`, want: `19`},
		// {in: `100 3`, want: `22`},
		// {in: `100 4`, want: `25`},
		// {in: `100 5`, want: `28`},
		// {in: `100 6`, want: `30`},
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
		_, file, line, ok := runtime.Caller(1)
		if ok {
			f, _ := os.Open(file)
			defer f.Close()
			s := bufio.NewScanner(f)
			lnum := 0
			for s.Scan() {
				lnum++
				if lnum == line {
					wd, _ := os.Getwd()
					fname, _ := filepath.Rel(wd, file)
					fmt.Printf("assertion fails: %s:%d: %v\n", fname, line, s.Text())
					break
				}
			}
		}
	}
}

func pow(a, b int) int {
	r := 1
	for i := 0; i < b; i++ {
		r *= a
	}
	return r
}
