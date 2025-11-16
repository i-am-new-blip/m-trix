xbin = bin
def n2esl(n):
    bin=xbin(n)[2:][::-1]
    bin=[int(i) for i in bin]
    bin=[i for i,v in enumerate(bin) if v == 1]
    base='(a()@(t()@(n()@n)@(n()@n)))' # NOTE: its .n=2
    out=[]
    for i in bin:
        number_trans=f"(a()@(t()@{'@'.join(['(n()@n)' for _ in range(i)])}))" if i>1 else ("(s()@(t()@(n()@n)@(n()@n)))" if i == 0 else ("(n()@n)" if i == 1 else ""))
        out.append(f'(e()@(t()@{base}@{number_trans}))')
    return '(a()@(t()@' + '@'.join(out) + '))'
def esl_convert(n):
    if isinstance(n, str):
        x=[n2esl(ord(i)) for i in n]
        return "c()@(t()@" + '@'.join(x) + ')'
    elif isinstance(n, int):
        return n2esl(n)+".n"
print(esl_convert(input()))
