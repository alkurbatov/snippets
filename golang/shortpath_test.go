// Extract short path in form parent/filename.
package snippets

import (
	"path/filepath"
	"testing"
)

func trimPath(src string) string {
	dir, file := filepath.Split(src)
	return filepath.Base(dir) + "/" + file
}

func BenchmarkTrimPath(b *testing.B) {
	var ret string

	for n := 0; n < b.N; n++ {
		ret = trimPath("aaa/bbb/parent/file.go")
	}

	_ = ret
}
