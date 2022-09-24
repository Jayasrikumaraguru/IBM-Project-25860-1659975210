dict={'tom':123,'jeg':34}
n=input()
ans=dict.get(n)
if(ans==None):
    print("not found")
else:
    print(f"{n} = {ans}")

