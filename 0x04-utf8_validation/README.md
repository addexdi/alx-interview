0x04-utf8_validation





UTF-8 is a variable-width character encoding used for electronic communication. Defined by the Unicode Standard, the name is derived from Unicode (or Universal Coded Character Set) Transformation Format – 8-bit.[1]

UTF-8 is capable of encoding all 1,112,064[nb 1] valid character code points in Unicode using one to four one-byte (8-bit) code units. Code points with lower numerical values, which tend to occur more frequently, are encoded using fewer bytes. It was designed for backward compatibility with ASCII: the first 128 characters of Unicode, which correspond one-to-one with ASCII, are encoded using a single byte with the same binary value as ASCII, so that valid ASCII text is valid UTF-8-encoded Unicode as well. Since ASCII bytes do not occur when encoding non-ASCII code points into UTF-8, UTF-8 is safe to use within most programming and document languages that interpret certain ASCII characters in a special way, such as / (slash) in filenames, \ (backslash) in escape sequences, and % in printf.

UTF-8 was designed as a superior alternative to UTF-1, a proposed variable-width encoding with partial ASCII compatibility which lacked some features including self-synchronization and fully ASCII-compatible handling of characters such as slashes. Ken Thompson and Rob Pike produced the first implementation for the Plan 9 operating system in September 1992.[2][3] This led to its adoption by X/Open as its specification for FSS-UTF, which would first be officially presented at USENIX in January 1993 and subsequently adopted by the Internet Engineering Task Force (IETF) in RFC 2277 (BCP 18) for future internet standards work, replacing Single Byte Character Sets such as Latin-1 in older RFCs.

UTF-8 is the dominant encoding for the World Wide Web (and internet technologies), accounting for 98% of all web pages, and up to 100.0% for some languages, as of 2022.[4]

