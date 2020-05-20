def is_matched_html(raw):
    stack = list()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith('/'):
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            if tag[1:] != stack.pop():
                return False
        j = raw.find('<', k + 1)

    return len(stack) == 0


raw = """<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>"""


print(is_matched_html(raw))


raw2 = """<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>"""


print(is_matched_html(raw2))