aud2arm
=======

Convert iOS aud file to arm

iOS apps uses aud as the audio file format.  Actually this file format is 99% similar to arm format, except it has no ARM heading.  e.g:

//file1.aud<br \>
binary_content

//file1.amr<br \>
\#!AMR<br \>
binary_content

This script is used to convert the aud file(s) to arm file(s).
