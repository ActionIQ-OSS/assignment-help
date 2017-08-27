// Read lines from a file:

let file = File::open(“foo”)?;
let reader = BufReader::new(file);
for l in reader.lines() {
    println!(“{}”, l.expect("could not parse line"));
}

// https://doc.rust-lang.org/std/io/struct.BufReader.html


// List files in a directory:

let  = fs::read_dir("./").unwrap();

// https://doc.rust-lang.org/std/fs/


// Match a line against a regex:

let re = Regex::eew(r".*").expect(“should be a valid regex”);
re.is_match("foo");

// https://doc.rust-lang.org/regex/regex/index.html


// Build an http-based client/server:

// JSON: https://docs.serde.rs/serde_json/
// WebApp: https://rocket.rs/
// Http Client: https://hyper.rs/
