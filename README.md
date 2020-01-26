# pandoc-acronyms - A Pandoc filter for managing acronyms

## Testing and debugging

The pandoc-acronyms code uses the standard Python unittest
framework. Most tests are data-driven in that they use regular
Markdown files and JSON acronym dictionaries as input and test how the
code handles them. To test the filter code as regular Python unit
tests, test Markdown input is first converted into the Pandoc "native
JSON" format in memory and then fed to the filter code by the
tests. This means the unit tests run stand-alone (without the need for
Pandon to invoke them as a filter), making the test code easily
debugable.
