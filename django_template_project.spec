# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
    ('venv/lib/python3.8/site-packages/bootstrap4/templates', 'templates/'),
    ('templates/', 'templates/'),
    ('users/static/css/', 'staticfiles/css/'),
    ('users/static/img/', 'staticfiles/img/'),
]

h_imports = [
    'bootstrap4',
    'whitenoise',
    'whitenoise.middleware',
    'whitenoise.storage',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.auth'
]

a = Analysis(
    ['manage.py'],
    pathex=['venv/lib/python3.8/site-packages', 'venv/lib/python3.8/site-packages/bootstrap4/'],
    binaries=[],
    datas=added_files,
    hiddenimports=h_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='django_template_project',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='django_template_project',
)
