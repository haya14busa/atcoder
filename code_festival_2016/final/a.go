package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	if false {
		test()
	} else {
		fmt.Println(solve(os.Stdin))
	}
}

func solve(r io.Reader) string {
	var h int
	var w int
	fmt.Fscanln(r, &h, &w)

	for i := 1; i <= h; i++ {
		for j := 0; j < w; j++ {
			var s string
			fmt.Fscan(r, &s)
			if s == "snuke" {
				return fmt.Sprintf("%s%d", string([]byte{byte(65 + j)}), i)
			}
		}
	}

	return ""
}

func test() {
	tests := []struct {
		in   string
		want string
	}{
		{
			in: `15 10
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snuke snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake`,
			want: "H6",
		},
		{
			in: `1 1
snuke`,
			want: "A1",
		},
	}
	for i, tt := range tests {
		if got := solve(strings.NewReader(tt.in)); got != tt.want {
			fmt.Printf("%d: got %v, want %v\n", i, got, tt.want)
		}
	}
}
