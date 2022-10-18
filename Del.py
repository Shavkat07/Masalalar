a = [1,2,3,4,5,6,7,8,9]

def delete(x,y):
    x = x[:y]+x[y+1:]
    return x
print(delete(a, 4))