# no_init
Tool that checks that there are no `__init__.py` in your modules.  
It's opinionated tool, sometimes `__init__.py` files are useful. But often if you use them you end up in a circular import error mess. 

```py
# install
python -m pip install no_init

# usage
python -m no_init folder1, folder2, folder3 
```
