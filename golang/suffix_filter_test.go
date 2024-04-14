package snippets_test

import (
	"regexp"
	"strings"
	"testing"
)

var testInput = [...]string{
	"/grpc.reflection.v1.ServerReflection/ServerReflectionInfo",
	"/AudioRecorder/AddRecognizeRequestData",
	"/asr_e2e_agent.v1.Agent/GetModelsInfo",
	"/mts.ai.audiogram.tracing.examples.v1.Example/StreamStream",
}

var ignoredMethods = regexp.MustCompile(`(Health/Check|ServerReflection/ServerReflectionInfo)$`)

func filterHasSuffix(method string) bool {
	return strings.HasSuffix(method, "Health/Check") || strings.HasSuffix(method, "ServerReflection/ServerReflectionInfo")
}

func BenchmarkRegexp(b *testing.B) {
	var ret bool

	for n := 0; n < b.N; n++ {
		for _, method := range testInput {
			ret = ignoredMethods.MatchString(method)
		}
	}

	_ = ret
}

func BenchmarkHasSuffix(b *testing.B) {
	var ret bool

	for n := 0; n < b.N; n++ {
		for _, method := range testInput {
			ret = filterHasSuffix(method)
		}
	}

	_ = ret
}
