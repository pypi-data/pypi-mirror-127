# checksums

A command line tool that show/verify checksums for a file. Works on Windows, macOS and Linux.

## Installation

```
pip install checksums
```

## Usages

- Show checksums of a file:

```
$ checksums ./file.txt
```

- Verify the MD5 checksum of a file:

```
$ checksums check-md5 [MD5-checksum here] ./file.txt
```

- Verify the SHA-1 checksum of a file:

```
$ checksums check-sha1 [SHA-1-checksum here] ./file.txt
```

- Verify the SHA-256 checksum of a file:

```
$ checksums check-sha256 [SHA-256-checksum here] ./file.txt
```

- Verify the SHA-512 checksum of a file:

```
$ checksums check-sha512 [SHA-512-checksum here] ./file.txt
```

