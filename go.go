// Read lines from a file:

file, _ := os.Open(‘foo’)
defer file.Close()

scanner := bufio.NewScanner(file)
for scanner.Scan() {
  line := scanner.Text()
  fmt.Println(line)
}

// https://golang.org/pkg/bufio/


// List files in a directory:

files, _ := ioutil.ReadDir("./")
for _, f := range files {
  // ...
}

// https://golang.org/pkg/io/ioutil/#ReadDir


// Match a line against a regex:

matched, err := regexp.MatchString(".*", "line to match")

// https://golang.org/pkg/regexp/


// Build an http-based client/server:

// JSON: https://golang.org/pkg/encoding/json/
// WebApp: https://golang.org/pkg/net/http/#Serve
// Http Client: https://golang.org/pkg/net/http/
