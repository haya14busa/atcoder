package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"math"
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
	time := n
	// k-1: count of eating cookies.
	// k <= log2(n) because
	//   - shortest eating interval is 2
	for k := 1; k <= int(math.Ceil(math.Log2(float64(n)))); k++ {
		// s: average number of eating interval
		s := int(math.Ceil(math.Pow(float64(n), 1/float64(k))))
		assert(pow(s, k) >= n)
		c := 0              // the number of "s" interval
		for ; c <= k; c++ { // TODO: binary search should be better
			if n <= pow((s-1), (k-c))*pow(s, c) {
				break
			}
		}
		if t := (k-1)*a + s*c + (s-1)*(k-c); t < time {
			// fmt.Println(strings.Join(procedure(s, k, c), ""))
			time = t
		}
	}
	fmt.Fprintln(w, time)
}

func procedure(s, k, c int) []string {
	ps := make([]string, 0, (s-1)*(k-c)+s*c+(k-1))
	for i := 0; i < k-c; i++ {
		if i != 0 {
			ps = append(ps, "E")
		}
		for j := 0; j < s-1; j++ {
			ps = append(ps, "B")
		}
	}
	for i := 0; i < c; i++ {
		if len(ps) > 0 {
			ps = append(ps, "E")
		}
		for j := 0; j < s; j++ {
			ps = append(ps, "B")
		}
	}
	return ps
}

func test() {
	tests := []struct {
		in   string
		want string
	}{
		{in: `8 1`, want: `7`},
		{in: `1000000000000 1000000000000`, want: `1000000000000`},
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
