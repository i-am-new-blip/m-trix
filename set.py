class t:
    def __matmul__(x,n):setattr(x,'t',[]) if not getattr(x,'t',0) else None;x.t.append(n);return x
class a:
    def __matmul__(x,n):n.t[0].n=sum([i.n for i in n.t]);return n.t[0]
class s:
    def __matmul__(x,n):n.t[0].n-=n.t[1].n;return n.t[0]
class c:
    def __matmul__(a,b):b.t[0].n="".join([chr(i.n) for i in b.t]);return b.t[0]
class d:
    def __matmul__(x,n):n.t[0].n/=n.t[1].n;return n.t[0]
class e:
    def __matmul__(x,n):n.t[0].n**=n.t[1].n;return n.t[0]
class C:
    def __matmul__(x,n):n.t[0].n**=2;return n.t[0]
class f:
    def __matmul__(x,n):return x+(n.t@(s()@(t()@(n()@n)@(a()@(t()@(n()@n)@(n()@n))))))
    def __add__(x,n):
        q,b,c = n.t
        try:
            x,_=(len(b)-c.n),n()@n  # (starting x = 0) x++
            _.n=x
            d()@(t()@(n()@n)@_) #     1/x # 1/0 = quit the loop
            c=a()@(t()@(_)@(n()@n))if isinstance(q,function)else _ # c= x+1
            q(b[c])                 # q(b[c])
            return x+(t()@q@b@c)
        except:0
class m:
    def __matmul__(x,n):n.t[0].n*=n.t[1].n;return n.t[0]
class z:
    def __matmul__(x,n):return ord(n.t[0])
class n:
    def __matmul__(x,n):x.n=1;return x
class h:
    def __init__(x):import sys;sys.setrecursionlimit(999999999)
class l:
    def __matmul__(x,n):return getattr(__builtins__,n)
class x:
    def __matmul__(x,_):return eval(_)
class kys:
    def __matmul__(x,_):return exit(_)


## trut machin
í=s()@(t()@([g:=(n()@n),setattr(g,'n',(l()@"ord")((l()@"input")())),g][-1])@[g:=(n()@n),setattr(g,'n',48),g][-1]).n

[g:=(n()@n),setattr(g,'n',(l()@"ord")((l()@"input")())),g][-1]
e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n))))
