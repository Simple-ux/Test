1. def to_camel_case(text): 
       return re.split('_|-', text)[0].title() + ''.join(word.title() for word in re.split('_|-', text)[1::]) 
  
2. class SingletonMeta(type):

    _instances = {}

    def str(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
       
3. count_bits = lambda n: bin(n).count('1')

4. def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int,str(n))))
       
5. even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
