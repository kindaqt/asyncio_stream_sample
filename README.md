# Code Sample

## Prompt

My engineers indicate this should take between 3-5 hours. If he uses Google correctly, many pointers are online; for an experienced developer such as himself, this shouldn't be an issue.

- [ ] Set up two local Python servers.
- [ ] On one of the servers, over the course of 10 minutes, generate 100 binary files of random sizes ranging from 1kb to 1Mb at random time intervals ranging from 1ms to 1s, encoded int16.
  - [ ] takes 10 minutes
  - [ ] generate 100 binary files
  - [ ] files generated in a time interval of 1ms to 1s
  - [ ] file contains random int16
- [ ] Transfer those binary files as they are being generated from the first server to the second server over HTTP using Python's async io functionality, thereby effectively implementing data streaming from one server to the other.
  - [ ] HTTP Streaming
- [ ] Provide a GH repo of your code.
