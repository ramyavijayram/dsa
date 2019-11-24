from stack import ArrayStack

def bodmas(exp):
	expr=exp.split()
	oper=ArrayStack()
	nums=ArrayStack()
	for a in expr:
		if a.isdigit()==True:
			nums.push(a)
		elif a in ['+','-','*','/']:
			oper.push(a)
		else :
			continue
	while oper.isempty()==False:
		a=int(nums.pop())
		b=int(nums.pop())
		op=oper.pop()
		if op=='+':
			result=b+a
		if op=='-':
			result=b-a
		if op=='*':
			result=b*a
		if op=='/':
			result=b/a
		nums.push(result)
	return (result)

if __name__ == '__main__':
	exp='[ 5 + { 12 * 15 * ( 32 / 2 ) } ]'
	print (bodmas(exp))
