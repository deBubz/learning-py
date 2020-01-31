# Regex quick guide

```txt
^           Matches start of line
$           Matches end of line
.           Matches any char

\s          Matches whitespace
\S          Matches any non-whitespace char

*           Repeats a char 0 or more times
*?          Repeats a char 0 or more times (non-greedy)

+           Reoeats a char 1 or more times
+?          Repeats a char 1 or more times (non-greedy)

[aeiou]     Match a single char in the listed set
[^XYZ]      Match a single char Not in the listed set
[a-z0-9]    Match set of chars in range 
(           where string extraction starts
)           where string extraction ends
```