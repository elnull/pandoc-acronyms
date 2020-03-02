# pandoc-acronyms - A Pandoc filter for managing acronyms

## Acronyms? WTF?

There is a convention in more precise writing to provide the full text
of an acronym at first use. This can get difficult for example if the
text of documents is split over multiple files, which makes it hard
for the authors to know where the acronym will be used first. Such a
task is best left to the computer. This is what the `pandoc-acronyms`
filter is for. Authors list acronyms in a data file and then reference
them in the text.

## HOWTO

Write a data file that contains your acronyms:

    {
		"aba": {
			"shortform": "ABA",
			"longform": "a better acronym"
		},
		"bba": {
			"shortform": "BBA",
			"longform": "beer brewing attitude"
		}
	}

Then in the text, use the acronym in encoded form like `[!bba]`. The
filter will recognize it. On first use it replaces the marker with
`beer brewing attitude (BBA)`.
Any later use will be replaced by `BBA`. The
filter will print a notice if an acronym is found in the text that is
not defined in the data file. The keys may consist of letters, numbers,
dashes and underscores ("a-b" or "ab" or "a_b").

## Using the filter

The filter mechanism is a built-in feature of pandoc. The filter is
added to how pandoc is invoked:

	> pandoc --filter pandoc-acronyms document.md

Unfortunately, pandoc does not allow to pass parameters to filters. The
acronym filter needs to load the acronyms from the data file. To work
around this, the parameters to the filter can be passed in environment
variables:

	> pandoc-acronyms --help
	Usage: pandoc-acronyms [OPTIONS] [FORMAT]...

	The pandoc-acronyms filter.

	Options:
		-a, --acronyms TEXT           A file with acronym definitions in JSON format.
		-v, --verbose / --no-verbose  Enable verbose output.
		-v, --debug / --no-debug      Enable debug output.
		--help                        Show this message and exit.

The environment variable PANDOC_ACRONYMS_ACRONYMS can be used to
replace the --acronyms option. Similarly, the variable
PANDOC_ACRONYMS_VERBOSE enables diagnostic output.

## Installation

The pandoc acronym filter is installed using Python setuptools:

	> python setup.py install
	...

After that, it is available as a stand-alone program in the
installation location used by Python.

## Testing and debugging

The `pandoc-acronyms` code uses the standard Python unittest
framework. Most tests are data-driven in that they use regular
Markdown files and JSON acronym dictionaries as input and test how the
code handles them. To test the filter code as regular Python unit
tests, test Markdown input is first converted into the Pandoc "native
JSON" format in memory and then fed to the filter code by the
tests. This means the unit tests run stand-alone (without the need for
Pandon to invoke them as a filter), making the test code easily
debugable.

## How to contribute

The [Git repository for the pandoc acronym filter](https://gitlab.com/mirkoboehm/pandoc-acronyms)
is hosted on Gitlab. It uses the Gitlab CI
to ensure quality, also for development branches and incoming merge
requests. To contribute, please submit a merge request. Your merge
request should maintain or increase the test coverage.
