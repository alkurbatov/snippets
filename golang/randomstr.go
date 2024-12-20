package snippets

import (
	"crypto/rand"
	"fmt"
)

// entropySize count of bytes for generation of random symbol sequences.
// The length is taken from recommendations in
// // https://pkg.go.dev/golang.org/x/crypto/sha3#hdr-Recommendations
const entropySize = 32

const base32alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

var SecureRandString = NewRandString(entropySize, base32alphabet)

// NewRandString generates secure random string that can be used e.g. as state or nonce.
// In Golang 1.24+ use https://pkg.go.dev/crypto/rand@master#Text
// NewRandString генерирует случайную строку.
func NewRandString(length uint, alphabet string) string {
	if length == 0 {
		panic("zero length random string requested")
	}

	l := len(alphabet)

	// NB (alkurbatov): Based on https://pkg.go.dev/crypto/rand@master#Text
	src := make([]byte, length)
	if _, err := rand.Read(src); err != nil {
		panic(fmt.Errorf("read random bytes: %w", err))
	}

	for i := range src {
		src[i] = alphabet[int(src[i])%l]
	}

	return string(src)
}
