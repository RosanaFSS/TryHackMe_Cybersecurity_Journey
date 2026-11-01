<h3><a href="https://man7.org/linux/man-pages/man1/grep.1.html">grep</a><br><br>
<a href="https://man7.org/linux/man-pages/man1/chmod.1.html">chmod</a><br><br>
<a href="https://www.man7.org/linux/man-pages/man8/cron.8.html">cron</a><br><br>
<a href="https://man7.org/linux/man-pages/man1/whoami.1.html">whoami</a></h3>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<h1><a href="https://man7.org/linux/man-pages/man1/grep.1.html">grep</a></h1>
<p>Print lines that match <em>PATTERNS</em>.<br>

- [Generic Program Information](#1)<br>
- [Pattern Syntax](#2)<br>
- [Matching Controls](#3)<br>
- [General Output Control](#4)<br>
- [Output Line Prefix Control](#5)<br>
- [Context Line Control](#6)<br>
- [File and Directory Selection](#7)<br>
- [Other Options](#8)</p>


<br>
<br>
<p>Generic Program Information<a id='1'></a></p>

<div align="left"><p>

|Parameter         |Description|
|:-----------------|:-------------|
|`--help`<br><br>`-V`, `--version`  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          |Output a usage message and exit.<br><br>Output the version number of `grep` and exit. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|

</p></div>

<br>
<p>Pattern Syntax<a id='2'></a></p>

<div align="left"><p>

|Parameter                    |Description|
|:----------------------------|:-------------|
|`-E`, `--extended-regexp`  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>`-V`, `--version`<br><br>`-F`, `--fixed-strings`<br><br>`-G`, `--basic-regexp`<br><br><br>`-P`, `--perl-regexp`<br><br><br>|Interpret <em>PATTERNS</em> as extended regular <em>expressions</em> (EREs,see below).<br><br>Output the version number of grep and exit.<br><br>Interpret <em>PATTERNS</em> as fixed strings, not regular <em>expressions</em>.<br><br>Interpret <em>PATTERNS</em> as basic regular <em>expressions</em> (BREs, see below).<br>This is the default.<br><br>Interpret <em>PATTERNS</em> as Perl-compatible regular <emg>expressions</em> (PCREs).<br>This option is experimental when combined with the `-z` (`--null-data`)<br> option, and `grep -P` may warn of unimplemented features.|

</p></div>

<br>
<p>Matching Controls<a id='3'></a></p>

<div align="left"><p>

|Parameter                    |Description|
|:----------------------------|:-------------|
|`-e` <em>PATTERNS</em>, `--regexp`=<em>PATTERNS</em> &nbsp;&nbsp;&nbsp;&nbsp;<br><br><br><br>`-f` <em>FILE</em>, `--file`=<em>FILE</em><br><br><br><br><br>`-i`, `--ignore-case`<br><br><br>`--no-ignore-case`<br><br><br><br>`-v`, `--invert-match`<br><br>`-w`, `--word-regexp`<br><br><br><br><br><br><br>`-x`, `--line-regexp`<br><br><br>|Use <em>PATTERNS</em> as the patterns.  If this option is used  multiple times<br>or is combined with the `-f` (`--file`) option, search for all patterns given.<br>This option can be used to protect a pattern beginning with `-`.<br><br>Obtain patterns from <em>FILE</em>, one per line.  If this option is used<br>multiple times or is combined with the `-e` (`--regexp`) option, search<br>for all patterns given.  The empty file contains zero patterns, and<br>therefore matches nothing.  If <em>FILE</em> is `-` , read patterns from standard input.<br><br>Ignore case distinctions in patterns and input data, so that characters<br>that differ only in case match each other.<br><br>Do not ignore case distinctions in patterns and input data. This is the<br>default.  This option is useful for passing to shell scripts that already<br>use `-i`, to cancel its effects because the two options override each other.<br><br>Invert the sense of matching, to select non-matching lines.<br><br>Select only those lines containing matches that form whole words.<br>The test is that the matching substring must either be at the beginning<br>of the line, or preceded by a non-word constituent character.  Similarly,<br>it must be either at the end of the line or followed by a non-word<br>constituent character.  Word-constituent characters are letters, digits,<br>and the underscore.  This option has no effect if `-x` is also specified.<br><br>Select only those matches that exactly match the whole line.  For a<br>regular expression pattern, this is like parenthesizing the pattern<br>and then surrounding it with `^`and `$`.<br>|

</p></div>

<br>
<p>General Output Control<a id='4'></a></p>

<div align="left"><p>

|Parameter                    |Description|
|:----------------------------|:-------------|
|`-c`, `--count`<br><br>`--color`[`=`<em>WHEN</em>], `--colour`[`=`<em>WHEN</em>]<br><br>`-L`, `--files-without-match`<br><br>`-l`, `--files-with-matches`<br><br>`-m`<em>NUM</em>, `--max-count=`<em>NUM</em><br><br>`-o`, `--only-matching`<br><br>`-q`, `--quiet`, `--silent`<br><br>`-s`, `--no-messages`|Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum|

</p></div>

<br>
<p>Output Line Prefix Control<a id='5'></a></p>

<div align="left"><p>

|Parameter                    |Description|
|:----------------------------|:-------------|
|`-b`, `--byte-offset`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>`-H`, `--with-filename`<br><br>`-h`, `--no-filename`<br><br>`--label`=<em>LABEL</em><br><br>`-n`, `--line-number`<br><br>`-T`, `--initial-tab`<br><br>`-Z`, `--null`|Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum<br><br>Lorem Ypsum|

</p></div>

<br>
<p>Context Line Control<a id='6'></a></p>

<div align="left"><p>

|Parameter                    |Description|
|:----------------------------|:-------------|
|Lorem Ypsum | Lorem Ypsum|

</p></div>

<br>
<p>File and Directory Selection<a id='7'></a></p>

<div align="left"><p>

|Parameter                    |Description|
|:----------------------------|:-------------|
|Lorem Ypsum | Lorem Ypsum|

</p></div>

<br>
<p>Other Options<a id='8'></a></p>

<div align="left"><p>

|Parameter                    |Description|
|:----------------------------|:-------------|
|Lorem Ypsum | Lorem Ypsum|

</p></div>

<br>
<br>
<h1><a href="https://man7.org/linux/man-pages/man1/chmod.1.html">chmod</a></h1>
<p>Change file mode bits<br>
It uses three octal digits to set permissions for three specific user categories: Owner, Group, and Others.</p>

<div align="left"><p>
  
|Owner                                                |Group                                                     |Others                                                                               |
|:----------------------------------------------------:|:---------------------------------------------------------:|:------------------------------------------------------------------------------------:|
|`7` &nbsp;&nbsp; Full Access<br>4 (Read) + 2 (Write) + 1 (Execute)|`5` &nbsp;&nbsp; Read and execute<br>4 (Read) + 0 (Write) + 1 (Execute)|`0` &nbsp;&nbsp; No permissions<br>0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0|
</p></div>

<br>
<br>
<h1><a href="https://www.man7.org/linux/man-pages/man8/cron.8.html">cron</a></h1>
<p>Daemon to execute scheduled commands.</p>

|Command          |Use|
|:----------------|:-------------|
|$ <code>0 */6 * * *</code> <code>cp</code> <code>-R</code> <code>/home/user/data/backups/</code><br>&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *<br> Minute &nbsp;&nbsp;&nbsp; Hour  &nbsp;&nbsp;&nbsp; Day of Month &nbsp;&nbsp;&nbsp; Month &nbsp;&nbsp;&nbsp; Day of Week|Back up <code>/home/user/data</code> to <code>backup</code> every 6 hours.|

</p></div>

<br>
<br>
<h1><a href="https://man7.org/linux/man-pages/man1/whoami.1.html">whoami</a></h1>
<p>Print effective user name.</p>

<div align="left"><p>

|Command/<br>Keys             |Task<br><br>                                                       |Example<br><br>            |
|:----------------------------|:------------------------------------------------------------------|:---------------------|
|$ `whoami`<br><br>           |Tells you who you are on the system.<br> <br>                      |Lorem Ypsum<br><br>   |

</p></div>

<p>—</p>
