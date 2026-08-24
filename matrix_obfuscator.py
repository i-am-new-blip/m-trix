#!/usr/bin/env python3.14
import sys,re,random, ast
def n2esl(n):
    cbin=bin(n)[2:][::-1]
    cbin=[int(i) for i in cbin]
    cbin=[i for i,v in enumerate(cbin) if v == 1]
    base='(a()@(t()@(n()@n)@(n()@n)))' # NOTE: its .n=2
    out=[]
    for i in cbin:
        number_trans=f"(a()@(t()@{'@'.join(['(n()@n)' for _ in range(i)])}))" if i>1 else ("(s()@(t()@(n()@n)@(n()@n)))" if i == 0 else ("(n()@n)" if i == 1 else ""))
        out.append(f'(e()@(t()@{base}@{number_trans}))')
    return '(a()@(t()@' + '@'.join(out) + '))'
def esl_convert(n):
    x=[n2esl(ord(i)) for i in n]
    return "c()@(t()@" + '@'.join(x) + ')'


dTop=list("̛̀́̂̃̄̅̆̇̈̉̊̋̌̍̎̏̐̑̒̓̔̽̾̿̀́͂̓̈́͊͋͌͐͑͒͗̈́͆͛̕̚͘͝͠͡")
dBot=list("̡̢̧̨̖̗̘̙̜̝̞̟̠̣̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼͇͈͉͍͎͙͚͓͔͕͖͜͟ͅ")
dMid=list("̴̵̶̷̸")
def zalgo(textSize=None,hs=None,nT=''):
 if not textSize:
  textSize=random.randint(1,120)
 if not hs:
  hs=random.randint(1,120)
 t=''
 for _ in range(textSize):
  t+=random.choice('qwertyuiopasdfghjklzxccvbnmQWERTY_UIOPASDFGHJKLZXCVBNM'+('01234567189'if _ else''))
 for i in t:
  nc=i
  nc += random.choice(dMid)
  for count in range(hs):
   nc += random.choice(dTop)
  for count in range(hs):
   nc += random.choice(dBot)
  nT+=nc
 return nT

VER = "1.5.3"
N = f"version{VER}-{zalgo(10,20)}"

