package snippets

import (
	"io"
	"log/slog"
)

// SuppressSlogBeforeGo124 demonstrates the Go <= 1.23 way of disabling slog output
// completely e.g. in case of tests and benchmarks.
func SuppressSlogBeforeGo124() {
	log := slog.New(
		slog.NewTextHandler(io.Discard, nil),
	)
	log.Info("Prints nothing")
}

// SuppressSlog demonstrates the way of disabling slog output completely
// e.g. in case of tests and benchmarks.
func SuppressSlog() {
	log := slog.New(slog.DiscardHandler)
	log.Info("Prints nothing")
}
