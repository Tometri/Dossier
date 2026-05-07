Headings: 

# '<h1>' heading == the largest
## '<h2>' heading
### '<h3>' heading
#### '<h4> heading
##### '<h5>' heading
###### '<h6>' heading == the smallest

Lists:

Unordered lists [each item placed on its own line using '-', '*', or '+'.]
Ordered lists [a list is ordered by using any number rather than a list character: '1., 1., 1.','1. 2. 3.';markdown handles counting automatically.]
Task lists [extends unordered lists to use checkboxes using empty brackets '[ ]', or filled brackets '[x]']

Code Blocks / Syntax Highlighting:
Example 1->
```bash
git clone https://github.com/skills/communicate-using-markdown
```

Example 2->
```js
var myVar = "Hello, world!";
```

Images:

Images can be displayed with URLs relative to the repo, or using absolute URLs. 
Relative-> ![Mona the Octocat](myrepo/original.png)
Absolute-> ![Mona the Octocat](https://octodex.github.com/images/original.png)

Simple HTML can be used for images-> <img alt="Mona the Octocat" src="https://octodex.github.com/images/original.png" width="200" align="right">
'alt' specifies alternative text
'src' specifies the source URL
'width'/'height' specify size in pixels
'align' allows setting a position: 'left', 'right', etc.

Styling:

Bold == '** **' or '__ __'
Italic == '* *' or '_ _'
Strikethrough == '~~ ~~' or '~ ~'
Bold and nested italic == '** **' and '_ _' Ex: '**text _text_ **'
All bold and italic == '*** ***'
Subscript == '<sub> </sub>'
Superscript == '<sup> </sup>'
Underline == '<ins> </ins>'
Quote == text is quoted with > Ex: > This is a quote.
Code == can be quoted with '` `' to quote a code and with '``` ```' to format the code into a block.

Color:

HEX == '#RRGGBB' Ex: '#0969DA'
RGB == 'rgb(R,G,B)' Ex: 'rgb(9, 105, 218)'
HSL == 'hsl(H,S,L)' Ex: 'hsl(212, 92%, 45%)

Links:

inline links: links are created by wrapping link text in brackets '[ ]'. then wrapping the url in parentheses '( )'

section links: any section with a heading can be linked to using a heading anchor. Basic rules for heading anchors are: letters converted to lowercase, spaces replaced with hyphens, any whitespace or punctuation characters removed, markup formatting removed ('__italic__' becomes 'italic')
Ex: 
section->##sample section
link->[link text](#sample-section)

relative links: 
You can define relative links and image paths in your rendered files to help readers navigate to other files in your repository.
A relative link is a link that is relative to the current file. For example, if you have a README file in root of your repository, and you have another file in docs/CONTRIBUTING.md, the relative link to CONTRIBUTING.md in your README might look like this:

[Contribution guidelines for this project](docs/CONTRIBUTING.md)

GitHub will automatically transform your relative link or image path based on whatever branch you're currently on, so that the link or path always works. The path of the link will be relative to the current file. Links starting with / will be relative to the repository root. You can use all relative link operands, such as ./ and ../.

Custom Anchors: 
You can use standard HTML anchor tags (<a name="unique-anchor-name"></a>) to create navigation anchor points for any location in the document. To avoid ambiguous references, use a unique naming scheme for anchor tags, such as adding a prefix to the name attribute value.
Ex:
custom anchor-> <a name="my-custom-anchor-point"></a>
link-> [A link to that custom anchor](#my-custom-anchor-point)

Line breaks: To include a line break add either two spaces at the end of the first line or a backslash at the end of the first line. An html single line break tag at the end of the first line can also be used '<br/>'.

Nested lists: can be made by indenting one or more list items below another item.
Ex: 1.item
	2.item
Emoji: 

You can add emoji to your writing by typing :EMOJICODE:, a colon followed by the name of the emoji.

Footnotes:

Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, add 2 spaces to the end of a line.  
This is a second line.

Alerts:
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

Hidden content:
<!-- This content will not appear in the rendered Markdown -->

There is much more MD syntax that has not been covered, but guides can be found on GitHub. More precisely, at the time of writing -> https://docs.github.com/en/get-started/writing-on-github 


