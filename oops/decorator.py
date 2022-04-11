
def validate(obj):
    def test(*args, **kwargs):
        a = args[0]
        b = args[1]
        if a ==0 or b == 0:
            raise Exception('value should not be zero')
        return obj(*args)
    return test


@validate
def addition(a,b):
    return a + b

print(addition(10,20))



def validate_age(obj):
    def inner_func(age):
        if age >18:
            return obj(age)
        else:
            print("age is not valid for voting")
    return inner_func

@validate_age
def vote(age):
    print("voting successfull")
vote(16)