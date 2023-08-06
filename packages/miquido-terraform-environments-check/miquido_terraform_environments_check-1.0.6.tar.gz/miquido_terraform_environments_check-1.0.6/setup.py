from distutils.core import setup
setup(
  name = 'miquido_terraform_environments_check',         # How you named your package folder (MyLib)
  packages = ['miquido_terraform_environments_check'],   # Chose the same as "name"
  version = '1.0.6',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'launches terraform validate on provided environments',   # Give a short description about your library
  author = 'Marek',                   # Type in your name
  author_email = 'marek.moscichowski@miquido.com',      # Type in your E-Mail
  keywords = ['GITLAB', 'TERRAFORM'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
