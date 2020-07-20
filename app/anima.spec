# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['../src/anima.py'],
             pathex=['/home/fkubota/Git/anima/app'],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn', 'scipy.special.cython_special', 'sklearn.utils._cython_blas', 'sklearn.neighbors._typedefs', 'sklearn.neighbors._quad_tree', 'sklearn.tree', 'sklearn.tree._utils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='anima',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='anima')
