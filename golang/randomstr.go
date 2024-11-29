package snippets

import (
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
)

// entropySize count of bytes for generation of random symbol sequences.
const entropySize = 24

// GenerateString generates secure random string that can be used e.g. as state or nonce.
func GenerateString() (string, error) {
	data := make([]byte, entropySize)
	if _, err := rand.Read(data); err != nil {
		return "", err
	}

	sum := sha256.Sum256(data)

	return hex.EncodeToString(sum[:]), nil
}