PY_EXEC="(l()@((c()@(t()@(a()@(t()@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(s()@(t()@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))))@(a()@(t()@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))))@(a()@(t()@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(s()@(t()@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))))@(a()@(t()@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(s()@(t()@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(n()@n)))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)))))@(e()@(t()@(a()@(t()@(n()@n)@(n()@n)))@(a()@(t()@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n)@(n()@n))))))))).n))"
PY_STDLIB=f'O="__matmul__";M=(type({N!r},(),{{"__init__":lambda *a:None}}),);t,a,s,c,e,n,l=(type({N!r},M,{{O:lambda x,n:(setattr(x,"t",[])if not getattr(x,"t",0)else 0,x.t.append(n),x)[-1]}}),type({N!r},M,{{O:lambda x,n:(setattr(n.t[0],"n",sum([i.n for i in n.t])),n.t[0])[-1]}}),type({N!r},M,{{O:lambda x,n:(setattr(n.t[0],"n",n.t[0].n-n.t[1].n),n.t[0])[-1]}}),type({N!r},M,{{O:lambda a,b:(setattr(b.t[0],"n","".join([chr(i.n)for i in b.t])),b.t[0])[-1]}}),type({N!r},M,{{O:lambda x,n:(setattr(n.t[0],"n",n.t[0].n**n.t[1].n),n.t[0])[-1]}}),type({N!r},M,{{O:lambda x,n:(setattr(x,"n",1),x)[-1]}}),type({N!r},M,{{O:lambda x,n:getattr(__builtins__,n)}}));del O,M'
PVM_PY_STDLIB=f"t,a,s,c,e,n,l=type({N!r},(),{{'g':__import__('builtins'),'c':lambda s,a,b=None:(s.c(a),s.c(b))if b!=None else a if type(a)is not list else s.r[a[0]]if len(a)==1 and isinstance(a[0],(str,int))else{{'reflist':lambda:list(map(s.c,a[1])),'tuple':lambda:tuple(a[1]),'reftuple':lambda:tuple(map(s.c,a[1]))}}[a[0]]()if len(a)==2 and type(a[0])==str else a,'__init__':lambda s:[s.__setattr__(a,b)for(a,b)in zip(['r','i'],[{{}},{{0:s.M_MATH,1:s.M_EQ,4:s.P_GET,5:s.P_CALL,6:s.P_PROP,7:s.P_INDEX,8:s.C_SETR,9:s.C_HLT,11:s.F_GOTO,14:s.F_IF,20:s.C_DEFINE,21:s.C_DICTADD}}])]and None,'M_MATH':lambda s,o,a,b,A:((b:=s.c(a,b)),(a:=b[0]),(b:=b[1]),s.r.__setitem__(A,[lambda:a+b,lambda:a-b,lambda:a**b][o]()),s.__setattr__('pc',s.pc+1)),'M_EQ':lambda s,a,b,A:((b:=s.c(a,b)),(a:=b[0]),(b:=b[1]),s.r.__setitem__(A,a==b),s.__setattr__('pc',s.pc+1)),'P_GET':lambda s,n,a:(s.r.__setitem__(a,getattr(s.g,s.c(n))),s.__setattr__('pc',s.pc+1)),'P_CALL':lambda s,f,a,*r:((b:=[s.c(i)for i in r[:a]]),(c:=r[a]if len(r)>a else None),(o:=s.r.get(f)(*b)),s.r.__setitem__(c,o),s.__setattr__('pc',s.pc+1)),'P_PROP':lambda s,S,*t:((a:=t[-1]),(t:=t[:-1]),(o:=s.r[S]),[(o:=getattr(o,v))for v in t],s.r.__setitem__(a,o),s.__setattr__('pc',s.pc+1)),'P_INDEX':lambda s,a,i,o:((i:=s.c(i)),(i:=slice(*i)if i.__class__==list and 1<len(i)<4 else i),s.r.__setitem__(o,s.r[a][i]),s.__setattr__('pc',s.pc+1)),'C_SETR':lambda s,v,a:(s.r.__setitem__(a,v),s.__setattr__('pc',s.pc+1)),'C_HLT':lambda s,a=None:(s.__setattr__('running',False),s.__setattr__('returns',s.c(a))),'C_DICTADD':lambda s,r,k,v:((v:=s.c(k,v)),(k:=v[0]),(v:=v[1]),s.r.setdefault(r,{{}}).__setitem__(k,v),s.__setattr__('pc',s.pc+1)),'C_DEFINE':lambda s,b,h:((f:=s.heap[h]),(d:=lambda*a:((v:=type(s)()),v.load(f).__setattr__('r',{{'args':a,'largs':len(a)}}),print(h),v.run())[-1]),s.r.__setitem__(b,d),s.__setattr__('pc',s.pc+1)),'F_IF':lambda s,b,a:s.__setattr__('pc',a if s.r[b]else s.pc+1)and print(s.pc),'F_GOTO':lambda s,a:s.__setattr__('pc',a),'load':lambda s,b:(s.__setattr__('b',b),s)[-1],'run':lambda s:((c:=s.b),(b:=c[1:]if type(c[0])==dict else c),print(type(c[0]),c[0]),[*map(s.__setattr__,['pc','returns','running'],[0,None,True])],s.__setattr__('heap',c[0]['heap'])if type(c[0])==dict else None,[*iter(lambda:s.running and((i:=b[s.pc]),print(i),s.i[i[0]](*i[1:]),1)[-1],False)])and s.returns}})().load([{{'heap':[[[9]],[[7,'args',0,2],[7,'args',1,5],[6,2,'t','append',4],[5,4,1,[5]],[9,[2]]],[[7,'args',1,1],[4,'setattr',2],[4,'getattr',3],[4,'len',8],[6,1,'t',4],[7,4,0,5],[8,0,6],[8,0,7],[5,8,1,[4],8],[7,4,[6],9],[6,9,'n',9],[0,0,[7],[9],7],[0,0,[6],1,6],[1,[6],[8],10],[14,10,16],[11,9],[5,2,3,[5],'n',[7]],[9,[5]]],[[7,'args',1,1],[4,'setattr',2],[6,1,'t',3],[7,3,1,4],[6,4,'n',4],[7,3,0,5],[6,5,'n',6],[0,1,[6],[4],7],[5,2,3,[5],'n',[7]],[9,[5]]],[[7,'args',1,1],[4,'setattr',2],[4,'getattr',3],[4,'len',8],[4,'chr',11],[6,1,'t',4],[7,4,0,5],[8,0,6],[8,'',7],[5,8,1,[4],8],[7,4,[6],9],[6,9,'n',9],[5,11,1,[9],9],[0,0,[7],[9],7],[0,0,[6],1,6],[1,[6],[8],10],[14,10,18],[11,10],[5,2,3,[5],'n',[7]],[9,[5]]],[[7,'args',1,1],[4,'setattr',2],[6,1,'t',3],[7,3,1,4],[6,4,'n',4],[7,3,0,5],[6,5,'n',6],[0,2,[6],[4],7],[5,2,3,[5],'n',[7]],[9,[5]]],[[7,'args',0,1],[4,'setattr',2],[5,2,3,[1],'n',1],[9,[1]]],[[7,'args',1,1],[4,[1],2],[9,[2]]],[[7,'args',0,1],[4,'setattr',0],[5,0,3,[1],'t',[]],[9]]]}},[4,'type',0],[8,'__matmul__',2],[20,1,0],[21,3,'__init__',[1]],[5,0,3,'base',['tuple',[]],[3],4],[20,1,1],[21,3,[2],[1]],[20,1,8],[21,3,'__init__',[1]],[5,0,3,'t',['reftuple',[[4]]],[3],'t'],[20,1,2],[21,3,[2],[1]],[5,0,3,'a',['reftuple',[[4]]],[3],'a'],[20,1,3],[21,3,[2],[1]],[5,0,3,'s',['reftuple',[[4]]],[3],'s'],[20,1,4],[21,3,[2],[1]],[5,0,3,'c',['reftuple',[[4]]],[3],'c'],[20,1,5],[21,3,[2],[1]],[5,0,3,'e',['reftuple',[[4]]],[3],'e'],[20,1,6],[21,3,[2],[1]],[5,0,3,'n',['reftuple',[[4]]],[3],'n'],[20,1,7],[21,3,[2],[1]],[5,0,3,'l',['reftuple',[[4]]],[3],'l'],[9,['reflist',[['t'],['a'],['s'],['c'],['e'],['n'],['l']]]]]).run()"
FILLER_LIST ='nice try; keep reading; this is not it; lets format to check what i can see - said you;lets deobfuscate this - 7 years ago, trying to deobfuscate; you thought; almost had it; wrong layer; try harder; nope; lol; lmao; wasted time; nothing here; dead end; keep scrolling; this does nothing; still nothing; are you sure; you missed it; bad guess; try again; not the flag; not the payload; not the secret; wrong path; this is filler; decoy; red herring; fake trail; noise; junk; intentional garbage; youre wasting time; keep deobfuscating; almost funny; this string is useless; hello reverser; hi analyst; enjoy the mess; good luck; have fun; nothing to see; move along; this wont help; still wrong; try a debugger; grep harder; read slower; read faster; this is a trap; decoding this is pointless; youre not there yet; not even close; far from done; wont make sense; youll regret this; this is intentional; designed to annoy; mission failed; abort analysis; go touch grass; take a break; coffee time; why are you here; what did you expect; surprise nothing; another fake string; yep more noise; youre still reading; seriously stop; this never ends; welcome to hell; python moment; matrix has you; wake up; there is no spoon; follow the white rabbit; knock knock; still no secret; final fake message; drivin; in; my; car; right after a beer; wait that bump; is shaped like a deer; D U I?; how about you die; ill walk a 1kM/H; blood is on the dirt; beer is on the trcuk; TRUCK; burguntruckung; asgore.'
FILLER_LIST = FILLER_LIST.split('; ')
def filler(match):
    name = match.group(1)

    if random.random() > .5:
        return f"{name}()"

    msg = random.choice(FILLER_LIST)
    q = '"' if random.random() > .5 else "'"

    return f"{name}({q}{msg}{q})"

