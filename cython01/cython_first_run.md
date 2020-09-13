# Cython Sample
## 파일 구성
* hello.pyx : 서비스 로직이 짜여있는 Cython 파일
    - 메소드 선언시 def는 python에서만 사용 가능 cdef 는 c언어에서만 가능, cpdef  c, python다 사용 가능
```
    from libc.math cimport pow

    cdef double square_and_add (double x):
        """Compute x^2 + x as double.
    
        This is a cdef function that can be called from within
        a Cython program, but not from Python.
        """
        return pow(x, 2.0) + x

    cpdef print_result (double x):
        """This is a cpdef function that can be called from Python."""
        print("({} ^ 2) + {} = {}".format(x, x, square_and_add(x)))
```
* setup.py : hello.pyx를 C컴파일러로 돌리기 위한 python 파일
```
    from distutils.core import Extension, setup
    from Cython.Build import cythonize
    
    # define an extension that will be cythonized and compiled
    ext = Extension(name="hello", sources=["hello.pyx"])
    setup(ext_modules=cythonize(ext))
```
* test.py : hello.pyx의 메소드를 실행하기 위한 파일
```
    # Import the extension module hello.
    import hello
    
    # Call the print_result method 
    hello.print_result(23.0)
```

## 컴파일 하기
* 1. hello.pyx, setup.py, test.py 파일이 있는 폴더로 이동
* 2. 다음의 명령어를 실행하여 hello.pyx 컴파일 하기
```
    python setup.py build_ext --inplace
```
* 3. hello.cp38-win_amd64.pyd, hello.c, hello.html 파일이 생성되어 사용 가능