# PolyFile
<p align="center">
  <img src="logo/polyfile_name.png?raw=true" width="256" title="PolyFile">
</p>
<br />

[![PyPI version](https://badge.fury.io/py/polyfile.svg)](https://badge.fury.io/py/polyfile)
[![Tests](https://github.com/trailofbits/polyfile/workflows/Tests/badge.svg)](https://github.com/trailofbits/polyfile/actions)
[![Slack Status](https://empireslacking.herokuapp.com/badge.svg)](https://empireslacking.herokuapp.com)

A utility to identify and map the semantic structure of files,
including polyglots, chimeras, and schizophrenic files. It can be used
in conjunction with its sister tool
[PolyTracker](https://github.com/trailofbits/polytracker) for
_Automated Lexical Annotation and Navigation of Parsers_, a backronym
devised solely for the purpose of collectively referring to the tools
as _The ALAN Parsers Project_.

## Quickstart

You can install the latest stable version of PolyFile from PyPI:
```
pip3 install polyfile
```

To install PolyFile from source, in the same directory as this README, run:
```
pip3 install -e .
```

This will automatically install the `polyfile` and `polymerge` executables in your path.

## Usage

```
usage: polyfile [-h] [--filetype FILETYPE] [--list] [--html HTML]
                [--try-all-offsets] [--only-match] [--debug] [--quiet]
                [--version] [-dumpversion]
                [FILE]

A utility to recursively map the structure of a file.

positional arguments:
  FILE                  The file to analyze; pass '-' or omit to read from
                        STDIN

optional arguments:
  -h, --help            show this help message and exit
  --filetype FILETYPE, -f FILETYPE
                        Explicitly match against the given filetype (default
                        is to match against all filetypes)
  --list, -l            list the supported filetypes (for the `--filetype`
                        argument) and exit
  --html HTML, -t HTML  Path to write an interactive HTML file for exploring
                        the PDF
  --try-all-offsets, -a
                        Search for a file match at every possible offset; this
                        can be very slow for larger files
  --only-match, -m      Do not attempt to parse known filetypes; only match
                        against file magic
  --debug, -d           Print debug information
  --quiet, -q           Suppress all log output (overrides --debug)
  --version, -v         Print PolyFile's version information to STDERR
  -dumpversion          Print PolyFile's raw version information to STDOUT and
                        exit
```

To generate a JSON mapping of a file, run:

```
polyfile INPUT_FILE > output.json
```

You can optionally have PolyFile output an interactive HTML page containing a labeled, interactive hexdump of the file:
```
polyfile INPUT_FILE --html output.html > output.json
```

### File Support

PolyFile has a cleanroom, [pure Python implementation of the libmagic file classifier](#libmagic-implementation), and
supports all 263 MIME types that it can identify.

It currently has support for parsing and semantically mapping the following formats:
* PDF, using an instrumented version of [Didier Stevens' public domain, permissive, forensic parser](https://blog.didierstevens.com/programs/pdf-tools/)
* ZIP, including recursive identification of all ZIP contents
* JPEG/JFIF, using its [Kaitai Struct grammar](https://formats.kaitai.io/jpeg/index.html)
* [iNES](https://wiki.nesdev.com/w/index.php/INES)
* [Any other format](https://formats.kaitai.io/index.html) specified in a [KSY grammar](https://doc.kaitai.io/user_guide.html)

For an example that exercises all of these file formats, run:
```bash
curl -v --silent https://www.sultanik.com/files/ESultanikResume.pdf | polyfile --html ESultanikResume.html - > ESultanikResume.json
```

Prior to PolyFile version 0.3.0, it used the [TrID database](http://mark0.net/soft-trid-deflist.html) for file
identification rather than the libmagic file definitions. This proved to be very slow (since TrID has many duplicate
entries) and prone to false positives (since TrID's file definitions are much simpler than libmagic's). The original
TrID matching code is still shipped with PolyFile and can be invoked programmatically, but it is not used by default.

### Output Format

PolyFile outputs its mapping in an extension of the [SBuD](https://github.com/corkami/sbud) JSON format described [in the documentation](docs/json_format.md).

### libMagic Implementation

PolyFile has a cleanroom implementation of [libmagic (used in the `file` command)](https://github.com/file/file).
It can be invoked programmatically by running:
```python
from polyfile.magic import MagicMatcher

with open("file_to_test", "rb") as f:
    # the default instance automatically loads all file definitions
    for match in MagicMatcher.DEFAULT_INSTANCE.match(f.read()):
        for mimetype in match.mimetypes:
            print(f"Matched MIME: {mimetype}")
        print(f"Match string: {match!s}")
```
To load a specific or custom file definition:
```python
list_of_paths_to_definitions = ["def1", "def2"]
matcher = MagicMatcher.parse(*list_of_paths_to_definitions)
with open("file_to_test", "rb") as f:
    for match in matcher.match(f.read()):
        ...
```

## Merging Output From PolyTracker

[PolyTracker](https://github.com/trailofbits/polytracker) is PolyFile’s sister utility for automatically instrumenting
a parser to track the input byte offsets operated on by each function. The output of both tools can be merged to
automatically label the semantic purpose of the functions in a parser. For example, given an instrumented black-box
binary, we can quickly determine which functions in the program are responsible for parsing which parts of the input
file format’s grammar. This is an area of active research intended to achieve fully automated grammar extraction from a
parser.

A separate utility called `polymerge` is installed with PolyFile specifically designed to merge the output of both
tools.

```
usage: polyfile [-h] [--filetype FILETYPE] [--list] [--html HTML]
                [--only-match-mime] [--only-match] [--require-match]
                [--max-matches MAX_MATCHES] [--debug] [--trace] [--quiet]
                [--version] [-dumpversion]
                [FILE]

A utility to recursively map the structure of a file.

positional arguments:
  FILE                  the file to analyze; pass '-' or omit to read from
                        STDIN

optional arguments:
  -h, --help            show this help message and exit
  --filetype FILETYPE, -f FILETYPE
                        explicitly match against the given filetype or
                        filetype wildcard (default is to match against all
                        filetypes)
  --list, -l            list the supported filetypes (for the `--filetype`
                        argument) and exit
  --html HTML, -t HTML  path to write an interactive HTML file for exploring
                        the PDF
  --only-match-mime, -I
                        just print out the matching MIME types for the file,
                        one on each line
  --only-match, -m      do not attempt to parse known filetypes; only match
                        against file magic
  --require-match       if no matches are found, exit with code 127
  --max-matches MAX_MATCHES
                        stop scanning after having found this many matches
  --debug, -d           print debug information
  --trace, -dd          print extra verbose debug information
  --quiet, -q           suppress all log output (overrides --debug)
  --version, -v         print PolyFile's version information to STDERR
  -dumpversion          print PolyFile's raw version information to STDOUT and
                        exit
```

The output of `polymerge` is the same as [PolyFile’s output format](docs/json_format.md), augmented with the following:
1. For each semantic label in the hierarchy, a list of…
    1. …functions that operated on bytes tainted with that label; and
    2. …functions whose control flow was influenced by bytes tainted with that label.
2. For each type within the semantic hierarchy, a list of functions that are “most specialized” in processing that type.
   This process is described in the next section.

`polymerge` can also optionally emit a Graphviz `.dot` file or rendered PDF of the runtime control-flow graph recorded
by PolyTracker. 

### Identifying Function Specializations 

As mentioned above, `polymerge` attempts to match each semantic type of the input file to a set of functions that are
“most specialized” in operating on that type. This is an active area of academic research  and is likely to change in
the future, but here is the current method employed by `polymerge`:
1. For each semantic type in the input file, collect the functions that operated on bytes from that type;
2. For each function, calculate the Shannon entropy of the different types on which that function operated;
3. Sort the functions by entropy, and select the functions in the smallest standard deviation; and
4. Keep the functions that are shallowest in the dominator tree of the runtime control-flow graph.

## License and Acknowledgements

This research was developed by [Trail of
Bits](https://www.trailofbits.com/) with funding from the Defense
Advanced Research Projects Agency (DARPA) under the SafeDocs program
as a subcontractor to [Galois](https://galois.com). It is licensed under the [Apache 2.0 license](LICENSE).
The [PDF parser](polyfile/pdfparser.py) is modified from the parser developed by Didier Stevens and released into the
 public domain. © 2019, Trail of Bits.
