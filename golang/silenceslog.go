package snippets

import (
	"io"
	"log/slog"
)

// SuppressSlog demonstrates the way of disabling slog output completely
// e.g. in case of tests and benchmarks.
func SuppressSlog() {
	log := slog.New(
		slog.NewTextHandler(io.Discard, nil),
	)
	log.Info("Prints nothing")
}
