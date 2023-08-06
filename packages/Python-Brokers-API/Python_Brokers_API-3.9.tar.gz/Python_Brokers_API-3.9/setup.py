import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'Python_Brokers_API',         
  packages = ['Python_Brokers_API'],   
  version = '3.9',
  license='MIT',        
  description = 'A package to make requests to brokers like binance,kraken',   
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Hugo Demenez',                  
  author_email = 'hdemenez@hotmail.fr',     
  url = 'https://github.com/hugodemenez/Python_Brokers_API',   
  download_url = 'https://github.com/hugodemenez/Python_Brokers_API/archive/refs/tags/v3.9.tar.gz', 
  keywords = ['Python', 'Brokers', 'API'],   
  install_requires=[
          'requests',
          'ciso8601'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.9',    
  ],
)