def AL(code):
    
    tascenl = [zalgo(random.randint(1,20), random.randint(1,20)) for _ in range(7)]
    names = dict(zip('tascenl', tascenl))

    class Rename(ast.NodeTransformer):
        def visit_Name(self, node):
            if node.id in names:
                node.id = names[node.id]
            return node

    tree = ast.parse(code)
    tree = Rename().visit(tree)
    ast.fix_missing_locations(tree)

    return ast.unparse(tree), names

def obfuscate(code, mode, zalgo, pvm=False):
    code = code[::-1]

    if mode == 'py':
        header = (
            f'# INTENDED FOR PYTHON 3.5+ '
            f'|| Check out https://esolangs.org/wiki/M@trix || '
            f'Check out https://github.com/i-am-new-blip/pvm\n'
            f'{PY_STDLIB if not pvm else PVM_PY_STDLIB};_='
        )
        
        inverted_obfuscated = '(' + esl_convert(code) + ').n[::-1]'

        payload = PY_EXEC + "(" + inverted_obfuscated + ")"

        # Only obfuscate the generated execution payload
        if zalgo:
            payload,mapping = AL(payload)
            default_split = list(mapping.values())
            header = header.replace('t,a,s,c,e,n,l', ','.join(default_split))
        else:
            default_split = 'tascenl'
        # Only filler the payload, NOT stdlib/header
        # (still risky because payload has syntax too)
        payload = re.sub(
            rf"({'|'.join(map(re.escape, default_split))})\(\)",
            filler,
            payload
        )
        
        return header + payload

