from setuptools import setup, find_packages

version = '0.1'

setup(name='pygments-doconce',
      version=version,
      description='Syntax coloring for DocOnce markup language',
      #long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='pygments doconce lexer',
      author='Hans Petter Langtangen',
      author_email='hpl@simula.no',
      url='',
      license='BSD',
      py_modules=['doconce_lexer'],
      zip_safe=True,
      install_requires=[
          'setuptools',
      ],
      entry_points={
          'pygments.lexers': 'doconce=doconce_lexer:DocOnceLexer',
      },
)
