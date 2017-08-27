Read lines from a file:

Source.fromFile(“foo”).foreach { print }

http://www.scala-lang.org/api/2.12.1/scala/io/Source$.html

Match a line against a regex:

val re = raw”.*”.r
re.findAllIn(“line to search”).start

https://www.scala-lang.org/api/current/scala/util/matching/Regex.html

List files in a directory:

import java.io.File
def recursiveListFiles(f: File): Array[File] = {
    val these = f.listFiles
      these ++ these.filter(_.isDirectory).flatMap(recursiveListFiles)
}

https://stackoverflow.com/questions/2637643/how-do-i-list-all-files-in-a-subdirectory-in-scala

Build an http-based client/server:

WebApp: https://www.playframework.com/
Http Library: https://github.com/http4s/http4s
