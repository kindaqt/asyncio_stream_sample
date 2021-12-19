# Code Sample

Hi reviewer! I've included the initial prompt as well as a checklist of things I needed to implement.

I wasn't quite sure about the int16 part of the prompt so I implemented functionality that creates a file of random int16s. Since int16 takes 2 bytes I generate files with a size that allows for 2 byte chunks. For example, the random file size might be 1023 in which case I increase the size by one. This way the files stay within the random limit. I didn't know what to do with the data once it hit the receiver so I just bundled it all up and printed it.

If I was to reimplement this I might create a buffer on the sender that accepts random ints. Then I would have 2 functions read from the buffer. One function would stream the data over to the receiver while the other function would save the data to files.

## Get Started

### 1. Start receiver

```
python ./receiver.py
```

### 2. Start sender

```
python ./sender.py
```

## Prompt

My engineers indicate this should take between 3-5 hours. If he uses Google correctly, many pointers are online; for an experienced developer such as himself, this shouldn't be an issue.

### Checklist

- [x] Set up two local Python servers.
  - [x] receiver server
  - [x] sender server
- [x] On one of the servers, over the course of 10 minutes, generate 100 binary files of random sizes ranging from 1kb to 1Mb at random time intervals ranging from 1ms to 1s, encoded int16.
  - [x] process takes less than 10 minutes
  - [x] generate 100 binary files
  - [x] files generated in a time interval of 1ms to 1s
  - [x] file contains random int16
- [x] Transfer those binary files as they are being generated from the first server to the second server over HTTP using Python's async io functionality, thereby effectively implementing data streaming from one server to the other.
  - [x] data is streamed to server
  - [x] HTTP Streaming
