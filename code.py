1. def to_camel_case(text): 
       return re.split('_|-', text)[0].title() + ''.join(word.title() for word in re.split('_|-', text)[1::]) 
  
2. class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
       
 3. count_bits = lambda n: bin(n).count('1')
