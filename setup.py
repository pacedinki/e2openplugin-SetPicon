from distutils.core import setup, Extension

pkg = 'Extensions.SetPicon'
setup (name = 'enigma2-plugin-extensions-setpicon',
       version = '0.35',
       description = 'work with picons',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg:
           ['plugin.png']},
      )