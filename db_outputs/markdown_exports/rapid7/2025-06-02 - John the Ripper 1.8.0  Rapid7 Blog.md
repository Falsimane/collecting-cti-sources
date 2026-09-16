# John the Ripper 1.8.0 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2013/05/30/john-the-ripper-180/
- **Date :** 2025-06-02

---

Hi,

Concluding phase one of the Magnificent7 project, I've released John the Ripper 1.8.0 today. This version number reflects that we view this as a major release, considering that version 1.7 came out in early 2006 - more than 7 years ago - and there have been only (many) minor releases during those years (the latest of them being 1.7.9). Curiously, it's also been a little over 7 years between versions 1.6 (late 1998) and 1.7, so it was time for a 1.8. ;-) (Seriously, though, I'd be happy to have released both 1.7 and 1.8 much sooner.)

Although only JtR 1.8.0 source code and .chr files are available at this time (to be used mostly on Unix-like systems, where building from source is customary and convenient), we do intend to release Windows build(s) of JtR 1.8.x, a jumbo based on 1.8.x, and a Pro based on 1.8.x at a later time. Meanwhile, magnum is regularly sync'ing the [bleeding-jumbo branch on GitHub](https://github.com/magnumripper/JohnTheRipper/tree/bleeding-jumbo) to be based on the latest core tree (which means 1.8.0 at the moment).

As planned, John the Ripper 1.8 features a new revision of incremental mode with better efficiency in terms of passwords cracked per candidate passwords tested. Also, incremental mode's length and character set limitations in default builds have been lifted. Now default builds are capable of lengths of up to 24 and of the full 8-bit character set (except only for the NUL character), although most of the supplied charset files only contain data for lengths of up to 13 (this is not an arbitrary choice, but is a reasonable cut-off based on our testing). As an exception, digits.chr contains data for lengths of up to 20.

I'd like to thank magnum and bartavelle for running additional tests, which first helped spot a problem and then confirmed that, after my fix, the new incremental mode consistently outperformed the old one in their tests as well.

Another thing that changed is the status line. Now it includes as many as four distinct speed metrics. The four speed metrics are as follows: g/s is successful guesses per second (so it'll stay at 0 until at least one password is cracked), p/s is candidate passwords tested per second, c/s is "crypts" (password hash or cipher computations) per second, and C/s is combinations of candidate password and target hash per second. Versions of John prior to 1.8.0 displayed only the C/s rate (calling it c/s).

Finally, John the Ripper has gained the "--fork=N" and "--node=MIN[-MAX]/TOTAL" options for trivial parallel and distributed processing. These are usable along with any cracking mode, regardless of whether the "format" is OpenMP-enabled or not, and these two options may be used together as well as on their own. Naturally, they're documented in some detail in doc/OPTIONS.

"--fork=N" is only available on Unix-like systems. It is an easy way to make use of multiple CPUs or CPU cores - you simply specify the number of John processes that you'd like to run. You may use "--fork" as an alternative to OpenMP, for formats currently lacking OpenMP support, or/and along with OpenMP (e.g., on a machine with 64 logical CPUs you might choose to run with "--fork=8" for 8 processes and use OpenMP to run 8 threads per process).

You may use "--fork" along with "--node" to use multiple machines while also running multiple John processes per machine. For example, to use two similar 8-core machines you may run "--fork=8 --node=1-8/16" on one of the machines and "--fork=8 --node=9-16/16" on the other.

Many other changes and enhancements have been made as well. Please refer to the announcement / release notes on our announcement mailing list for more detail. Feedback is welcome on the john-users mailing list, as usual.

I'd like to thank Rapid7 and the Magnificent7 program for enabling me to dedicate more time to implementing many of these changes and bringing them to release quality.

Alexander

## Article tags

  * [Metasploit](/blog/tag/metasploit/)