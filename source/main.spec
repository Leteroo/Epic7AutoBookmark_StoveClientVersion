# -*- mode: python ; coding: utf-8 -*-

my_files = ['main.py', './api/WindowsOperation.py', './api/CVWindow.py']

a = Analysis(
    my_files,
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=['win32api', 'win32con', 'cv2', 'mss', 'numpy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    onefile=False,
    console=False,
    icon='main.ico',
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
	version='version.txt',
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['main.ico'],
)