def get_mode(file):
    if file.endswith('.py'):
        return 'py'
    elif file.endswith('.lua'):
        return 'lua'
    elif file.endswith('.js'):
        return 'js'

if __name__=='__main__':
 running_from = 'intr'if hasattr(sys,'ps1')else'-c'if sys.argv and sys.argv[0]=='-c'else'file'
 if 'CODE' in locals() or 'CODE' in globals(): exit(obfuscate(CODE,MODE))
 filename=input("input the file to obfuscate: ")if len(sys.argv)==1 or running_from=='intr'else sys.argv[-2]
 zalginator=input("Hello my friend! do i zalgo? (yn) ")=='y' if len(sys.argv)==1 or running_from=='intr'else sys.argv[-1]
 pvm=False#input("Hello my guy! do i include PVM stdlib? (yn) ")=='y' if len(sys.argv)==1 or running_from=='intr'else sys.argv[-1]
 mode=get_mode(filename)
 with open(filename)as r: read=r.read()
 output = obfuscate(read,mode,zalginator,pvm)
 if not sys.stdin.isatty(): exit(output)
 with open(filename+'.obfuscated','w')as f:
  f.write(output)
  print(end='Done! check it out on '+filename+'.obfuscated')
  if len(sys.argv)==1 and running_from != 'intr':
   print(end=', by the way you can put the filename in the args.'if running_from=='file'else f', by the way you can put the filename right after the exec code like this:\n{sys.executable} -c [code] [filename]')
  print()