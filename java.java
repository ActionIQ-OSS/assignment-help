// Read lines from a file:

BufferedReader br = new BufferedReader(new FileReader(“foo”));  
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}

// https://docs.oracle.com/javase/7/docs/api/java/io/BufferedReader.html


// List files in a directory:

File folder = new File("./");
File[] files = folder.listFiles();


// Match a line against a regex: 

boolean matched = Pattern.matches(“.*”, “line to search”);

// https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html


// Build an http-based client/server:

// JSON: https://github.com/FasterXML/jackson-jr
// Webapp: http://www.dropwizard.io/1.1.4/docs/
// Http Library: https://hc.apache.org/httpcomponents-client-ga/index.html
