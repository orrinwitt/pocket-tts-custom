# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

# Determine base path (works for both source and CI)
base_path = os.path.abspath(SPECPATH)

a = Analysis(
    ['pocket-tts-launcher.py'],
    pathex=[base_path],
    binaries=[],
    datas=[
        (os.path.join(base_path, 'pocket_tts', 'static'), 'pocket_tts/static'),
    ],
    hiddenimports=[
        'pocket_tts.main',
        'pocket_tts.data.audio',
        'pocket_tts.data.voices',
        'pocket_tts.utils',
        'fastapi',
        'uvicorn',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'starlette',
        'pydantic',
        'torch',
        'torchaudio',
        'transformers',
        'numpy',
        'huggingface_hub',
        'sentencepiece',
        'soundfile',
        'packaging',
        'filelock',
        'requests',
        'tqdm',
        'regex',
        'tokenizers',
        'safetensors',
        'yaml',
        'jinja2',
        'markupsafe',
        'typing_extensions',
    ],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PocketTTS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(base_path, 'pocket_tts', 'static', 'favicon.ico'),
)
