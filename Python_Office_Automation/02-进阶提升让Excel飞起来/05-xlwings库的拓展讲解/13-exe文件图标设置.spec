# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['13-exe文件图标设置.py'],
             pathex=['E:\\study\\python\\Python_Office_Automation\\02-进阶提升让Excel飞起来\\05-xlwings库的拓展讲解'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='13-exe文件图标设置',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='1.ico')
