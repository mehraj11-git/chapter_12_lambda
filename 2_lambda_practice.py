def is_even(a):
    if a %2==0:
        return True
    else:
        return False
# this is a normal form 
# short form
def is_even(a):
    if a %2==0:
        return True
    return False
# very short form
def is_even(a):
  return a%2==0 

print(is_even(5))
 

#  now using lambda 
is_even2 = lambda a : a%2==0
print(is_even2(6))
# other funcs
def last(s):
    return s[-1]
print(last('khan'))

last1=lambda s : s[-1]
print(last1('mehraj'))

# now how we can use if else with lambda expression
def func(s):
    if len(s)>5:
        return True
    return False
print(func('hdhfsoshso'))


func1 = lambda s :True if len(s)>5 else False
print(func1('abhdw'))
# very short form
def func(s):
    return len(s)>5
      
print(func('hdhfsoshso'))

func1 = lambda s :len(s)>5 
print(func1('abhdw'))